# -*- coding: UTF-8 -*-

class Htest:

    def test(self, real_amount):
        real_price = real_amount if real_amount is not None else "您好"
        print real_price

    def test3(self, real_amount):
        if real_amount:
            print "这不是空的"
        if real_amount is not None:
            print "这也不是空的"

    @classmethod
    def test2(cls, real1, **kwargs):
        print real1
        print kwargs['real2']
        print kwargs['real3']


#Htest.test2(1, real2=2, real3=4)

ht=Htest()
ht.test(None)
ht.test3("not null")