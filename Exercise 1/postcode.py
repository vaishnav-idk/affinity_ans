#as we are dealing with apis on python , we should use the requests package
from textwrap import indent

import requests as req
import json
import re

# import re for regex and json for handling api response
def pincode_return(address):
	pattern = r'\b\(d{6}\b'
	match = re.search(pattern, address)
	pincode = match.group(0)
	if pincode :
		return pincode
	else:
		return None


def get_actual_place(address):
	std_address=""
	dict={
		"bengaluru": "bangalore",
		"mysore bank colony": "state bank of mysore colony"
	}
	places=re.split(r",\s*|\.\s*", address)
	for i in places:
		i=i.lower()
		if i in dict:
			std_address=std_address+dict[i]
		else:
			std_address=std_address+i
	return std_address


def checK_valid_address(address):
	pincode = pincode_return(address)
	if pincode is None:
		#chekcing if pincode function returned any pincode
		return print("address without pincode ")
	url=f'http://www.postalpincode.in/api/pincode/{pincode}'
	api_response = req.get(url)#storing api response object
	if api_response.status_code == 200:
		data = api_response.json()
		#converting api response to json and writing it into a file
		with open("api_response_data.json", "w") as file:
			json.dump(data, file)
			file.close()
	else:
		return print("api timedout")
	#changing the alternative district and place name to standered names
	low_address=get_actual_place(address)

	#storing all the postoffices returned from api response on a particular pin
	postoffices=data[0]["PostOffices"]
	for postoffice in postoffices:
		if(postoffice["District"].lower() in address.lower()) and postoffice["Name"]:





