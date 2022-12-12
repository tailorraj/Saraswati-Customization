frappe.ui.form.on('Sales Invoice', {
	refresh(frm) {
		// your code here
	},
	freight_charges_custom: async function(frm){
		if(!frm.doc.freight_charges_custom){
			frm.doc.freight_charges_custom = 0;
		}

		console.log(frm.doc.freight_charges_custom)
		var taxes = frm.doc.taxes
		frm.doc.taxes = []

		var f_charge = ""

		await frappe.db.get_single_value('Saraswati Freight Setting', 'account')
			.then(account => {
				f_charge = account
			})

		var cost_c = ""
		await frappe.db.get_value('Company',frm.doc.company,'cost_center')
			.then(r => {
				cost_c = r.message.cost_center
			})

		var tax = cur_frm.add_child("taxes");
		tax.account_head = f_charge;
		tax.charge_type = "Actual";
		tax.description = "Freight Charges";
		tax.cost_center = cost_c;
		tax.rate = 0;
		tax.account_currency = frm.doc.currency;
		tax.tax_amount = frm.doc.freight_charges_custom;
		tax.base_tax_amount = frm.doc.freight_charges_custom;
		tax.total = frm.doc.total+ frm.doc.freight_charges_custom;
		tax.base_total = frm.doc.total+ frm.doc.freight_charges_custom;

		var total = frm.doc.total+ frm.doc.freight_charges_custom
		var act_tot = total


		for (var i in taxes){
			if (taxes[i].account_head != f_charge){
				var t_tax = (act_tot * taxes[i].rate) / 100;
				total = t_tax + total
				tax = cur_frm.add_child("taxes");
				tax.account_head = taxes[i].account_head;
				tax.charge_type = "On Previous Row Total";
				tax.description = taxes[i].description;
				tax.cost_center = taxes[i].cost_center;
				tax.rate = taxes[i].rate;
				tax.row_id = "1"
				tax.account_currency = taxes[i].account_currency;
				tax.tax_amount = t_tax;
				tax.base_tax_amount = t_tax;
				tax.total = total;
				tax.base_total = total;
			}
		}

		refresh_field('taxes')
	}
})