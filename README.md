
## Description

企业微信群机器人Webhook Python 客户端. 支持文本消息, markdown, 图片, 图文, 文件 消息 ( https://work.weixin.qq.com/api/doc/90000/90136/91770 ).

A wechat work webhook Python client which support text, markdown, image, news, file message ( https://work.weixin.qq.com/api/doc/90000/90136/91770 ).

## Install

```
pip install --upgrade wechat_work_webhook
```

## Examples

```
import wechat_work_webhook
wechat = wechat_work_webhook.connect("webhook_url")

wechat.text('test',['@all'])

wechat.markdown('实时新增用户反馈<font color=\"warning\">132例</font>，请相关同事注意。')

wechat.image('test.png')

wechat.news([{
               "title" : "中秋节礼品领取",
               "description" : "今年中秋节公司有豪礼相送",
               "url" : "URL",
               "picurl" : "http://res.mail.qq.com/node/ww/wwopenmng/images/independent/doc/test_pic_msg1.png"
           }])

wechat.media(wechat.upload_media('test.csv')['media_id'])

wechat.file('test.csv')


# send pandas dataframe to wechat work as image:
# pip install dataframe_image
wechat.df(df)

```