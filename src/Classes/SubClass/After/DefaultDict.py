class defaultDict(dict):
    def __init__(self, default=None):
        dict.__init__(self)
        self.default = default

    def __getitem__(self, key):
        if(key in self):
            return dict.__getitem__(self, key)
        else:
        	return self.default

if __name__ == '__main__':
	d = defaultDict(default= 3)
	d[1] = 9
	d[5] = 18
	print d
	print d[0]
	print d.keys()
