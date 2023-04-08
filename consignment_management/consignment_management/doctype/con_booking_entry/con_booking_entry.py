# Copyright (c) 2023, TEAMPRO and contributors
# For license information, please see license.txt

import frappe
import requests
from frappe.model.document import Document

class CONBookingEntry(Document):
	pass

@frappe.whitelist()
def get_area(pincode):
	url = f"https://api.postalpincode.in/pincode/{pincode}"
	response = requests.get(url)

	if response.status_code == 200:
		data = response.json()
		area_names = []
		area_list = []
		for item in data:
			for post_office in item["PostOffice"]:
				area_name = post_office["Name"]
				frappe.errprint(area_name)
				if frappe.db.exists('Area',{'name1':area_name,"pincode":pincode}):
					frappe.errprint("HI")
				else:
					frappe.errprint("HII")
					area = frappe.new_doc('Area')
					area.name1 = area_name
					area.pincode = pincode
					area.save(ignore_permissions=True)
					frappe.db.commit()
	else:
		frappe.throw(f"Failed to retrieve data from {url}: {response.status_code}")
