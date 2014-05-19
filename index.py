#-*- coding:utf-8 -*-

import web
import json

# def app(environ, start_response):
#    status = '200 OK'
#    headers = [('Content-type', 'text/html')]
#    start_response(status, headers)
#    body=["Welcome to Baidu Cloud!\n"]
#    return body


urls = (
    '/(.*)', 'generate'
)


class generate:        

	from fontTools import subset

	def POST(self, name):
		data = json.loads(web.data())
		#bucket = Bucket('font')
		#return bucket.get_object_contents('test.zip')
		name = "/s/font/fangzheng.TTF"
		data = "--text=我们"
		arg = [name,data]
		subset.main(arg)
		#return bucket.generate_url('test.zip')
		
		return data["text"]

from bae.core.wsgi import WSGIApplication
app = web.application(urls, globals()).wsgifunc()
application = WSGIApplication(app)