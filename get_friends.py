import itchat
import re, sys, json
from itchat.content import *


itchat.auto_login(enableCmdQR=2)
friends = itchat.get_friends()

for f in friends:
	if f['NickName'] == "培林" or f['NickName']== "张强":
		print(f)

@itchat.msg_register(SYSTEM)
def get_uin(msg):
	if msg['SystemInfo'] != 'uins': return
	ins = itchat.instanceList[0]
	fullContact = ins.memberList + ins.chatroomList + ins.mpList
	print('** Uin Updated **')
	for username in msg['Text']:
		member = itchat.utils.search_dict_list(
		fullContact, 'UserName', username)
		print(('%s: %s' % (member.get('NickName', ''), member['Uin'])).encode(sys.stdin.encoding, 'replace'))

@itchat.msg_register(TEXT,isFriendChat=True, isMpChat=True)
def text_reply(msg):
	print(msg)
	userName = msg['FromUserName']
	ins = itchat.instanceList[0]
	fullContact = ins.memberList + ins.chatroomList + ins.mpList
	member = itchat.utils.search_dict_list(fullContact, 'UserName',userName)
	print('%s: %s' % (member.get('NickName', ''), member['Uin']))

itchat.run()
