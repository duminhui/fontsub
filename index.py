#-*- coding:utf-8 -*-

import web
import json
import sys
#from fontTools import subset

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
	def POST(self, name):
		data = json.loads(web.data())
		name = "/s/font/fangzheng.TTF"
		data = "--text=我们"
		arg = [name,data]
		fontTools.subset.main(arg)
		
		return data["text"]

app = web.application(urls, globals()).wsgifunc()

from bae.core.wsgi import WSGIApplication
application = WSGIApplication(app)
