from flask import Flask, request, abort

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import json
import random
import os

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi(os.environ.get("LINE_CHANNEL_ACCESS_TOKEN"))
# Channel Secret
handler = WebhookHandler(os.environ.get("LINE_CHANNEL_SECRET"))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"


# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == "查看農民曆":
        text = "今天又是新的一天！📢\n提醒您接下來的重大節日有：\n1.開鬼門\n🕐時間：國曆7/29(倒數43天)\n🚩相關資料：\n(1)開鬼門拜拜要注意什麼？🆖⚠️\nhttps://www.edh.tw/article/22301\n(2)開鬼門祭品準備⚠️\nhttps://www.cool3c.com/article/163767\n🚩合作廟宇夥伴資訊：\n(1)大甲鎮瀾宮-線上代辦中元普渡（慶贊中元-澎派組)\nhttps://reurl.cc/Dy7omm\n(2)鹿港天后宮-普渡消災金\nhttps://www.lugangmazu.org/home.php\n(更多詳細資訊請點選「祭拜補給站」)\n\n想要查詢其他農民曆，請到官方網站喔！"
        line_bot_api.reply_message(
            event.reply_token,
            [
                ImageSendMessage(
                    original_content_url="https://github.com/Tonyrj3268/temple-test/blob/main/%E8%BE%B2%E6%B0%91%E6%9B%86.png?raw=true",
                    preview_image_url="https://github.com/Tonyrj3268/temple-test/blob/main/%E8%BE%B2%E6%B0%91%E6%9B%86.png?raw=true",
                ),
                TextSendMessage(text=text),
            ],
        )
        # line_bot_api.reply_message(event.reply_token,[ImageSendMessage(original_content_url='https://github.com/Tonyrj3268/temple-test/blob/main/%E8%BE%B2%E6%B0%91%E6%9B%86.png?raw=true',preview_image_url='https://github.com/Tonyrj3268/temple-test/blob/main/%E8%BE%B2%E6%B0%91%E6%9B%86.png?raw=true')])

    elif event.message.text == "我要求籤":
        # FlexMessage = json.load(open('test.json','r',encoding='utf-8'))
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text="profile",
                contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.15752-9/248182057_398474188548443_8524158146577294049_n.png?_nc_cat=100&ccb=1-6&_nc_sid=ae9488&_nc_ohc=COTA1dt-d3UAX8332SY&_nc_ht=scontent.ftpe7-1.fna&oh=03_AVKncHEX8i97x6-_0WMJErqCz1qUd0bEkOClQt2QyOOTCQ&oe=62A49356",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {"type": "uri", "uri": "http://linecorp.com/"},
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "現在，你已從籤筒中抽中了一隻籤，準備好打開了嘛！",
                                "weight": "bold",
                                "size": "sm",
                                "wrap": True,
                            }
                        ],
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                    "type": "message",
                                    "label": "豪！我準備好了",
                                    "text": "我準備好了！",
                                },
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "margin": "sm",
                            },
                        ],
                        "flex": 0,
                    },
                },
            ),
        )
    elif event.message.text == "我要拜月老":
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text="profile",
                contents=(
                    {
                        "type": "bubble",
                        "hero": {
                            "type": "image",
                            "url": "https://scontent.xx.fbcdn.net/v/t1.15752-9/248072448_892728564699227_4638610249510133605_n.png?stp=dst-png_p206x206&_nc_cat=111&ccb=1-6&_nc_sid=aee45a&_nc_ohc=wjjPq4HDNxkAX8YKaZI&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AVLlX2Z_wxT100grlOhfeWlxW1E-MdzciNm6YxIKWooVmg&oe=62A59E3C",
                            "size": "full",
                            "aspectRatio": "20:13",
                            "aspectMode": "cover",
                            "action": {"type": "uri", "uri": "http://linecorp.com/"},
                        },
                        "body": {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                                {
                                    "type": "text",
                                    "text": "請跟著圖上指示，在心中詳細描述理想對象的外在與內涵。讓月老在茫茫人海中找到他，替你的感情路牽線。",
                                    "weight": "bold",
                                    "size": "sm",
                                    "wrap": True,
                                }
                            ],
                        },
                        "footer": {
                            "type": "box",
                            "layout": "vertical",
                            "spacing": "sm",
                            "contents": [
                                {
                                    "type": "button",
                                    "style": "link",
                                    "height": "sm",
                                    "action": {
                                        "type": "message",
                                        "label": "好！我準備好了",
                                        "text": "請幫我牽線吧～",
                                    },
                                },
                                {
                                    "type": "box",
                                    "layout": "vertical",
                                    "contents": [],
                                    "margin": "sm",
                                },
                            ],
                            "flex": 0,
                        },
                    }
                ),
            ),
        )
    elif event.message.text == "祭拜補給站":
        text = "\n【⚠️官網尚未建置】\n\n感謝您使用「祭拜補給站」功能，官網尚未建置完成，請稍後片刻，預計6/30日正式上線，敬請期待😎\n\n祭拜補給站介紹：\n🎈動動手指準備好拜拜用品\n🎈全台法會、節慶一站報名\n🎈完整祈福項目、神明\n🎈宮廟開立證明狀，虛擬融合更安心。\n\n祭拜補給站功能與全台各地廟宇合作，不需出門就能完成平安點燈。歡迎到官網使用功能喔❤️"

        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=text)])

    elif event.message.text == "查看廟宇資訊":
        text = "【⚠️官網尚未建置】\n\n感謝您使用「廟宇資訊」功能，官網尚未建置完成，請稍後片刻，預計6/30日正式上線，敬請期待😎\n\n廟宇資訊功能介紹：\n🎈完整全台廟宇資訊\n🎈合作夥伴官網介紹\n🎈關注功能：及時掌握廟宇資訊\n🎈分門別類，尋找廟宇更輕鬆\n\n廟宇資訊包含全台各地廟宇資訊，讓你隨時掌握關注中廟宇資訊。歡迎到官網使用功能喔❤️"

        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=text)])

    elif event.message.text == "前往線上點燈":
        text = "【⚠️官網尚未建置】\n\n感謝您使用「線上點燈服務」功能，官網尚未建置完成，請稍後片刻，預計6/30日正式上線，敬請期待😎\n\n線上點燈介紹：\n🎈實體與虛擬平安燈\n🎈祈福項目與神明分類\n🎈平安燈廣場上分享祝福\n🎈宮廟開立證明狀，虛擬融合更安心。\n\n線上點燈功能與全台各地廟宇合作，不需出門就能完成平安點燈。歡迎到官網使用功能喔❤️"

        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=text)])
    elif event.message.text == "拜拜工具書":
        text = "【⚠️官網尚未建置】\n感謝您使用「拜拜工具書」功能，官網尚未建置完成，請稍後片刻，預計6/30日正式上線，敬請期待😎\n拜拜工具書介紹：\n🎈查詢祭拜、節慶資訊\n🎈完整的祭拜與法會資訊\n🎈相關宮廟、服務連結\n\n拜拜工具書紀錄全年每一節日與祭拜的完整資訊，歡迎到官網使用功能喔❤️"
        line_bot_api.reply_message(event.reply_token, [TextSendMessage(text=text)])

    elif event.message.text == "開始線上抽籤":
        line_bot_api.reply_message(
            event.reply_token,
            FlexSendMessage(
                alt_text="profile",
                contents={
                    "type": "bubble",
                    "hero": {
                        "type": "image",
                        "url": "https://scontent.ftpe7-1.fna.fbcdn.net/v/t1.15752-9/248182057_398474188548443_8524158146577294049_n.png?_nc_cat=100&ccb=1-6&_nc_sid=ae9488&_nc_ohc=COTA1dt-d3UAX8332SY&_nc_ht=scontent.ftpe7-1.fna&oh=03_AVKncHEX8i97x6-_0WMJErqCz1qUd0bEkOClQt2QyOOTCQ&oe=62A49356",
                        "size": "full",
                        "aspectRatio": "20:13",
                        "aspectMode": "cover",
                        "action": {"type": "uri", "uri": "http://linecorp.com/"},
                    },
                    "body": {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [
                            {
                                "type": "text",
                                "text": "現在，你已從籤筒中抽中了一隻籤，準備好打開了嘛！",
                                "weight": "bold",
                                "size": "sm",
                                "wrap": True,
                            }
                        ],
                    },
                    "footer": {
                        "type": "box",
                        "layout": "vertical",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "button",
                                "style": "link",
                                "height": "sm",
                                "action": {
                                    "type": "message",
                                    "label": "豪！我準備好了",
                                    "text": "我準備好了！",
                                },
                            },
                            {
                                "type": "box",
                                "layout": "vertical",
                                "contents": [],
                                "margin": "sm",
                            },
                        ],
                        "flex": 0,
                    },
                },
            ),
        )


import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
