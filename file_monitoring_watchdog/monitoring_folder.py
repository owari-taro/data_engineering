from watchdog.events import FileSystemEventHandler,RegexMatchingEventHandler
from watchdog.observers import Observer

# ファイルアクセスとスリープのため、osとtimeをインポート
import os
import time
from pathlib import Path
# 監視対象ディレクトリを指定する
target_dir = '/home/tarob/git_repos/data_engineering/file_monitoring_watchdog'

# FileSystemEventHandler の継承クラスを作成
class FileChangeHandler(FileSystemEventHandler):
     # ファイル作成時のイベント
     def on_created(self, event):
         filepath = event.src_path
         test=Path(filepath)
         print(test)
         filename = os.path.basename(filepath)
         print('%s created' % filename)
         time.sleep(20)
         print("++++++++++++++++++++++++++++++++")

     # ファイル変更時のイベント
     def on_modified(self, event):
         filepath = event.src_path

         filename = os.path.basename(filepath)
         print('%s changed' % filename)

     # ファイル削除時のイベント
     def on_deleted(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s deleted' % filename)

     # ファイル移動時のイベント
     def on_moved(self, event):
         filepath = event.src_path
         filename = os.path.basename(filepath)
         print('%s moved' % filename)

# コマンド実行の確認
if __name__ == "__main__":
     # ファイル監視の開始
     event_handler = FileChangeHandler()
     observer = Observer()
     observer.schedule(event_handler, target_dir, recursive=True)
     observer.start()
     # 処理が終了しないようスリープを挟んで無限ループ
     try:
         while True:
             time.sleep(1)
     except KeyboardInterrupt:
         observer.stop()
     observer.join()