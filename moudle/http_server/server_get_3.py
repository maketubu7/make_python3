#--coding:utf-8--
from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class base_case(object):
    '''Parent for case handlers.'''
    def handle_file(self, handler, full_path):
        try:
            with open(full_path, 'rb') as reader:
                content = reader.read()
            handler.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(full_path, msg)
            handler.handle_error(msg)
    '''Serve index.html page for a directory exists.'''
    def index_path(self, handler):
        return os.path.join(handler.full_path, 'index.html')
    def test(self, handler):
        assert False, 'Not implemented.'
    def act(self, handler):
        assert False, 'Not implemented.'


class ServerException(Exception):
    def __init__(self,msg):
        self.msg=msg
    def __str__(self):
        return self.msg

class case_no_file(base_case):
    '''File or directory does not exist.'''
    def test(self, handler):
        return not os.path.exists(handler.full_path)
    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path))

class case_cgi_file(base_case):
    '''Something runnable.'''
    def test(self, handler):
        return os.path.isfile(handler.full_path) and \
               handler.full_path.endswith('.py')
    def act(self, handler):
        handler.run_cgi(handler.full_path)

class case_existing_file(base_case):
    '''File exists.'''
    def test(self, handler):
        return os.path.isfile(handler.full_path)
    def act(self, handler):
        handler.handle_file(handler.full_path)

class case_directory_index_file(base_case):
    def test(self, handler):
        return os.path.isdir(handler.full_path) and \
               os.path.isfile(self.index_path(handler))
    def act(self, handler):
        handler.handle_file(self.index_path(handler))
class case_directory_no_index_file(base_case):
    '''Serve listing for a directory without an index.html page.'''
    def test(self, handler):
        return os.path.isdir(handler.full_path)
    def act(self, handler):
        handler.list_dir(handler.full_path)

class case_always_fail(base_case):
    '''Base case if nothing else worked.'''
    def test(self, handler):
        return True
    def act(self, handler):
        raise ServerException("Unknown object '{0}'".format(handler.path))

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
    Listing_Page = '''\
        <html>
        <body>
        <ul>
        {0}
        </ul>
        </body>
        </html>
        '''
    Cases = [case_no_file(), case_cgi_file(),case_existing_file(), case_directory_index_file(), case_directory_no_index_file(), case_always_fail()]
    # filepath no index.html
    def list_dir(self, full_path):
        try:
            entries = os.listdir(full_path)

            bullets = ['<li>{0}</li>'.format(e)
                for e in entries if not e.startswith('.')]
            print(bullets)
            page = self.Listing_Page.format('\n'.join(bullets))
            self.send_content(page)
        except OSError as msg:
            msg = "'{0}' cannot be listed: {1}".format(self.path, msg)
            self.handle_error(msg)
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
        content = content.encode('utf8').decode('utf8')
        # print(content)
        ''' bytes 下的中文乱码问题 未解决 '''
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
                ''' 如果这里不转为str 直接发送到page 则会在返回之后产生异常 但是静态页面不会产生影响 后续的异常 '''
                content = str(content, encoding="utf8")
            self.send_content(content)
        except IOError as msg:
            msg = "'{0}' cannot be read: {1}".format(self.path, msg)
            self.handle_error(msg)
    # cgi run
    def run_cgi(self, full_path):
        cmd = "python " + full_path
        child_stdout = os.popen(cmd)
        data = child_stdout.read()
        child_stdout.close()
        self.send_content(data)

    def do_GET(self):
        ''' get '''
        try:
            # Figure out what exactly is being requested.
            self.full_path = os.path.dirname(os.path.realpath(__file__)) + r"\statics" + self.path.replace('/','\\')
            # Figure out how to handle it.
            for case in self.Cases:
                handler = case
                if handler.test(self):
                    handler.act(self)
                    break
        # Handle errors.
        except Exception as msg:
            self.handle_error(msg)

    def do_POST(self):
        ''' post '''
        
        

if __name__ == '__main__':
    serverAddress = ('', 8080)
    server = HTTPServer(serverAddress,MyRequestHandler)
    print('running server...')
    server.serve_forever()