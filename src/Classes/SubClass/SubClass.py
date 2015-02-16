class defaultDict(dict):
    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        if(key in self):
            return dict.__getitem__(self, key)
        else:
        	return self.default

    def get(self, key, *args):
    	if not args:
    		args = (self.default,)
    	return dict.get(self, key, *args)

    def merge(self, other):
    	for key in other:
    		if key not in self:
    			self[key] = other[key]

if __name__ == '__main__':
	'''
	Built-in Dict has a issue. 
	You want solve the problem, 
	when dict doesn't declare variable that you call the variable will throw the "KeyError"
	'''
	print defaultDict
	print type(defaultDict)
	d = defaultDict(default = 5)	#Init
	print d
	print type(d)		# Get Type
	print d.__class__	# Get Class
	print type(d) is d.__class__
	d[1] = 3
	print d
	print d[0]
	d.merge({1:300, 2:400})
	print d
	print "~~~~"
	print d.keys()
	exec "x=5; print x" in d
	print d.keys()
	print d["x"]

	print "-----"
	built_dict = dict()
	built_dict[1] = 3
	print built_dict
	print built_dict[0]
