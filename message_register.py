import itchat
import random
import os
from child_message_handler import *
from robot_config import *
from itchat.content import *

@itchat.msg_register(TEXT,isFriendChat=True, isMpChat=True)
def text_reply(msg):
	print(msg)
	msgHandler = TextMessageHandler()
	return msgHandler.handleMessage(msg);

@itchat.msg_register(FRIENDS)
def add_friend(msg):
	print(msg)
	itchat.add_friend(**msg['Text']) # 该操作会自动将新好友的消息录入，不需要重载通讯录
	response_list = ['你好，很高兴认识你，我是'+robot_name,
			'你好，上知天文下知地理的'+robot_name+'就是我啦~',
			'太好了，终于遇见你，以后多多指教哦，我是'+robot_name]
	itchat.send_msg(random.choice(response_list), msg['RecommendInfo']['UserName'])

@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply(msg):
	if msg['isAt']:
		msgHandler = TextMessageHandler()	
		userid = msg['FromUserName']
		text = msg['Content'].replace('@'+robot_name,' ')
		response = msgHandler.handleMessage(msg,userid,text);
		itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], response), msg['FromUserName'])

@itchat.msg_register([PICTURE, ATTACHMENT, VIDEO])
def download_files(msg):
	img_count = get_img_count()
	img_i = random.randint(1, img_count);
	return '@img@' + 'image/' + str(img_i) + '.jpg'
	#return '还是和我聊天吧，' + robot_name + '现在还处理不了这些内容 - -||'
	#msg['Text'](msg['FileName'])
	#response = '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
	#return response

@itchat.msg_register(RECORDING,isFriendChat=True, isMpChat=True)
def voice_reply(msg):
	msgHandler = VoiceMessageHandler()
	return msgHandler.handleMessage(msg)

def get_img_count():
	output = os.popen('ls -l image/ |grep "^-"|wc -l')
	count_str = output.read().strip()
	count = int(count_str)
	return count
