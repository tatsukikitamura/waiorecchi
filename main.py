import requests
import os

# TryHackMe APIからバッジ画像を取得
def fetch_thm_badge(output_file="/assets/thm_propic.png"):
    api_url = f"https://tryhackme-badges.s3.amazonaws.com/tatsukikitamura.png"
    
    try:
        # APIリクエストを送信
        
        response = requests.get(api_url)
        response.raise_for_status()  # エラーチェック
        
        # JSONデータから画像URLを抽出
        data = response.json()
        if not data.get("success", False):
            raise Exception("API returned an error")
        
        badge_url = data["badges"][0]["icon"]  # 最新バッジの画像URLを取得
        
        # 画像をダウンロード
        img_response = requests.get(badge_url)
        img_response.raise_for_status()
        
        # 画像を保存
        with open(output_file, "wb") as f:
                f.write(img_response.content)
        
        print(f"✅ Successfully saved badge image to: {output_file}")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    fetch_thm_badge()  # デフォルトで userPublicId=4877687 を使用