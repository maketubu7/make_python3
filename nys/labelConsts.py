# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:11
# @Author  : dengwenxing
# @Software: PyCharm

from collections import OrderedDict

vertex_index = OrderedDict()

vertex_index["vertex_person"] = 0
vertex_index["vertex_phonenumber"] = 10000000

vertex_drop = OrderedDict()

vertex_drop["vertex_person"] = "sfzh"
vertex_drop["vertex_phonenumber"] = "phone"

vertex_table_info = OrderedDict()

vertex_table_info["vertex_person"] = ["sfzh","xm","gj","address"]
vertex_table_info["vertex_phonenumber"] = ["phone","province","city"]


edge_table_info = OrderedDict()
edge_table_info["edge_phone_smz_person"] = ["sfzh","phone","start_time","end_time"]


edge_map_info = OrderedDict()
edge_map_info["edge_phone_smz_person"] = ("vertex_person","vertex_phonenumber")

edge_drop = OrderedDict()
edge_drop["edge_phone_smz_person"] = ["sfzh","phone"]

