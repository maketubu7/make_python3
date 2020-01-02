# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:06
# @Author  : dengwenxing
# @Software: PyCharm

import flask, json, logging, subprocess, sys

logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

server = flask.Flask(__name__)

@server.route("/fakerLabel",methods=["get"])
def run():
    pass




if __name__ == '__main__':
    pass