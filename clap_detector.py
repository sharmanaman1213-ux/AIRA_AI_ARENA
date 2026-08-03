import time
import numpy as np
import sounddevice as sd
from PyQt6.QtCore import QObject, pyqtSignal, QThread

class ClapDetector(QThread):
    on_double_clap = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self._running = True
        self.threshold = 0.12  # Adjust based on microphone sensitivity
        self.min_delay = 0.15
        self.max_delay = 0.8
        
    def run(self):
        chunk_size = 1024
        sample_rate = 16000
        
        last_clap_time = 0
        
        def audio_callback(indata, frames, time_info, status):
            nonlocal last_clap_time
            if not self._running:
                raise sd.CallbackStop()

            if status:
                pass
            
            # Calculate RMS amplitude
            rms = np.sqrt(np.mean(indata**2))
            
            if rms > self.threshold:
                now = time.time()
                delay = now - last_clap_time
                if delay > 0.08:  # Debounce within 80ms to avoid single-clap echo
                    if self.min_delay < delay < self.max_delay:
                        # Double clap detected!
                        self.on_double_clap.emit()
                        last_clap_time = 0 # Reset to prevent triple-clap triggering twice
                    else:
                        # Potential first clap
                        last_clap_time = now
                
        try:
            with sd.InputStream(samplerate=sample_rate, channels=1, dtype='float32', blocksize=chunk_size, callback=audio_callback):
                while self._running:
                    time.sleep(0.1)
        except Exception as e:
            print(f"[ClapDetector] Error: {e}")

    def stop(self):
        self._running = False
