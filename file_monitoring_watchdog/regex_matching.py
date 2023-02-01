from watchdog.events import RegexMatchingEventHandler
from watchdog.observers import Observer
import os
import time

if __name__ == "__main__":

    # 対象ディレクトリ

    DIR_WATCH ='/home/tarob/git_repos/data_engineering/file_monitoring_watchdog'

    # 対象ファイルパスのパターン
    PATTERNS = [r'^.*\.txt$']

    def on_modified(event):
        filepath = event.src_path
        filename = os.path.basename(filepath)
        print('%s changed' % filename)

    event_handler = RegexMatchingEventHandler(PATTERNS)
    
    observer = Observer()
    observer.schedule(event_handler, DIR_WATCH, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()