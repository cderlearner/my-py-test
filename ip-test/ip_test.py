
from air import iplib

class IpTest:

    def find(self, ip):
        return iplib.find(ip)




test = IpTest()

# print test.find("172.217.24.35")
# print test.find("127.0.0.1")
# print test.find("192.168.1.100")

# tmp = test.find("10.13.63.255")
# print tmp["country_code"] != '*'

print test.find("172.217.24.35")
#print test.find("61.135.169.125")
# print test.find("123.125.104.197")
# print test.find("111.111.111.111")
# print test.find("222.222.222.222")
# print test.find("221.222.222.222")
# print test.find("220.222.222.222")
# print test.find("219.222.222.222")
