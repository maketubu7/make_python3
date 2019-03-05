#--coding:utf-8--
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class ServerException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

class MyRequestHandler(BaseHTTPRequestHandler):
    '''Handle HTTP requests by returning a fixed 'page'.'''
    # Page to send back.
    Error_Page = """\
        <html>
        <body>
        <h1>Error accessing {path}</h1>
        <p>{msg}</p>
        </body>
        </html>
        """
    # send error content
    def handle_error(self, msg):
        content = self.Error_Page.format(path=self.path, msg=msg)
        self.send_content(content, 404)
    
    # Send actual content.
    def send_content(self, content, status=200):
        self.send_response(status)
        self.send_header("Content-type", "text/html")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        ''' wfile.write 在"text/html"文本协议下 只能写入bytes object 数据 '''
        self.wfile.write(bytes(content, encoding="utf8"))
        # self.wfile.write(content)

    def handle_file(self, full_path):
        values = {
                'date_time'   : self.date_time_string(),
                'client_host' : self.client_address[0],
                'client_port' : self.client_address[1],
                'command'     : self.command,
                'path'        : self.path
                }
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
                # content = str(content, encoding="utf8").format(**values)
                ''' 如果这里不转为str 直接发送到page 则会在返回之后产生异常 但是静态页面不会产生影响 '''
                content = str(content, encoding="utf8")
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)

    def do_GET(self):
        try:
            # Figure out what exactly is being requested.
            full_path = os.path.dirname(os.path.realpath(__file__)) + r"\statics" + self.path.replace('/','\\')
            # It doesn't exist...
            if not os.path.exists(full_path):
                raise ServerException("'{0}' not found".format(self.path))
            # ...it's a file...
            elif os.path.isfile(full_path):
                self.handle_file(full_path)
            # ...it's something we don't handle.
            else:
                raise ServerException("Unknown object '{0}'".format(self.path))
        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)


if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress,MyRequestHandler)
    print('running server...')
    server.serve_forever()
    