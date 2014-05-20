if (string.find(lighty.env["uri.path"], "^/$")) then                               
	    lighty.env["uri.path"] = "index.py" 

end
lighty.expire[".jpg"] = "modify 10 years" 
lighty.expire[".swf"] = "modify 10 years" 
lighty.expire[".png"] = "modify 10 years" 
lighty.expire[".gif"] = "modify 10 years" 
lighty.expire[".JPG"] = "modify 10 years" 
lighty.expire[".ico"] = "modify 10 years" 
