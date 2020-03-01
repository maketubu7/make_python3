# -*- coding:utf-8 -*-
# @Time    : 2020/1/2 15:11
# @Author  : dengwenxing
# @Software: PyCharm

from collections import OrderedDict

vertex_index = OrderedDict()
vertex_index["vertex_person"] = 0
vertex_index["vertex_phonenumber"] = 10000000
vertex_index["vertex_airline"] = 20000000
vertex_index["vertex_company"] = 30000000
vertex_index["vertex_trainline"] = 40000000

edge_type = OrderedDict()
edge_type["commonLib"] = ["edge_phone_smz_person","edge_groupcall"]
edge_type["pre_tuili"] = ["edge_person_reserve_airline","edge_person_work_company","edge_person_reserve_trainline"]
edge_type["tuili"] = ["edge_person_withairline_person","edge_person_withtrain_person"]

vertex_drop = OrderedDict()
vertex_drop["vertex_person"] = ["sfzh"]
vertex_drop["vertex_phonenumber"] = ["phone"]
vertex_drop["vertex_airline"] = ["hbh"]
vertex_drop["vertex_company"] = ["companyid"]
vertex_drop["vertex_trainline"] = ["hcbc"]

vertex_table_info = OrderedDict()
vertex_table_info["vertex_person"] = ["sfzh","xm","gj","address"]
vertex_table_info["vertex_phonenumber"] = ["phone","province","city"]
vertex_table_info["vertex_airline"] = ["hbh","sfd","mdd","qfsj","ddsj"]
vertex_table_info["vertex_company"] = ["companyid","companyname","qyxz","qydz","clrq"]
vertex_table_info["vertex_trainline"] = ["hcbc","sfd","mdd","fcsj","dzsj"]

edge_table_info = OrderedDict()
edge_table_info["edge_phone_smz_person"] = ["sfzh","phone","start_time","end_time"]
edge_table_info["edge_person_reserve_airline"] = ["sfzh","hbh"]
edge_table_info["edge_person_reserve_trainline"] = ["sfzh","hcbc"]
edge_table_info["edge_person_work_company"] = ["sfzh","companyid"]
edge_table_info["edge_person_withairline_person"] = ["sfzh1","sfzh2","num"]
edge_table_info["edge_person_withtrain_person"] = ["sfzh1","sfzh2","num"]

edge_map_info = OrderedDict()
edge_map_info["edge_phone_smz_person"] = ("vertex_person","vertex_phonenumber")
edge_map_info["edge_person_reserve_airline"] = ("vertex_person","vertex_airline")
edge_map_info["edge_person_reserve_trainline"] = ("vertex_person","vertex_trainline")
edge_map_info["edge_person_work_company"] = ("vertex_person","vertex_company")
edge_map_info["edge_person_withairline_person"] = ("edge_person_reserve_airline","edge_person_reserve_airline")
edge_map_info["edge_person_withtrain_person"] = ("edge_person_reserve_trainline","edge_person_reserve_trainline")


edge_drop = OrderedDict()
edge_drop["edge_phone_smz_person"] = ["sfzh","phone"]
edge_drop["edge_person_reserve_airline"] = ["sfzh","hbh"]
edge_drop["edge_person_reserve_trainline"] = ["sfzh","hcbc"]
edge_drop["edge_person_work_company"] = ["sfzh","companyid"]
edge_drop["edge_person_withairline_person"] = ["sfzh1","sfzh2"]
edge_drop["edge_person_withtrain_person"] = ["sfzh1","sfzh2"]

if __name__ == '__main__':
    # tablename = "vertex_trainline"
    # res = [ i for i in range(100)]
    # print(vertex_index[tablename])
    # print(res)
    pass
