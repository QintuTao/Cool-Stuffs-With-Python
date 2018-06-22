
import re
import time
import itchat
from itchat.content import *


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
def text_reply(msg):
	print(msg['Text'])


@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])
@itchat.msg_register([TEXT, PICTURE, MAP, CARD, NOTE, SHARING, RECORDING, ATTACHMENT, VIDEO])


def text_reply(msg):
	reply_content = ""
	if msg['Type'] == 'Text':
		reply_content = msg['Text']
	elif msg['Type'] == 'Picture':
		reply_content = r"图片: " + msg['FileName']
	elif msg['Type'] == 'Card':
		reply_content = r" " + msg['RecommendInfo']['NickName'] + r" 的名片"
	elif msg['Type'] == 'Map':
		x, y, location = re.search("<location x=\"(.*?)\" y=\"(.*?)\".*label=\"(.*?)\".*", msg['OriContent']).group(1,2,3)
		if location is None:
			reply_content = r"位置: 纬度->" + x.__str__() + " 经度->" + y.__str__()
		else:
			reply_content = r"位置: " + location
			if msg['Type'] == 'Note':
				reply_content = r"通知"
			elif msg['Type'] == 'Sharing':
				reply_content = r"分享"
			elif msg['Type'] == 'Recording':
				reply_content = r"语音"
			elif msg['Type'] == 'Attachment':
				reply_content = r"文件: " + msg['FileName']
			elif msg['Type'] == 'Video':
				reply_content = r"视频: " + msg['FileName']
			else:
				reply_content = r"消息"

	friend = itchat.search_friends(userName= msg['FromUserName'])
	itchat.send(r"Friend:%s -- %s"  r"Time:%s " r" Message:%s" % (friend['NickName'], friend['RemarkName'], time.ctime(), reply_content),toUserName='filehelper')
	itchat.send(r"亲爱的%s， 万分抱歉，小图现在正忙没有第三只手抓手机！请耐心稍等片刻，	谢谢！" % (friend['NickName']),toUserName=msg['FromUserName'])
itchat.auto_login()
itchat.run()