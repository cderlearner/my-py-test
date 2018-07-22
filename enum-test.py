# -*- coding: UTF-8 -*-

from enum import Enum

class User(Enum):

    Twoater = 98
    Liangdianshui = 30
    Tom = 12

twoater = User.Twoater
liandianshui = User.Liangdianshui

print twoater == liandianshui, twoater == User.Twoater
print twoater is liandianshui, twoater is User.Twoater