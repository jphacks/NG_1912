import os
from flask import Flask, request, abort, render_template, redirect
import requests
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.models import (
    MessageEvent,
    TextMessage,
    TextSendMessage,
    FlexSendMessage,
    BubbleContainer,
    StickerSendMessage,
    QuickReply,
    QuickReplyButton,
    MessageAction,
    URIAction,
    TemplateSendMessage,
    ButtonsTemplate,
    PostbackAction
)

access_token = "QOWpUISg/uvJVpPk25KsJwyrBwrvq7ltCxHE0TRjxlfABMwg5pDa3jmAaoKIgmhU9YPZBF97NSpewbDNff1XEEyVymF6Ob0MPqqeBqIX2pCZ9Q7ugEdmE6zAtmmF7t0Bn/78DU+XaTtcq8YZ+I+MHwdB04t89/1O/w1cDnyilFU="
bot_secret = "0f5a26663f1b87d3265a89a858d565ca"
line_bot_api = LineBotApi(access_token)
handler = WebhookHandler(bot_secret)
app = Flask(__name__, static_folder='static')
bootstrap = Bootstrap(app)
CORS(app)

import json
import shelve
import uuid

class LinePay(object):

    DEFAULT_ENDPOINT = 'https://sandbox-api-pay.line.me/'
    VERSION = 'v2'


    def __init__(self, channel_id, channel_secret, redirect_url):
        self.channel_id = channel_id
        self.channel_secret = channel_secret
        self.redirect_url = redirect_url

    def reserve(self, product_name, amount, currency, order_id, UserId, **kwargs):
        url = '{}{}{}'.format(self.DEFAULT_ENDPOINT, self.VERSION, '/payments/request')
        data = {**
                {
                    'productName':product_name,
                    'amount':amount,
                    'currency':currency,
                    'confirmUrl':'https://{}{}'.format(request.environ['HTTP_HOST'], self.redirect_url),
                    'orderId':order_id,
                },
                **kwargs}
        headers = {'Content-Type': 'application/json',
                   'X-LINE-ChannelId':self.channel_id,
                   'X-LINE-ChannelSecret':self.channel_secret}
        response = requests.post(url, headers=headers, data=json.dumps(data).encode("utf-8"))

        if int(json.loads(response.text)['returnCode']) == 0:
            with shelve.open('store') as store:
                # just for prototyping
                store[str(json.loads(response.text)['info']['transactionId'])] = {'productName': product_name, 'amount': amount, 'currency': currency, 'user':UserId, 'orderId':order_id}
            return json.loads(response.text)

        else:
            abort(400, json.loads(response.text)['returnCode'] + ' : ' + json.loads(response.text)['returnMessage'])

    def confirm(self, transaction_id):
        transaction_info = {}
        with shelve.open('store') as store:
            transaction_info = store[transaction_id]
            print(transaction_info)

        if len(transaction_info) == 0:
            abort(400, 'reservation of this transaction id is not exists')

        url = '{}{}{}'.format(self.DEFAULT_ENDPOINT, self.VERSION, '/payments/{}/confirm'.format(transaction_id))
        data = {
                'amount':transaction_info['amount'],
                'currency':transaction_info['currency'],
                }
        headers = {'Content-Type': 'application/json',
                   'X-LINE-ChannelId':self.channel_id,
                   'X-LINE-ChannelSecret':self.channel_secret}
        response = requests.post(url, headers=headers, data=json.dumps(data).encode("utf-8"))
        print(url)
        print(data)
        print(headers)
        return transaction_info

# get it in https://pay.line.me/jp/developers/techsupport/sandbox/creation?locale=ja_JP
chennel_id = '1653356129'
channel_secret = '7081575736c14da990811be96fce8637'
callback_url = '/callback'

"""
# get these at https://pay.line.me/center/notice/list after creating sandbox sandbox
chennel_id = YOUR_LINE_PAY_CHANNEL_ID
channel_secret = YOUR_LINE_PAY_CHANNEL_SECRET
callback_url = '/callback'
"""
pay = LinePay(chennel_id, channel_secret, callback_url)

@app.route("/")
def render_index():
    item_id = request.args.get("itemName")
    return render_template('index.html', data=item_id)

@app.route("/app")
def render_index_app():
    return redirect('tokimeter:')

@app.route("/reserve/<UserId>/<itemName>", methods=["POST"])
def redirect_to_pay(UserId=None, itemName=None):
    print("got: ", request.form)
    data = {"product_name": itemName,
            'amount':'100',
            'currency':'JPY',
            'order_id':uuid.uuid4().hex,
            "UserId":UserId,
            # optional values can be set. see https://pay.line.me/file/guidebook/technicallinking/LINE_Pay_Integration_Guide_for_Merchant-v1.1.2-JP.pdf
            'productImageUrl':'https://{}{}'.format(request.environ['HTTP_HOST'], '/static/cola.jpeg')
            }
    transaction_info = pay.reserve(**data)
    print(transaction_info['info']['paymentUrl']['web'])
    return transaction_info['info']['paymentUrl']['web']

@app.route("/callback")
def callback_from_pay():
    transaction_info = pay.confirm(request.args.get('transactionId'))
    print("trasaction: ",transaction_info)
    # push message to trasaction_info['user']
    userId = transaction_info['user']
    profile = line_bot_api.get_profile(userId).display_name

    with open("recipt.json", "r", encoding="utf-8") as f:
        json_data = json.load(f)
        json_data["body"]["contents"][6]["contents"][1]["text"] = transaction_info["orderId"]
        line_bot_api.push_message(
            userId,
                [
                    FlexSendMessage(
                        alt_text="レシート",
                        contents=BubbleContainer.new_from_json_dict(json_data)
                    ),
                    StickerSendMessage(
                        package_id=2,
                        sticker_id=41
                    )
                ]
            )
    return render_template('purchased.html', **transaction_info)

@app.route("/bot", methods=["POST"])
def return_bot():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        data = json.loads(body)
        userId = data["events"][0]["source"]["userId"]
        if userId == "Udeadbeefdeadbeefdeadbeefdeadbeef":
            return "OK"
        handler.handle(body, signature)

        # with open("alert.json", "r", encoding="utf-8") as f:
        #     json_data = json.load(f)
        #     syohin = data["events"][0]["message"]["text"]
        #     print(syohin)
        #     json_data["footer"]["contents"][0]["action"]["uri"] = "line://app/1653356763-y5x3nxO4&itemName=" + syohin
        #     line_bot_api.push_message(
        #         userId,
        #             [
        #                 FlexSendMessage(
        #                     alt_text="お支払いがあります",
        #                     contents=BubbleContainer.new_from_json_dict(json_data)
        #                 )
        #             ]
        #         )
    except Exception as e:
        print(e)
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    buttons_template_message = TemplateSendMessage(
        alt_text='お支払いの連絡',
        template=ButtonsTemplate(
            thumbnail_image_url='https://scdn.line-apps.com/n/channel_devcenter/img/fx/01_1_cafe.png',
            title='お支払いの連絡',
            text='LinePayでお支払いを完了してください',
            actions=[
                URIAction(
                    label='LINEPayで支払い',
                    uri="line://app/1653356763-y5x3nxO4?itemName="+event.message.text
                )
            ]
        )
    )
    line_bot_api.reply_message(
        event.reply_token,
        buttons_template_message
    )



@app.errorhandler(400)
def handler_error_400(error):
    return error

if __name__ == '__main__':
    app.debug = True
    app.run()
