# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import requests, json,urllib,time


f_root_path = 'http://15.6.46.234:8081/inet/query/beginadvancequery?analyseResourceIds=&analyseResourceNames=&appTypeNames=QQ&appTypes=1030001&caseDesc=&caseId=613612&caseName=20200511%E6%89%93%E5%87%BB%E7%BD%91%E7%BB%9C%E9%BB%91%E4%BA%A7%E8%B7%91%E5%88%86%E6%94%AF%E4%BB%98%E5%B9%B3%E5%8F%B0%E6%83%85%E6%8A%A5%E4%B8%93%E6%A1%88&caseTaskId=679274&caseTaskName=20200511%E6%89%93%E5%87%BB%E7%BD%91%E7%BB%9C%E9%BB%91%E4%BA%A7%E8%B7%91%E5%88%86%E6%94%AF%E4%BB%98%E5%B9%B3%E5%8F%B0%E6%83%85%E6%8A%A5%E4%B8%93%E6%A1%88&caseType=0&endTime=1591252708&endTimeStr=2020-06-04+14%3A38%3A28&isQueryCache=1&location=&locationStr=&memberId=&needDelivery=false&paramCode=accountname&paramName=QQ%E5%8F%B7&paramValue={}&priValue=false&remark=&secondParamCode=&secondParamCodeName=&secondParamName=&secondParamValue=&secondQuery=false&sourceCodes=10091063%2C10091012&sourceCodesStr=%E5%A5%BD%E5%8F%8B%E4%BF%A1%E6%81%AF%2C%E7%BE%A4%E8%81%8A&startTime=1588660709&startTimeStr=2020-05-05+14%3A38%3A29&taskId=0&userId=0'

header = {
        'Host': '15.6.46.234:8081',
        'Proxy-Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 FH/1.1.0.0 (553A42F6E74BAAE2)(53C9BE9B6308AABF)',
        'Referer': 'http://15.6.46.234:8081/inet/query/loadingpage',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Cookie': 'JSESSIONID=748D8B64C2BCABA3D2E5F964683BE00F; _last_optime_userid_229140=1591346498245; _icp_userid_229140=613612; _pk_id.193.1fe4=dbb37a52e5c719e0.1583234384.161.1591346502.1591344880.; _pk_ses.193.1fe4=*',
        }


header2 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Cookie':'JSESSIONID=748D8B64C2BCABA3D2E5F964683BE00F; _last_optime_userid_229140=1591346498245; _icp_userid_229140=613612; _pk_id.193.1fe4=dbb37a52e5c719e0.1583234384.161.1591346502.1591344880.; _pk_ses.193.1fe4=*',
        'Host':'15.6.46.234:8081',
        'Proxy-Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 FH/1.1.0.0 (553A42F6E74BAAE2)(53C9BE9B6308AABF)',
        }


header4 = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'max-age=0',
        'Cookie':'JSESSIONID=748D8B64C2BCABA3D2E5F964683BE00F; _last_optime_userid_229140=1591346498245; _icp_userid_229140=613612; _pk_id.193.1fe4=dbb37a52e5c719e0.1583234384.161.1591346502.1591344880.; _pk_ses.193.1fe4=*',
        'Host':'15.6.46.234:8081',
        'Proxy-Connection':'keep-alive',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36 FH/1.1.0.0 (553A42F6E74BAAE2)(53C9BE9B6308AABF)',
        }

