# -*- coding: UTF-8 -*-

import logging
import time
import sys
import stomp

logging.basicConfig
logging.debug('just test...')


logger = logging.getLogger('activemq')


class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)

    def on_message(self, headers, message):
        print('received a message %s' % message)


# 官方示例的连接代码也落后了，现在分协议版本
conn = stomp.Connection10([('localhost', 61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect()

# 注意，官方示例这样发送消息是有问题的
# conn.send(body='hello,garfield! this is '.join(sys.argv[1:]), destination='/queue/test')
conn.send(body='hello,garfield!{"1":1,"2",2}', destination='/topic/SampleTopic.PyTest')

time.sleep(2)
conn.disconnect()
