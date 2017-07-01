from flask import Flask
from flask import request
from flask import jsonify
from flask import abort
import itchat
import uuid
import time
import random
import message_register
from short_uid_generator import *
from message_handler import *

app = Flask(__name__)

@app.route('/wechat/robot/webhook', methods=['POST'])
def get_msg_from_robot_server():
	if not request.json:
		return jsonify({'code':0,'text':"请保证body数据为json格式"}) , 500
	if not 'userid' in request.json:
		return jsonify({'code':0,'text':"json中未包含userid"}) , 500

	userid = request.json['userid'];
	messageHandler = MessageHandler()
	msg = messageHandler.handleRobotResult(request.json)
	user = itchat.search_friends(name=userid)[0]
	itchat.send(msg,user["UserName"])
	return jsonify({'code':1,'text':"发送成功"}) , 200


def update_remark_name():
	friends = itchat.get_friends()
	updateNum = 0
	for f in friends:
		userName = f["UserName"]
		nickName = f["NickName"]
		remarkName = f["RemarkName"]
		if remarkName == '':
			print("开始设置第" +str(updateNum)+ "位好友的备注名")
			uid = generate_short_uid()
			resp = itchat.set_alias(userName,uid)
			print(resp)
			updateNum = updateNum + 1
			print("NickName:" +nickName )
			t = random.randint(7,15)
			time.sleep(t) #这里需要放慢请求微信的速度，因为请求过快，微信会阻止后续请求
			#if updateNum == 10:
			#break
			if resp['BaseResponse']['Ret'] != 0:
				print("退出好友备注更新，机器人启动开始")
				break
	print("已更新"+str(updateNum)+"位好友的备注")



itchat.auto_login(enableCmdQR=2)

update_remark_name()

itchat.run(blockThread=False)

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=5001)
