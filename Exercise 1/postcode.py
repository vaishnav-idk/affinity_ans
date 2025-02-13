#as we are dealing with apis on python , we should use the requests package
import json

import requests as req
import re

#using regex patter for finding pincode
pattern=r'\b(\d{6})\b'
address="2nd Phase, 374/B, 80 Feet Rd, Mysore Bank Colony,Banashankari 3rd Stage, Srinivasa Nagar, Bengaluru, Karnataka 560050"
match=re.search(pattern,address)
pincode=match.group(1)
print(pincode)



api_url="https://api.postalpincode.in/pincode/560050"
api_response=req.get(api_url)
data=api_response.json()
if api_response.status_code !=200:
		print("error")
else:

		with open("api_data.json","w") as file:
			json.dump(data,file,indent=4)
			file.close()

postoffices=data[0]["PostOffice"]

for postoffice in postoffices:
	if(postoffice["State"].lower() in address.lower() or
		postoffice["District"].lower() in address.lower() or
		postoffice["Name"].lower() in address.lower()):
			print("valid address for pincode")

#considering the various names that each district and place using a dictonairy
def get_actual_place(address):
	std_address=""
	dict={
		"bengaluru" : "bangalore",
		"mysore bank colony" : "state bank of mysore colony"
	}
	place = re.split(r",\s*|\.\s*", address)
	for i in place:
		i=i.lower()
		if i in dict:
			std_address=std_address+" "+dict[i]
		else:
			std_address=std_address+" "+i

	print(std_address)
get_actual_place(address)