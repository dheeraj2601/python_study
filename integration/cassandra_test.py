from cassandra.cluster import Cluster
import json
import requests

cluster = Cluster(['192.168.122.1'], port=9042)
session = cluster.connect('adaranetworks_wan')

class Ship_Shore:
        "class for ship or shore information"
	def __init__(self, vnf_id):
		self.dc_id = []
		self.vnf_id = vnf_id
		self.public_ip = []
		self.pvt_ip = []
		self.dc_type = []

	def extract_vnf_info(self):
		row = session.execute("select * from vnf_public_ip_table where vnf_id = %s", [self.vnf_id])
		for user_row in row:
			print "vnf : ", user_row.vnf_id, "   data_center : ", user_row.dc_id, "  public_ip : ",user_row.public_ip
			self.public_ip = user_row.public_ip
			self.dc_id = user_row.dc_id
			self.pvt_ip = user_row.pvt_ip
			
		print type(self.dc_id)

                query = ("SELECT * FROM datacenter_table where datacenter_id = ?")
                prepared = session.prepare(query)
                row = session.execute(prepared.bind([self.dc_id]))

                for user_row in row:
                        print "data_center : ", user_row.datacenter_id, "  datacenter_vendor_type : ",user_row.vendor
                        self.dc_type = user_row.vendor

	def display(self, name):
                print name
		print "dc id : ", self.dc_id
		print "dc type : ", self.dc_type
		print "vnf id : ", self.vnf_id
		print "public ip : ", self.public_ip
		print "private ip : ", self.pvt_ip


def main():
	ship_id = raw_input("enter the ship_vnf_id : ")
	shore_id = raw_input("enter the shore_vnf_id : ")
	ship = Ship_Shore(ship_id)
	shore = Ship_Shore(shore_id)

	ship.extract_vnf_info()
	shore.extract_vnf_info()

	if not ship.public_ip:
		if ship.dc_type == "openstack":
			print ("please provide ship floating ip for openstack with vm id : ", ship.vnf_id)
		if ship.dc_type == "aws":
			print ("please provide ship elastic ip for aws with vm id : ", ship.vnf_id)
		return

	if not shore.public_ip:
		if shore.dc_type == "openstack":
			print ("please provide ship floating ip for openstack with vm id : ", shore.vnf_id)
		if shore.dc_type == "aws":
			print ("please provide ship elastic ip for aws with vm id : ", shore.vnf_id)
		return
		
	print ("\n\n")

	data = {"ship_dc_id":str(ship.dc_id),
		"ship_dc_type":ship.dc_type,
		"ship_pvt_ip":ship.pvt_ip,
		"ship_public_ip":ship.public_ip,
		"shore_dc_id":str(shore.dc_id),
		"shore_dc_type":ship.dc_type,
		"shore_pvt_ip":shore.pvt_ip,
		"shore_public_ip":shore.public_ip}

	header2 = {'Content-type': 'application/json', 'Accept': 'text/plain'}

	# send the event to the ship
	data["type"] = "ship"
	API_ENDPOINT = "http://"+ship.public_ip+":9990/api"
	r_ship = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=header2)

	response_back_ship = r_ship.text
	#response_back_ship = r_ship.json
	print ("response status of ship is ", r_ship.status_code)
	print ("response of ship is ", response_back_ship)


'''
	# send the event to the shore
	data["type"] = "shore"
	API_ENDPOINT = "http://"+shore.public_ip+":8080/api"
	r_shore = requests.post(url=API_ENDPOINT, data=json.dumps(data), headers=header2)

	response_back_shore = r_shore.text
	#response_back = r_shore.json
	print ("response status of shore is ", r_shore.status_code)
	print ("response of shore is ", response_back_shore)
'''

if __name__ == main():
	main()
