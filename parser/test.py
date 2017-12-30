# coding=utf-8
import sys
from bs4 import BeautifulSoup
from collections import defaultdict
import re
import json
import os
import time
from collections import OrderedDict

from multiprocessing import Queue, Process


def pass_data(q):
    while(True):
        q.put("1")
        time.sleep(1)
class parser_for_movie:
    def __init__(self,q):
        self.queue = q
        while(True):
            m = self.queue.get()
            print(m)

q = Queue()
writer = Process(target=pass_data, args=(q,))
writer.start()

reader = Process(target=parser_for_movie, args=(q,))
reader.start()
