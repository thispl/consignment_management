// Copyright (c) 2023, TEAMPRO and contributors
// For license information, please see license.txt

frappe.ui.form.on('Tracking Status', {
	refresh: function(frm) {
		frm.disable_save()
	},
	reference_number(frm){
		frm.call('status_data').then(r => {
			if (r.message) {
				frm.fields_dict.status.$wrapper.empty().append(r.message)
			}
		})
	},
	track_status(frm){
		frm.call('status').then(r => {
			if (r.message) 
			{
			    frm.fields_dict.track.$wrapper.empty().append(r.message)
			}
		})
	}
});
