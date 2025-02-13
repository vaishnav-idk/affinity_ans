#as we are dealing with apis on python , we should use the requests package
import requests as req
import json
import re

# import re for regex and json for handling api response

def checK_valid_address(address):
	pattern=r'\b\(d{6}\b'
	match=re.search(pattern,address)
	pincode