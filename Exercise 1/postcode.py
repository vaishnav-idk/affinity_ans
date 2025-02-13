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



api_url="https://api.postalpincode.in/pincode/110001"
api_response=req.get(api_url)
if api_response.status_code !=200:
		print("error")
else:
		data=api_response.json()
		with open("api_data.json","w") as file:
			json.dump(data,file,indent=4)
			file.close()


