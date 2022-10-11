import frappe

def validate(doc, method):
    account_value = frappe.db.get_single_value('Saraswati Freight Setting', 'account')
    freight_list =  [d.account_head for d in doc.taxes]
    if doc.freight_charges_custom:
        if account_value not in freight_list:
            doc.append("taxes", {
                "idx":"1",
                "charge_type": "Actual",
                "account_head": frappe.db.get_single_value('Saraswati Freight Setting', 'account'),
                "description":"Freight Charges",
                "cost_center":frappe.db.get_value('Company',doc.company,'cost_center'),
                "account_currency": doc.currency,
                "tax_amount":doc.freight_charges_custom,
                "base_tax_amount":doc.freight_charges_custom,
                "total":doc.total+ doc.freight_charges_custom,
                "base_total":doc.total+ doc.freight_charges_custom
            })
            
            for taxes in doc.taxes:
                if taxes.description in ["Output SGST-9%","Output CGST-9%","Output IGST-18%"]:
                    taxes.idx = taxes.idx + 1  
                    taxes.charge_type = "On Previous Row Total"
                    taxes.row_id = "1"
                    tax_total_final_value = (doc.freight_charges_custom * taxes.rate)/100
                    # frappe.msgprint(str(tax_total_final_value))
                    taxes.tax_amount = tax_total_final_value + (doc.total*taxes.rate)/100
                    taxes.base_tax_amount = tax_total_final_value + (doc.total*taxes.rate)/100
                    taxes.total = tax_total_final_value + (doc.total*taxes.rate)/100 + doc.total
                    taxes.base_total = tax_total_final_value + (doc.total*taxes.rate)/100 + doc.total
           
        
        else:
            for tax in doc.taxes:
                # if tax.description == "Freight And Forwarding Charges":
                if tax.account_head == account_value:
                    tax.tax_amount = doc.freight_charges_custom
                    tax.base_tax_amount = doc.freight_charges_custom
                    tax.total = doc.total
                    tax.base_total = doc.total
                
    if account_value in freight_list and not doc.freight_charges_custom:
        for tax in doc.taxes:
                # if tax.description == "Freight And Forwarding Charges":
                if tax.account_head == account_value:
                    tax.tax_amount = 0
                    tax.base_tax_amount = 0
                    tax.total = doc.total
                    tax.base_total = doc.total

    doc.calculate_taxes_and_totals()

    frappe.db.set_value("Payment Schedule",doc.name,'payment_amount',doc.rounded_total)
    frappe.db.set_value("Payment Schedule",doc.name,'base_payment_amount',doc.rounded_total)
    frappe.db.set_value("Payment Schedule",doc.name,'outstanding',doc.rounded_total)