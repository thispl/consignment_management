# Copyright (c) 2023, TEAMPRO and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class TrackingStatus(Document):
	pass

	@frappe.whitelist()
	def status_data(self):
		con = frappe.get_value("CON Booking Entry",{'reference_number':self.reference_number},['date','customer_name','customer_contact_number','courier','contains','pieces','actual_weight','origin_location','consigner_name','consigner_phone_number','tat_alert_date','delivered_on','desination_location'])
		data = ''
		data += '<table class="table table-bordered" style="widtd:50%">'
		data += '<tr><td style="padding:1px;border: 1px solid black;" colspan = 4><b><center>Booking & Customer Details</center></b></td></tr>'
		data += '<tr><td style="padding:1px;border: 1px solid black;"><b><center>Booking Date</center></b></td><td style="padding:1px;border: 1px solid black;"><b><center>Customer</center></b></td><td style="padding:1px;border: 1px solid black;"><b><center>Customer Contact Number</center></b></td><td style="padding:1px;border: 1px solid black;"><b><center>Origion/Desination</center></b></td></tr>'
		data += '<tr><td style="padding:1px;border: 1px solid black;"><b><center>%s</center></b></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td></tr>'%(con[0]  or '-',con[1]  or '-',con[2] or '-',con[7]+'/'+con[12])
		data += '<tr><td style="padding:1px;border: 1px solid black;" colspan = 4><b><center>Courier Details</center></b></td></tr>'
		data += '<tr><td style="padding:1px;border: 1px solid black;"><b><center>Courier</center></b></td><td style="padding:1px;border: 1px solid black;"><center><b>Contains</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>Pieces</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>Actual Weight</b></center></td></tr>'
		data += '<tr><td style="padding:1px;border: 1px solid black;"><b><center>%s</center></b></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td></tr>'%(con[3]  or '-',con[4] or '-',con[5] or '-',con[6])
		data += '<tr><td style="padding:1px;border: 1px solid black;" colspan = 4><b><center>Delivery Details</center></b></td></tr>'
		data += '<tr><td style="padding:1px;border: 1px solid black;"><b><center>Consigner Name</center></b></td><td style="padding:1px;border: 1px solid black;"><center><b>Consigner Phone Number</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>TAT Alert Date</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>Delivered On</b></center></td></tr>'
		data += '<tr><td style="padding:1px;border: 1px solid black;"><b><center>%s</center></b></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td><td style="padding:1px;border: 1px solid black;"><center><b>%s</b></center></td></tr>'%(con[8]  or '-',con[9]  or '-',con[10]  or '-',con[11]  or '-')
		data += '</table>'
		return data

	@frappe.whitelist()
	def status(self):
		frappe.errprint("HI")
		con = frappe.get_value("CON Booking Entry",{'reference_number':self.reference_number},['status'])
		frappe.errprint(con)
		data = ''
		data += '<table class="table table-bordered" style="widtd:50%">'
		# if con == "Booking":
		# 	data += '<tr><td><b>Booking</b></td><td>Packing</td><td>Intransit</td><td>Delivered</td><tr>'
		# if con == "Packing":
		# 	data += '<tr><td>Booking</td><td><b>Packing</b></td><td>Intransit</td><td>Delivered</td><tr>'
		# if con == "Intransit":
		# 	data += '<tr><td>Booking</td><td>Packing</td><td><b>Intransit</b></td><td>Delivered</td><tr>'
		if con == "Delivered":
			data += '<tr><td>Booking</td><td src="/files/image.png">Packing</td><td width = 100px height = 100px src="/files/image.png">Intransit</td><td width = 100px height = 100px src="/files/image.png"><b>Delivered</b></td><tr>'
		data += '</table>'
		return data

