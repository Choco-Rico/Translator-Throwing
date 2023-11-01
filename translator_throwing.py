import keyboard
import subprocess
import time
import os
import win32gui
import win32con
import win32event
import win32api
import threading
import winerror
import sys
import json
from PIL import Image
import pystray
from pystray import MenuItem as item

def reset_and_restart():
    print("エラーが発生しました。アプリケーションを再起動します...")
    if mutex is not None:  # Mutexが存在する場合
        win32api.CloseHandle(mutex)
    os.execl(sys.executable, sys.executable, *sys.argv)

try:
    mutex = win32event.CreateMutex(None, 1, 'Translator_SingleInstanceMutex')
    if win32api.GetLastError() == winerror.ERROR_ALREADY_EXISTS:
        mutex = None
        print("既に別のインスタンスが実行中です。終了します。")
        sys.exit(0)

    count = 0
    timestamp = 0
    shutdown_event = threading.Event()  # シャットダウンを検知するためのイベント

    def monitor_shutdown():
        def on_shutdown_handler(hwnd, msg, wparam, lparam):
            if msg == win32con.WM_QUERYENDSESSION:
                print("シャットダウンまたは再起動中...")
                shutdown_event.set()  # シャットダウンイベントを設定
                return 0  # システムにシャットダウンを許可する
            return True

        win32gui.PumpMessages()

    # バックグラウンドでメッセージ監視スレッドを開始
    shutdown_thread = threading.Thread(target=monitor_shutdown)
    shutdown_thread.start()

    def on_hotkey():
        global count, timestamp
        try:
            current_time = time.time()

            if count == 0:
                timestamp = current_time
            elif count == 1 and current_time - timestamp <= 1:
                time.sleep(0.2)
                keyboard.send('ctrl+c')
                time.sleep(0.2)  # 必要に応じて調整
                keyboard.send('delete')
                subprocess.run([os.path.join('translate.exe')])
                keyboard.send('ctrl+v')

            count = (count + 1) % 2
        except Exception as e:
            print("エラーが発生しました:", e)
            reset_and_restart()  # エラーが発生した場合のリセット処理

    def load_hotkey():
        config_file_path = 'config.json'
        if os.path.exists(config_file_path):
            with open(config_file_path, 'r') as config_file:
                config = json.load(config_file)
                return config["hotkey"]  # ホットキーを返す
        else:
            print('デフォルトの設定ファイルを作成します')
            default_hotkey = "alt+C"
            config = {"hotkey": default_hotkey}
            with open(config_file_path, 'w') as config_file:
                json.dump(config, config_file)
            return default_hotkey  # デフォルトのホットキーを返す

    def update_hotkey():
        global hotkey
        new_hotkey = load_hotkey()
        if new_hotkey != hotkey:
            print(f"ホットキーが {hotkey} から {new_hotkey} に変更されました")
            keyboard.remove_hotkey(hotkey)
            hotkey = new_hotkey
            keyboard.add_hotkey(hotkey, on_hotkey)

    config_file_path = 'config.json'
    hotkey = load_hotkey()
    last_modified_time = os.path.getmtime(config_file_path)
    keyboard.add_hotkey(hotkey, on_hotkey)

    def create_icon(icon_path):
        image = Image.open(icon_path)
        icon = pystray.Icon("name", image, "Translator-Trowing", menu=pystray.Menu(item('Quit', exit_app)))
        icon.run()

    def exit_app(icon, item):
        icon.stop()
        os._exit(0)

    # アイコンのパスを指定
    icon_path = 'images/icon.ico'

    # アイコンを作成して実行
    create_icon(icon_path)

    try:
        while not shutdown_event.is_set():
            current_modified_time = os.path.getmtime(config_file_path)
            if current_modified_time != last_modified_time:
                update_hotkey()
                last_modified_time = current_modified_time
            time.sleep(1)
    except Exception as e:
        print(f"予期しないエラーが発生しました: {e}")
        reset_and_restart()
except:
    reset_and_restart()