friend_url = 'http://15.6.46.234:8081/inet/result/tablepage?opId={}&sourceCode=10091063&pagesize=2000&page=1&type=QUERY&appType=1030001'
m_root_path = 'http://15.6.46.234:8081/inet/query/beginadvancequery?analyseResourceIds=&analyseResourceNames=&appTypeNames=QQ&appTypes=1030001&caseDesc=&caseId=613612&caseName=20200511%E6%89%93%E5%87%BB%E7%BD%91%E7%BB%9C%E9%BB%91%E4%BA%A7%E8%B7%91%E5%88%86%E6%94%AF%E4%BB%98%E5%B9%B3%E5%8F%B0%E6%83%85%E6%8A%A5%E4%B8%93%E6%A1%88&caseTaskId=679274&caseTaskName=20200511%E6%89%93%E5%87%BB%E7%BD%91%E7%BB%9C%E9%BB%91%E4%BA%A7%E8%B7%91%E5%88%86%E6%94%AF%E4%BB%98%E5%B9%B3%E5%8F%B0%E6%83%85%E6%8A%A5%E4%B8%93%E6%A1%88&caseType=0&endTime=1591326969&endTimeStr=2020-06-05+11%3A16%3A09&isQueryCache=1&location=&locationStr=&memberId=&needDelivery=false&paramCode=accountname&paramName=QQ%E5%8F%B7&paramValue={}&priValue=false&remark=&secondParamCode=&secondParamCodeName=&secondParamName=&secondParamValue=&secondQuery=false&sourceCodes=10091063%2C10091012&sourceCodesStr=%E5%A5%BD%E5%8F%8B%E4%BF%A1%E6%81%AF%2C%E7%BE%A4%E8%81%8A&startTime=1588734970&startTimeStr=2020-05-06+11%3A16%3A10&taskId=0&userId=0&_=1591327131419 HTTP/1.1'

def qq_friend():
    all_res = []
    all_error = []
    ids = []
    with open ('D:\\Users\\User\\Desktop\\case_data\\QQ.txt','r') as f:
        lines = f.readlines()
        #print(lines)
        for qq in lines:
            qq = qq.replace('\r\n','').replace('\r','').replace('\n','').strip()
            try:
                url = urllib.parse.unquote(f_root_path,'utf8').format(qq)
                print(url)
                text = requests.get(url,headers=header).text
                if text:
                    id = str(int(json.loads(text)['result']) + 1)
                    ids.append({'qq':qq,'id':id})
            except:
                pass
    time.sleep(20)
    i = 0
    print(ids)           
    for info in ids:
        try:
            qq = info['qq']
            find_f_url = friend_url.format(info['id'])
            f_text = requests.get(find_f_url,headers=header2).text
            f_res = json.loads(f_text)
            qqs = f_res['result']['tableData']['results']
            i += 1
            print("qq_friend 处理到%s个qq %s"%(str(i),qq))
            if qqs:
                for info in qqs:
                    qq1 = info['APPID']
                    qq2 = info['FRIAPPID']
                    all_res.append({'qq1':qq1,'qq2':qq2})
        except:
                print('qq %s 出现异常'%qq)
                all_error.append({'qq':qq})
    
    with open('D:\\Users\\User\\Desktop\\case_data\\qq_friend.txt','w') as f:
        json.dump(all_res,f,ensure_ascii=False)
        
    with open('D:\\Users\\User\\Desktop\\case_data\\qq_friend_error.txt','w') as f:
        json.dump(all_error,f,ensure_ascii=False)
        
        
msg_url = 'http://15.6.46.234:8081/inet/result/groupchatpage?opId={}&startTimeStr=&endTimeStr=&keyWord=&keyAccount=&page=1&pagesize=1000&appType=1030001&type=QUERY&sort=desc&mediaType=00&_=1591328923424'
        
## 参数为groupid
group_member_root = 'http://15.6.46.234:8081/inet/query/beginadvancequery?analyseResourceIds=&analyseResourceNames=&appTypeNames=QQ&appTypes=1030001&caseDesc=&caseId=613612&caseName=20200511%E6%89%93%E5%87%BB%E7%BD%91%E7%BB%9C%E9%BB%91%E4%BA%A7%E8%B7%91%E5%88%86%E6%94%AF%E4%BB%98%E5%B9%B3%E5%8F%B0%E6%83%85%E6%8A%A5%E4%B8%93%E6%A1%88&caseTaskId=679274&caseTaskName=20200511%E6%89%93%E5%87%BB%E7%BD%91%E7%BB%9C%E9%BB%91%E4%BA%A7%E8%B7%91%E5%88%86%E6%94%AF%E4%BB%98%E5%B9%B3%E5%8F%B0%E6%83%85%E6%8A%A5%E4%B8%93%E6%A1%88&caseType=0&endTime=1591337834&endTimeStr=2020-06-05+14%3A17%3A14&isQueryCache=1&location=&locationStr=&memberId=&needDelivery=false&paramCode=groupid&paramName=%E7%BE%A4%E5%8F%B7&paramValue={}&priValue=false&remark=&secondParamCode=&secondParamCodeName=&secondParamName=&secondParamValue=&secondQuery=false&sourceCodes=10091068&sourceCodesStr=%E7%BE%A4%E6%88%90%E5%91%98&startTime=1588745835&startTimeStr=2020-05-06+14%3A17%3A15&taskId=0&userId=0&_=1591339136472'
group_member_detail = 'http://15.6.46.234:8081/inet/result/tablepage?opId={}&sourceCode=10091068&pagesize=3000&page=1&type=QUERY&appType=1030001&_=1591339151454'

