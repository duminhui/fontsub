#-*- coding:utf-8 -*-

import web
import json
import sys
import os
from fontTools import subset
from bae.core.wsgi import WSGIApplication

urls = (
    '/(.*)', 'generate'
)

#app_root = os.path.dirname(_file_)
#sys.path.insert(0, app_root)
#templates_root = os.path.join(app_root, 'templates')
#render = web.template.render(templates_root)

class generate:        
	def POST(self, name):
		data = json.loads(web.data())
		name = "fangzheng.TTF"
		data = "--text=我们"
		arg = [name,data]
		#fontTools.subset.main(arg)
		outfile = "/tmp/" + name + '_after.ttf'
		subset.main(arg)
		if os.path.isfile(outfile)
			return "success"
		else
			return "fail"
		
		#return data["text"]

app = web.application(urls, globals()).wsgifunc()

application = WSGIApplication(app)
