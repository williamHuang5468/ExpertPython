class abc:
	def hello(x): # No "self"
		print x
	hello = staticmethod(hello)

class ClassMethod:
	def hello(cls, y): #cls get class name.
		print "classMethod", cls, y
	hello = classmethod(hello)

class D(ClassMethod):
	pass

class E(ClassMethod):
	def hello(cls, y):
		print "E.hello() called"
		ClassMethod.hello(y)
	hello = classmethod(hello)

abc.hello("abc")
a = abc()
a.hello("cc")

ClassMethod.hello(1)
c = ClassMethod()
c.hello(1)

D.hello(1)
d = D()
d.hello(1)

E.hello(1)
e = E()
e.hello(1)
