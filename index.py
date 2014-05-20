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

BUF_SIZE = 262144

#app_root = os.path.dirname(_file_)
#sys.path.insert(0, app_root)
#templates_root = os.path.join(app_root, 'templates')
#render = web.template.render(templates_root)
app = web.application(urls, globals()).wsgifunc()

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
				web.header('Content-Type','application/octet-stream')
				web.header('Content-disposition','attachment; filename=%s.dat' % outputFile)
				while True:
					c = f.read(BUF_SIZE)
					if c:
						yield c
					else:
						break
			except Exception, e:
				yield e
				#yield 'Error when read font file'
			finally:
				if f:
					f.close()
			#return "success"
		#else:
			#return "fail"
		
		#return data["text"]


application = WSGIApplication(app)
