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
		subset.main(arg)
		outputFile = "/tmp/" + name + ".subset"
		if (os.path.isfile(outputFile)):
			try:
				f = open(outputFile, "rb")
				webpy.header('Content-Type','application/octet-stream')
				webpy.header('Content-disposition','attachment; filename=%s.dat' % file_name)
				while True:
					c = f.read(BUF_SIZE)
					if c:
						yield c
					else:
						break
			except Exception, e:
				print e
				yield 'Error when read font file'
			finally:
				if f:
					f.close()
			#return "success"
		#else:
			#return "fail"
		
		#return data["text"]

app = web.application(urls, globals()).wsgifunc()

application = WSGIApplication(app)
