import os
import shutil
import datetime
import schedule
import time

source_dir = r"The\path\you\want\to\copy"
destination_dir = r"The\destination\you\want\to\copy\into"

def CFTD(source, dest):
    today = datetime.datetime.today()
    # Safe folder name
    safe_timestamp = today.strftime("%Y-%m-%d_%H-%M-%S")
    dest_dir = os.path.join(dest, safe_timestamp)

    try:
        shutil.copytree(source, dest_dir, dirs_exist_ok=True)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder already exists in: {dest}")

                    #you can put any time you want
schedule.every().day.at("10:30").do(lambda: CFTD(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)