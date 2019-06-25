 From flask import Flask, request, abort 
  From linebot import ( 
  LineBotApi, WebhookHandler 
  ) 
  From linebot.exceptions import ( 
  InvalidSignatureError 
  ) 
  From linebot.models import * 
  App = Flask( __name__ ) 
  # Channel Access Token 
  Line_bot_api = LineBotApi( 'JAkiT/xizWqtsFMxzFZHUVxx5yacRkBjSDgvU+ulNTD6L/HfeVwtelULk5nPmQxLro3UgB5TjhPl5LIfXOYyXuxbJcRsTQWBcXKjUw9YXZZVlwbCWTBXmnsLaBqNSTT8f5OIk/aV6kffghU4M3sNPAdB04t89/1O/w1cDnyilFU=' ) 
  # Channel Secret 
  Handler = WebhookHandler( '3ec036fffe82cfcc225679876cb63c78' ) 
  #Listen all Post requests from /callback 
  @app.route ( " /callback " , methods = [ ' POST ' ]) 
  Def callback (): 
  # get X-Line-Signature header value 
  Signature = request.headers[ ' X-Line-Signature ' ] 
  # get request body as text 
  Body = request.get_data( as_text = True ) 
  App.logger.info( " Request body: " + body) 
  # handle webhook body 
  Try : 
  Handler.handle(body, signature) 
  Except InvalidSignatureError: 
  Abort( 400 ) 
  Return ' OK ' 
  #处理消息 
  @handler.add (MessageEvent, message = TextMessage) 
  Def handle_message ( event ): 
  Message = TextSendMessage( text = event.message.text) 
  Line_bot_api.reply_message(event.reply_token, message) 
  Import os 
  If __name__ == " __main__ " : 
  Port = int (os.environ.get( ' PORT ' , 5000 )) 
  App.run( host = ' 0.0.0.0 ' , port = port) 