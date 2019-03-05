import random
import time

url_paths = [
    "class/128.html",
    "class/131.html",
    "class/168.html",
    "class/179.html",
    "learn/821",
    "source/list",
    "class/156.html",
    "class/130.html",
    "class/147.html"
]

ip_list = [128,192,127,26,47,36,187,98,33,27,124,34,147,183,74,72]


http_referer= [
    "https://www.baidu.com/s?wd={qurry}",
    "https://www.sogou.com/web?query={qurry}",
    "https://cn.bing.com/search?q={qurry}",
    "https://search.yahoo.com/search?p={qurry}"
]

search_key = [
    "spark hadoop实战",
    "hadoop 基础",
    "Strom实战",
    "大数据面试",
    "spark streaming 实战"
]


status_code = ["500","200","404"]



def sample_url():
    return random.sample(url_paths, 1)[0]


def sample_ip():
    slices = random.sample(ip_list,4)
    return ".".join(str(elem) for elem in slices)

def sample_referer():
   
    if random.uniform(0, 1) > 0.2:
        return "-"

    http = random.sample(http_referer,1)
    key = random.sample(search_key,1)

    return http[0].format(qurry=key[0])

def sample_status_code():
    return random.sample(status_code,1)[0]


def generator_log (count = 10):
    time_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    
    f = open("E:\opt\data\log.txt","a+")
    
    while count >= 1:
        qurry_log = "{ip}\t{localtime}\t\"GET /{url} HTTP/1.1\"\t{status_code}\t{referer}".format(url=sample_url(),ip=sample_ip(),referer=sample_referer(),status_code=sample_status_code(),localtime=time_str)
        #print(qurry_log)
        f.write(qurry_log + "\n")
        count = count - 1

if __name__ == '__main__':
    generator_log(100)