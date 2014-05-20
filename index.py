#-*- coding:utf-8 -*-

import web
from bae.core.wsgi import WSGIApplication
import json
import sys
from fontTools import subset

urls = (
    '/(.*)', 'generate'
)

app_root = os.path.dirname(_file_)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

class generate:        
	def POST(self, name):
		data = json.loads(web.data())
		name = "fangzheng.TTF"
		data = "--text=我们"
		arg = [name,data]
		#fontTools.subset.main(arg)
		subset.main(arg)
		
		return data["text"]

app = web.application(urls, globals()).wsgifunc()

application = WSGIApplication(app)
