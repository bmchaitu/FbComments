#! /usr/bin/env python3.6

import facebook
import json
import datetime
graphAPI = facebook.GraphAPI(access_token)
profile=graphAPI.get_object("me")
result=graphAPI.get_connections(profile['id'],'feed')
posts=result['data']
Bday=datetime.datetime.strptime('31-8-2019','%d-%m-%Y')
for post in posts:
	pdate=datetime.datetime.strptime(post['created_time'],'%Y-%m-%dT%H:%M:%S+0000')
	if (pdate.day == Bday.day and pdate.month == Bday.month):
		graphAPI.put_comment(post['id'],"Thank You")
		print('posted')
