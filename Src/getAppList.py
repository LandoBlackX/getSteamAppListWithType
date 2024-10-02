import sqlite3
import time

import requests

getAppList_URL = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

response = requests.get(getAppList_URL)

if response.status_code == 200:
    start_time = time.time()
    data = response.json()
    app_list = data['applist']['apps']
    app_ids = [(app['appid'],) for app in app_list]

    conn = sqlite3.connect('app_list.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS
    apps (
        appid INTEGER PRIMARY KEY,
        status BOOLEAN DEFAULT FALSE
    )
    ''')
    conn.commit()

    new_count = 0
    for app_id in app_ids:
        cursor.execute('''
            INSERT OR IGNORE INTO apps (appid) VALUES (?) ''', app_id)
        if cursor.rowcount > 0:
            new_count += 1
            print(f"新增 appid: {app_id[0]}")

    conn.commit()
    end_time = time.time()
    conn.close()
    total_time = end_time - start_time
    print(f"新增 {new_count} 个 appid ,已成功写入数据库。")
    print(f"总耗费时间: {total_time:.6f} 秒")
else:
    print(f"请求失败，状态码: {response.status_code}")
