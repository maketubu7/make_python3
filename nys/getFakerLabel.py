# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:06
# @Author  : dengwenxing
# @Software: PyCharm

import flask, json, logging, subprocess, sys
from nys import dataCreator
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

server = flask.Flask(__name__)

@server.route("/fakerLabel",methods=["get"])
def run():
    label = flask.request.args.get("label")
    num = int(flask.request.args.get("num"))
    if label.startswith("edge"):
        try:
            dataCreator.get_edge_data(label)
            return json.dumps({'msg':'create %s success'%label,'msg_code':200})
        except:
            return json.dumps({'msg':'fi you want create edges you must create nodes at first'%label,'msg_code':404})
    else:
        dataCreator.get_vertex_data(tablename=label,num=num)
        return json.dumps({'msg': 'create %s success' % label, 'msg_code': 200})


if __name__ == '__main__':
    port = int(sys.argv[1])
    server.config["JSON_AS_ASCII"] = False
    server.run(host='192.168.0.146',port=port,debug=True)