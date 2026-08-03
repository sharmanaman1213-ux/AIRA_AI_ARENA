import time
import json
import os
import threading
from pathlib import Path
from typing import Dict, Any, List

import psutil
try:
    import ctypes
    from ctypes import wintypes
    user32 = ctypes.windll.user32
    _CTYPES_AVAILABLE = True
except Exception:
    _CTYPES_AVAILABLE = False


class StudyGuardian:
    def __init__(self, ui=None):
        self.ui = ui
        self.is_study_mode = False
        self.tasks: List[Dict[str, Any]] = []
        self.current_task_index = -1
        
        self.screen_monitoring_enabled = True
        self.autonomous_mode = True
        self.strict_mode = False
        
        self._distraction_grace_period = 60 # seconds
        self._last_task_related_time = time.time()
        self._monitor_thread = None
        self._running = False
        
        self._last_window_title = ""
        self._distraction_start_time = 0.0

    def set_mode(self, enabled: bool):
        self.is_study_mode = enabled
        if enabled:
            if not self._running:
                self.start_monitoring()
        else:
            self.stop_monitoring()
            
    def get_current_task(self) -> str:
        if self.current_task_index >= 0 and self.current_task_index < len(self.tasks):
            return self.tasks[self.current_task_index].get('name', 'Unknown Task')
        return "No active task"

    def add_task(self, task_desc: str):
        self.tasks.append({"name": task_desc, "completed": False})
        if self.current_task_index == -1:
            self.current_task_index = 0
            
    def complete_current_task(self):
        if self.current_task_index >= 0 and self.current_task_index < len(self.tasks):
            self.tasks[self.current_task_index]["completed"] = True
            self.current_task_index += 1
            if self.current_task_index >= len(self.tasks):
                return "All tasks completed!"
            return f"Next task: {self.get_current_task()}"
        return "No active task to complete."

    def get_active_window_title(self) -> str:
        if not _CTYPES_AVAILABLE: return ""
        hwnd = user32.GetForegroundWindow()
        length = user32.GetWindowTextLengthW(hwnd)
        buf = ctypes.create_unicode_buffer(length + 1)
        user32.GetWindowTextW(hwnd, buf, length + 1)
        return buf.value

    def start_monitoring(self):
        self._running = True
        self._last_task_related_time = time.time()
        self._monitor_thread = threading.Thread(target=self._monitor_loop, daemon=True)
        self._monitor_thread.start()

    def stop_monitoring(self):
        self._running = False

    def is_likely_distraction(self, title: str) -> bool:
        title = title.lower()
        distractions = ["instagram", "facebook", "tiktok", "netflix", "game", "steam", "riot"]
        for d in distractions:
            if d in title:
                return True
        return False

    def _monitor_loop(self):
        while self._running:
            time.sleep(5)
            if not self.screen_monitoring_enabled or self.current_task_index == -1:
                continue
                
            title = self.get_active_window_title()
            if not title: continue
            
            if title != self._last_window_title:
                self._last_window_title = title
            
            if self.is_likely_distraction(title):
                if self._distraction_start_time == 0.0:
                    self._distraction_start_time = time.time()
                elif time.time() - self._distraction_start_time > self._distraction_grace_period:
                    self.trigger_reminder(title)
                    self._distraction_start_time = 0.0
            else:
                self._distraction_start_time = 0.0
                self._last_task_related_time = time.time()
                
    def trigger_reminder(self, window_title: str):
        if self.ui:
            self.ui.write_log(f"SYS: You seem distracted by '{window_title}'. Current Task: {self.get_current_task()}")
            if self.strict_mode and _CTYPES_AVAILABLE:
                hwnd = user32.GetForegroundWindow()
                user32.ShowWindow(hwnd, 6) # SW_MINIMIZE = 6

study_guardian_instance = StudyGuardian()
