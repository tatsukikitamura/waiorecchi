import requests
import time

def update_thm_badge():
    # キャッシュ回避用にタイムスタンプを付与
    api_url = f"https://tryhackme-badges.s3.amazonaws.com/tatsukikitamura.png?update=5"
    
    res = requests.get(api_url)
    if res.status_code == 200:
        with open("assets/thm_propic.png", "wb") as f:
            f.write(res.content)
        print("画像を更新しました")
    else:
        print(f"エラー: {res.status_code}")

update_thm_badge()