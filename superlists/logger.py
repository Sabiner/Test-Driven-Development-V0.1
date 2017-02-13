# -*- coding:utf-8 -*-

import logging
import os

logging.basicConfig(level=logging.DEBUG,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S',
    filename=os.path.join('log.txt'),
    filemode='a')
