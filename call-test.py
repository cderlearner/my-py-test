
class SimpleCall:

    def __init__(self, id, name):
        self.id = id
        self.name = name
        print self.id;
        print self.name

    def __call__(self, x):
        print "call"




t = SimpleCall(1, 'wo')
t(1)