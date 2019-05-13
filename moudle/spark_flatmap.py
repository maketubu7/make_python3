
def same_jail_fjh(data):
    ret = []
    jsbhdata,rows = data
    jsbh,fjh = jsbhdata
    rows = list(rows)
    if len(rows)>1:            
        for index,row in enumerate(rows):
            for i in range(index+1,len(rows)):
                sfzh1 = row[0] if row[0]> rows[i][0] else row[0]
                sfzh2 = rows[i][0] if row[0] > rows[i][0] else row[0]
                start1,start2 = row[1],rows[i][1]
                end1,end2 = row[2],rows[i][2]               
                max_start_time = start1 if start1>start2 else start2
                min_end_time = 0                
                if end1!=0 and end2!=0:
                    min_end_time = end1 if end1<end2 else end2
                    if min_end_time-max_start_time>=0:
                        ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
                        
                elif end1==0 and end2==0:
                    ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
                else:
                    min_end_time = end1 if end1>end2 else end2
                    if min_end_time-max_start_time>=0:
                        ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
    if not ret:
        ret.append(['','','','','0','0'])
    return ret  


def same_jail_fjh_bk2(data):
    ret = []
    jsbhdata,rows = data
    jsbh,fjh = jsbhdata
    rows = list(rows)
    if len(rows)>1:            
        for index,row in enumerate(rows):
            for i in range(index+1,len(rows)):
                sfzh1 = row['sfzh'] if row['sfzh']> rows[i]['sfzh'] else rows[i]['sfzh']
                sfzh2 = rows[i]['sfzh'] if row['sfzh'] > rows[i]['sfzh'] else row['sfzh']
                start1,start2 = row['start_time'],rows[i]['start_time']
                end1,end2 = row['end_time'],rows[i]['end_time']               
                max_start_time = start1 if start1>start2 else start2
                min_end_time = 0                
                if end1!=0 and end2!=0:
                    min_end_time = end1 if end1<end2 else end2
                    if min_end_time-max_start_time>=0:
                        ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
                        
                elif end1==0 and end2==0:
                    ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
                else:
                    min_end_time = end1 if end1>end2 else end2
                    if min_end_time-max_start_time>=0:
                        ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
    if not ret:
        ret.append(['','','','','0','0'])
    return ret  

def same_jail_fjh_bk(data):
    ret = []
    jsbhdata,rows = data
    jsbh,fjh = jsbhdata
    rows = list(rows)
    if len(rows)>1:
        for index,row in enumerate(rows):
            for i in range(index+1,len(rows)):
                
                sfzh1 = row['sfzh'] if row['sfzh'] > rows[i]['sfzh'] else rows[i]['sfzh']
                sfzh2 = row['sfzh'] if row['sfzh'] < rows[i]['sfzh'] else rows[i]['sfzh']
                
                
                print(sfzh1, sfzh2)
                start1,start2 = row['start_time'],rows[i]['start_time']
                end1,end2 = row['end_time'],rows[i]['end_time']               
                max_start_time = start1 if start1>start2 else start2
                min_end_time = 0                
                if end1!=0 and end2!=0:
                    #结束时间较小值
                    min_end_time = end1 if end1<end2 else end2
                    if min_end_time-max_start_time>=0:
                        ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
                        
                elif end1==0 and end2==0:
                    ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
                else:
                    min_end_time = end1 if end1>end2 else end2
                    if min_end_time-max_start_time>=0:
                        ret.append([sfzh1,sfzh2,jsbh,fjh,max_start_time,min_end_time])
    if not ret:
        ret.append(['','','','','0','0'])
    return ret  


if __name__ == '__main__':

    arr = [
        {'sfzh':'110','start_time':1233,'end_time':2345}, 
        {'sfzh':'1800','start_time':1333,'end_time':2045},
        {'sfzh':'190','start_time':1433,'end_time':2145},
        {'sfzh':'170','start_time':1533,'end_time':2245},    
        ]

    data = (('jkf342','1197'),arr)
    res = same_jail_fjh_bk(data)
    res2 = same_jail_fjh_bk2(data)
    print(res)
    print(res2)
