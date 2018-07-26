
from air import iplib

class IpTest:

    def find(self):
        return iplib.find("172.217.24.35")




test = IpTest()

print test.find()