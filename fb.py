import facebook 
from pprint import pprint
import json


class Facebook:
	def __init__(self):
		self.token="CAAGkDEtWDG0BADZCYZBlbJWDc3p0ckVmmXqvdCSZAO2mgUhlGqmtDgnGZCFQhooPzUMTAsWfu1rLpa0w2UZBlqxS5ov8UTDmPkhSZBwbCT2bofBuyZAkyHZCZCWfsYQm7r4M1wHZAymkZARXfoJqCRYlO49QsbhZCol8tePDMxygCbad7avXy80RYVWU0UHa0EjTTUgToOlWeZA8dZCgZDZD"
		self.graph = facebook.GraphAPI(self.token)
		self.friends_map=self.create_data_of_friends()
		self.message_dump()

	def get_notifications_dump(self):
		notifications=self.graph.get_connections("me","notifications")
		pprint(notifications)

	def create_data_of_friends(self):
		friends = self.graph.get_connections("me", "friends")
		dic={}
		for friend in friends["data"]:
			dic.update({friend["name"]:friend["id"]})
		return dic

	def post_on_wall(self,name,message):
		id=self.friends_map[name]
		self.graph.put_wall_post(message,profile_id=id)
		
	def status_update(self,message):
		self.graph.put_object("me","feed",message=message)

	def get_friends_names(self):
		list_of_names=[]
		for friend in self.friends_map:
			list_of_names.append(friend)
		return list_of_names

	def get_friends_ids(self):
		list_of_ids=[]
		for friend in self.friends_map:
			list_of_ids.append(friends_map[friend])
		return list_of_ids	

	def get_name_from_id(self,id):
		for friend in self.friends_map:
			if friends_map[friend]==id:
				return friend		
		return ""

	def get_id_from_name(self,name):
		for friend in self.friends_map:
			if friend==name:
				return friends_map[friend]		
		return ""

	def get_message_in_format(self,message_dump):
		string=""
		for dump in message_dump:
			#pprint(dump)
			if 'message' in dump:
				string+=dump["from"]["name"]+":" +"\t"+dump["message"]+"\n"
		return string+"\n"	

	def message_dump(self):
		f=open("data.json","r")
		dump=json.loads(f.read())
		data_dump_list=dump['data']
		self.names={}
		for dump in data_dump_list:
			name=dump["to"]['data'][1]["name"]
			message_dump=dump["comments"]["data"]
			result_string=self.get_message_in_format(message_dump)
			self.names.update({name:{"message":result_string,"object_id":dump["id"]}})
	
	def get_messages(self,name):
		return self.names[name]["message"]
	
	

if __name__=="__main__":
	
	fb=Facebook()
	fb.write_messages("Shiladitya Mandal")