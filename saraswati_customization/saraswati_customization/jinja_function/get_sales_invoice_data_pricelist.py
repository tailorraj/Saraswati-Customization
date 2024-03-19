from __future__ import unicode_literals
import frappe
from frappe import _
from functools import reduce

@frappe.whitelist()
def get_sales_invoice_data_pricelist(doc):
    estimate_doc = frappe.get_doc("Sales Invoice",doc.name)
    doc_items = get_grouped_data(estimate_doc.items)
    # html = frappe.render_template("templates/print_estimation_scheme.html",{"doc":estimate_doc, "scheme": doc_scheme})
    html = frappe.render_template("templates/saraswati_sales_invoice_pricelist.html",{"doc":estimate_doc, "items": doc_items})
    return html

@frappe.whitelist()
def get_sales_invoice_data_pricelist_with_letter_head(doc,letter_head,footer,print_settings):
    estimate_doc = frappe.get_doc("Sales Invoice",doc.name)
    doc_items = get_grouped_data(estimate_doc.items)
    print_settings_doc = frappe.get_doc("Print Settings", print_settings)

    # html = frappe.render_template("templates/print_estimation_scheme.html",{"doc":estimate_doc, "scheme": doc_scheme})
    html = frappe.render_template("templates/saraswati_sales_invoice_pricelist_with_letter_head.html",{"doc":estimate_doc, "items": doc_items,  "letter_head": letter_head,"footer":footer,"print_settings":print_settings_doc})
    return html

def get_grouped_data(data_of_dict):
    data_list = []
    def reduce_data(result,data):
        key = data.item_code
        # key = ":".join([data["location"],data["surface_preparation"],data["area"]])
        batch = {
            "batch_no": data.batch_no,
            "qty": data.qty,
        }

        if key in result:
            result[key]["qty"] = result[key]["qty"] + data.qty
            result[key]["amount"] = result[key]["amount"] + data.amount
            result[key]["batch"].append(batch)
        else:
            result[key] = {
                "item_code": data.item_code,
                "description": data.description,
                "product_description":data.product_description,
                "gst_hsn_code": data.gst_hsn_code,
                "qty": data.qty,
                "uom": data.uom,
                "price_list_rate":data.price_list_rate,
                "discount_percentage":data.discount_percentage,
                "rate": data.rate,
                "item_tax_template": data.item_tax_template,
                "amount": data.amount,
                "batch": [batch]
            }
        return result

        # if key in result:
        #     result[key]["data_detail_list"].append(data_to_add)
        # else:
        #     result[key] = {
        #     "location":data.location,
        #     "surface_preparation":data.surface_preparation,
        #     "area":data.area,
        #     "data_detail_list":[data_to_add]
        #     }
        # return result
    data_list = reduce(reduce_data,data_of_dict,{})
    return list(data_list.values())