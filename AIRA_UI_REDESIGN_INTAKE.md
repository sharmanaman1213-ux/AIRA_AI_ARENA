# AIRA AI — UI Redesign Project Intake

> **How to use this file:** Fill in whatever you can. You may paste file contents below the relevant sections, or attach/upload source files separately in batches. Do **not** include API keys, passwords, `.env` contents, tokens, or private credentials.

---

## 1. Project Overview

**Application name:** AIRA AI  
**Operating system target(s):** Windows 
**Python version:** Python 3.x
**UI framework (if known):** PyQt6  
**How to run the application:**
```bash
python main.py
```

**Main entry file:** `main.py`
**Current working directory / project name:** AIRA_AI

---

## 2. Project File Tree (Very Important)

**Paste project tree below:**
```text
C:\USERS\NAMAN\DOCUMENTS\NEW FOLDER\AIRA_AI MAIN\AIRA_AI
|   AIRA.spec
|   add_to_startup.vbs
|   fix_ui.py
|   main.py
|   pyrightconfig.json
|   readme.md
|   requirements.txt
|   setup.py
|   ui.py
|   
+---actions
|       background_monitor.py
|       browser_control.py
|       clap_detector.py
|       code_helper.py
|       computer_control.py
|       computer_settings.py
|       desktop.py
|       dev_agent.py
|       file_controller.py
|       file_processor.py
|       flight_finder.py
|       game_updater.py
|       open_app.py
|       proactive.py
|       reminder.py
|       screen_processor.py
|       send_message.py
|       study_guardian.py
|       system_monitor.py
|       weather_report.py
|       web_search.py
|       youtube_video.py
|           
+---config
|   |   api_keys.json (EXCLUDED)
|   |   jarvis.ico
|   |   __init__.py
|   |   
|   +---certs
|   |       jarvis.crt
|   |       jarvis.key
|           
+---core
|       installer.py
|       llm_client.py
|       prompt.txt
|       stt.py
|       tts.py
|       __init__.py
|       
+---dashboard
|   |   server.py
|   |   __init__.py
|   |   
|   +---static
|   |       app.html
|   |       crypto-js.min.js
|   |       login.html
|           
+---memory
|   |   config_manager.py
|   |   memory_manager.py
```

---

## 3. Essential Files to Share

### Required — First Batch
- [x] Main application entry file — e.g. `main.py`, `app.py`, `launcher.py`
- [x] Dependency file — `requirements.txt`, `pyproject.toml`, or `Pipfile`
- [x] Main window / UI bootstrap file (`ui.py`)
- [x] Existing chat UI and chat controller/handler file
- [x] Existing stylesheet/theme file(s), if any
- [x] README or current run instructions, if any

### Required — Feature Connection Files
- [x] AI chat request / streaming handler
- [x] Voice recognition handler
- [x] Text-to-speech / AI speaking handler
- [x] File upload and file-processing handler
- [x] Model selection function / model configuration UI
- [x] System monitoring service / CPU-RAM-GPU reader
- [x] Activity log service or event logger
- [x] Settings/configuration state and persistence logic

### Recommended — Existing Workspaces
- [x] Memory UI + memory service
- [ ] Projects / conversations UI
- [ ] Image generation workspace
- [ ] Presentation workspace
- [ ] Code workspace
- [ ] Workflow / agents UI and handlers
- [x] Icons, logo, images, custom fonts, and other assets

---

## 4. Current Feature Map

| Feature | File path | Class / function / signal / callback | Notes |
|---|---|---|---|
| App startup | `main.py` | `MainWindow` init | Bootstraps Qt app and UI |
| Main window | `ui.py` | `MainWindow` | Contains central HUD and layout |
| Send chat message | `ui.py` | `self.on_text_command(text)` | Emitted by `CommandInputArea` |
| Receive / stream AI response | `core/llm_client.py` | `llm_client` handlers | Managed by backend core |
| Stop generation | `ui.py` | `self.on_interrupt()` | Bound to Escape shortcut |
| Microphone / voice input | `core/stt.py` | Background listening | Triggered / muted via UI (F4) |
| Text-to-speech | `core/tts.py` | TTS engine | Linked to HUD visualizer |
| File upload | `ui.py` | `FileDropZone` | Handles drag & drop |
| File analysis | `actions/file_processor.py` | | Backend action |
| Model switcher | `ui.py` | `CustomizeOverlay` | Dropdown for mode/model |
| System monitor | `ui.py` | `_SysMetrics` | Updates `MetricBar` UI elements |
| Activity logs | `ui.py` | `_log_sig.emit(text)` | Written to Right Panel |
| Memory system | `memory/memory_manager.py` | | JSON storage |
| Settings | `ui.py` | `CustomizeOverlay` | Contains HueWheel / accent color |
| Fullscreen | `ui.py` | `self._toggle_fullscreen()` | F11 shortcut |
| Image studio | | | |
| Code workspace | `actions/code_helper.py` | | |
| Workflow / agents | | | |

---

## 5. Existing Signals, Events, or Callbacks

**Paste actual interfaces below:**
```python
# From ui.py (MainWindow & RootShim)
def on_text_command(self, text: str): ...
def on_remote_clicked(self): ...
def on_interrupt(self): ...
def on_mode_changed(self, mode: str): ...
def set_state(self, state: str): ...
def write_log(self, text: str): ...
def show_content(self, title: str, text: str): ...
def notify_phone_connected(self): ...
```

---

## 6. Backend and API Safety Notes

List the files/modules that should **not** be modified because they contain working backend/API/AI logic.

**Your protected files/modules:**
```text
- core/llm_client.py
- core/stt.py
- core/tts.py
- memory/memory_manager.py
- memory/config_manager.py
- actions/* (All backend skills/handlers)
- dashboard/server.py
```

---

## 7. Current Screenshots and Known Issues

**Current UI screenshots available:** Yes — reference screenshots already supplied  

---

## 8. Assets and Branding

| Asset | Existing file/path | Notes |
|---|---|---|
| App icon | `config/jarvis.ico` | Main executable / tray icon |

---

## 9. Platform and Constraints

- [x] Windows desktop
- [ ] macOS desktop
- [ ] Linux desktop
- [ ] Touch device support needed
- [ ] Offline/local model support
- [ ] Low-end hardware support important
- [x] Must retain current UI framework (yes)

**Minimum supported screen size:** 820x580 (defined in `_MIN_W, _MIN_H`)  
**Preferred desktop resolution:** 980x700 (defined in `_DEFAULT_W, _DEFAULT_H`)  
**Any packaging method (PyInstaller, etc.):** PyInstaller (`AIRA.spec`)  

---

## 10. Safe Sharing Checklist

Before sharing files, remove or redact:

- [x] `.env` files
- [x] API keys
- [x] Provider tokens
- [x] Database passwords
- [x] Personal paths if sensitive
- [x] Private certificates
- [x] Production user data / chat logs
