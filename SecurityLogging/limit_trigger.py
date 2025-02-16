from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import logging
import time
from collections import defaultdict
import json
LOG_FILE = "event.json"
RATE_LIMIT = 3

failed_attemps = defaultdict(int)

class SecurityLoggingHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(LOG_FILE):
            logging.info("File modified: %s", event.src_path)
            with open(LOG_FILE, 'r') as log:
                data = json.load(log)
                if data:
                    last_event = data[-1]
                    print('last event', last_event)
                    if last_event['status_code'] == 401:
                        ip_addr = last_event['ip_addr']
                        failed_attemps[ip_addr] += 1
                        if failed_attemps[ip_addr] >= RATE_LIMIT:
                            logging.error("Rate limit exceeded for %s", ip_addr)
                            logging.error('THIS IS AN ALERT, TAKE ACTION IMMEDIATELY')
                            failed_attemps[ip_addr] = 0

if __name__ == "__main__":
    event_handler = SecurityLoggingHandler()
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=False)
    observer.start()
    
    print("🔍 Monitoring security logs...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()