def qq_groupids():
    all_res = []
    all_error = []
    ids = []
    with open ('D:\\Users\\User\\Desktop\\case_data\\QQ.txt','r') as f:
        lines = f.readlines()
        for qq in lines:
            qq = qq.replace('\r\n','').replace('\r','').replace('\n','').strip()
            try:
                url = urllib.parse.unquote(m_root_path,'utf8').format(qq)
                text = requests.get(url,headers=header).text
                id = str(int(json.loads(text)['result']) + 2)
                ids.append({'qq':qq,'id':id})
            except:
                pass
    print        
    time.sleep(20)   
    i = 0
    for info in ids:
        try:
            qq = info['qq']
            find_msg_url = urllib.parse.unquote(msg_url,'utf8').format(info['id'])
            f_text = requests.get(find_msg_url,headers=header4).text
            f_res = json.loads(f_text)
            #print(f_res)
            qqs = f_res['result']['results']
            i += 1
            print("qq_groupids 处理到%s个qq %s"%(str(i),qq))
            if qqs:
                for info in qqs:
                    groupid = info['groupId']
                    all_res.append({'qq':qq,'groupid':groupid})
        except:
            print('qq %s 出现异常'%qq)
            all_error.append({'qq':qq})
    
    with open('D:\\Users\\User\\Desktop\\case_data\\qq_group.txt','w') as f:
       json.dump(all_res,f,ensure_ascii=False)
       
    with open('D:\\Users\\User\\Desktop\\case_data\\qq_group_error.txt','w') as f:
        json.dump(all_error,f,ensure_ascii=False)
       
def qq_group_member(groupids):
    all_res = []
    all_error = []
    ids = []
    for groupid in groupids:
        try:
            url = group_member_root.format(groupid)
            text = requests.get(url,headers=header).text
            if text:
                resp_json = json.loads(text)
                id = str(int(json.loads(text)['result']) + 1)
                ids.append({'groupid':groupid,'id':id})
        except:
            pass
        
    i = 0
    time.sleep(20)
    for info in ids:
        try:
            groupid = info['groupid']
            find_member_url = group_member_detail.format(info['id'])
            mem_text = requests.get(find_member_url,headers=header2).text
            mem_res = json.loads(mem_text)
            qqs = mem_res['result']['tableData']['results']
            i += 1
            print("qq_group_member 处理到%s个groupid %s"%(str(i),groupid))
            if qqs:
                for info in qqs:
                    qq = info['APPID']
                    all_res.append({'groupid':groupid,'qq':qq})
        except:
            print('groupid %s 出现异常'%groupid)
            all_error.append({'groupid':groupid})
            
    with open('D:\\Users\\User\\Desktop\\case_data\\qq_group_detail.txt','w') as f:
       json.dump(all_res,f,ensure_ascii=False)
       
    with open('D:\\Users\\User\\Desktop\\case_data\\qq_group_detail_error.txt','w') as f:
        json.dump(all_error,f,ensure_ascii=False)
                
                
def read_json(path):
    with open(path,'r') as f:
        res = json.load(f)
    return res
                
                
if __name__ == '__main__':
    qq_friend()
    #qq_groupids()
    #groupids = set([t['groupid'] for t in read_json('D:\\Users\\User\\Desktop\\case_data\\qq_group.txt')])
    #qq_group_member(groupids)
   
    
    
    
    
       
        
        