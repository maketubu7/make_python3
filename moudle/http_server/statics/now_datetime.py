from datetime import datetime
import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage()

print('''\
<html>
<body>
<p>Generated {0}</p>
</body>
</html>'''.format(datetime.now().strftime("%Y-%m-%d %H:%M:%S")))