from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, json
from datasync import _file

class Ship_Shore_Members:
    "common base class for ship and shore"
    def __init__(self, dc_id, dc_type, pvt_ip, public_ip):
        self.dc_id = dc_id
        self.dc_type = dc_type
        self.pvt_ip = pvt_ip
        self.public_ip = public_ip

def func_data_sync(host_ip, remote_ip):
	print "hello"
	_file(host_ip, remote_ip)


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        message = '\n'.join([
            'sys_version=%s' % self.sys_version,
            ])
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message)
        return

    def do_POST(self):
        global host_ip
        global remote_ip

        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.end_headers()

        print (post_body)
        dsync = json.loads(post_body)
        print (dsync)

        print dsync["type"]
        print dsync["ship_dc_id"]
        print dsync["ship_dc_type"]
        print dsync["ship_pvt_ip"]
        print dsync["ship_public_ip"]
        print dsync["shore_dc_id"]
        print dsync["shore_dc_type"]
        print dsync["shore_pvt_ip"]
        print dsync["shore_public_ip"]

        ship = Ship_Shore_Members(dsync["ship_dc_id"], dsync["ship_dc_type"], dsync["ship_pvt_ip"], dsync["ship_public_ip"])

        shore = Ship_Shore_Members(dsync["shore_dc_id"], dsync["shore_dc_type"], dsync["shore_pvt_ip"], dsync["shore_public_ip"])
        type = dsync["type"]

        if ship.dc_id == shore.dc_id:
            if type == "ship":
                host_ip = ship.pvt_ip
                remote_ip = shore.pvt_ip
            else:
                host_ip = shore.pvt_ip
                remote_ip = ship.pvt_ip
        else:
            if type == "ship":
                host_ip = ship.public_ip
                remote_ip = shore.public_ip
            else:
                host_ip = shore.public_ip
                remote_ip = ship.public_ip

        print ("\n\n")
        print ("host ip : ", host_ip)
        print ("remote ip : ", remote_ip)

        if (host_ip and remote_ip):
            self.send_response(200, "success")
        else:
            self.send_error(406, "internal error")

	func_data_sync(host_ip, remote_ip)

        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    HTTPServer.allow_reuse_address = True
    server = HTTPServer(('127.0.0.1', 9990), GetHandler)
    print 'Starting server at http://127.0.0.1:9990'
    server.serve_forever()

