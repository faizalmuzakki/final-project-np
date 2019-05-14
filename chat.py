import sys
import os
import json
import uuid
from Queue import Queue

class Chat:
	def __init__(self):
		self.sessions= {}
		self.session= None
		self.users = {}
		self.users['messi']={ 'nama': 'Lionel Messi', 'negara': 'Argentina', 'password': 'surabaya', 'incoming' : {}, 'outgoing': {}}
		self.users['henderson']={ 'nama': 'Jordan Henderson', 'negara': 'Inggris', 'password': 'surabaya', 'incoming': {}, 'outgoing': {}}
		self.users['lineker']={ 'nama': 'Gary Lineker', 'negara': 'Inggris', 'password': 'surabaya','incoming': {}, 'outgoing':{}}

	def proses(self, data):
		j=data.strip().split(" ")
		try:
			command=j[0]

			if (command=='auth'):
				if(self.session!=None):
					return {'status': 'ERROR', 'message': 'Logout Terlebih Dahulu'}
				username=j[1]
				password=j[2]
				return self.autentikasi_user(username,password)

			if (self.session):
				if (command=='send'):
					sessionid = self.session['tokenid']
					usernameto = j[1]
					message = j[2]
					usernamefrom = self.session['username']
					return self.send_message(sessionid, usernamefrom, usernameto, message)
				elif (command=='read'):
					return self.get_inbox(self.session['username'])
				elif (command=='logout'):
					self.session= None
					return {'status': 'OK', 'message': 'Logout Berhasil'}
				return {'status': 'SESSION', 'message': 'Session Diterima'}
			else:
				return {'status': 'ERROR', 'message': 'Login Terlebih Dahulu'}
			return {'status': 'ERROR', 'message': 'Protocol Tidak Benar'}
			
			# elif (command=='send'):
				# sessionid = j[1]
				# usernameto = j[2]
				# message = j[3]
				# usernamefrom = self.sessions[sessionid]['username']
				# return self.send_message(sessionid, usernamefrom, usernameto, message)
			# else:
			# 	return {'status': 'ERROR', 'message': 'Protocol Tidak Benar'}
		except IndexError:
			return {'status': 'ERROR', 'message': 'Protocol Tidak Benar'}

	def autentikasi_user(self, username, password):
		if (username not in self.users):
			return { 'status': 'ERROR', 'message': 'User Tidak Ada' }
 		if (self.users[username]['password']!= password):
			return { 'status': 'ERROR', 'message': 'Password Salah' }
		tokenid = str(uuid.uuid4())
		self.sessions[tokenid]={ 'username': username, 'userdetail':self.users[username]}
		self.session = {'tokenid':tokenid, 'username': username, 'userdetail':self.users[username]}
		return { 'status': 'OK', 'tokenid': tokenid }

	def get_user(self, username):
		if (username not in self.users):
			return False
		return self.users[username]

	def send_message(self, sessionid, username_from, username_dest, message):
		if (sessionid not in self.sessions):
			return {'status': 'ERROR', 'message': 'Session Tidak Ditemukan'}
		s_fr = self.get_user(username_from)
		s_to = self.get_user(username_dest)

		if (s_fr==False or s_to==False):
			return {'status': 'ERROR', 'message': 'User Tidak Ditemukan'}

		message = { 'msg_from': s_fr['nama'], 'msg_to': s_to['nama'], 'msg': message }
		outqueue_sender = s_fr['outgoing']
		inqueue_receiver = s_to['incoming']
		try:
			outqueue_sender[username_from].put(message)
		except KeyError:
			outqueue_sender[username_from]=Queue()
			outqueue_sender[username_from].put(message)
		try:
			inqueue_receiver[username_from].put(message)
		except KeyError:
			inqueue_receiver[username_from]=Queue()
			inqueue_receiver[username_from].put(message)
		return {'status': 'OK', 'message': 'Message Sent'}

	def get_inbox(self, username):
		s_fr = self.get_user(username)
		incoming = s_fr['incoming']
		msgs={}
		for users in incoming:
			msgs[users]=[]
			while not incoming[users].empty():
				msgs[users].append(s_fr['incoming'][users].get_nowait())

		return {'status': 'OK', 'messages': msgs}


if __name__=="__main__":
	j = Chat()
	print j.proses("auth messi surabaya")
	print j.proses("send lineker halo")
	print j.proses("logout")
	print j.proses("auth lineker surabaya")
	print j.proses("read")
	# print sesi
	#sesi = j.autentikasi_user('messi','surabaya')
	#print sesi
	# tokenid = sesi['tokenid']
	# print j.proses("send {} henderson helloson " . format(tokenid))
	# print j.send_message(123,'messi','henderson','hello son')
	#print j.send_message(tokenid,'henderson','messi','hello si')
	#print j.send_message(tokenid,'lineker','messi','hello si dari lineker')


	# print j.get_inbox('henderson')