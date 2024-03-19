from __future__ import unicode_literals
import frappe
from frappe import _
from functools import reduce

@frappe.whitelist()
def get_delivery_note_data(doc):
    estimate_doc = frappe.get_doc("Delivery Note",doc.name)
    doc_items = get_grouped_data(estimate_doc.items)
    # html = frappe.render_template("templates/print_estimation_scheme.html",{"doc":estimate_doc, "scheme": doc_scheme})
    html = frappe.render_template("templates/saraswati_delivery_note.html",{"doc":estimate_doc, "items": doc_items})
    return html

@frappe.whitelist()
def get_delivery_note_data_with_letter_head(doc,letter_head,footer):
    estimate_doc = frappe.get_doc("Delivery Note",doc.name)
    doc_items = get_grouped_data(estimate_doc.items)
    # html = frappe.render_template("templates/print_estimation_scheme.html",{"doc":estimate_doc, "scheme": doc_scheme})
    html = frappe.render_template("templates/saraswati_delivery_note_with_letter_head.html",{"doc":estimate_doc, "items": doc_items,  "letter_head": letter_head,"footer":footer})
    return html
def get_grouped_data(data_of_dict):
    data_list = []
    def reduce_data(result,data):
        key = data.item_code
        # key = ":".join([data["location"],data["surface_preparation"],data["area"]])
        batch_data = {
            "batch_no": data.batch_no,
            "qty": data.qty,
        }

        if key in result:
            result[key]["qty"] = result[key]["qty"] + data.qty
            result[key]["amount"] = result[key]["amount"] + data.amount
            result[key]["batch"].append(batch_data)
        else:
            result[key] = {
                "item_code": data.item_code,
                "description": data.description,
                "product_description":data.product_description,
                "gst_hsn_code": data.gst_hsn_code,
                "qty": data.qty,
                "uom": data.uom,
                "rate": data.rate,
                "item_tax_template": data.item_tax_template,
                "amount": data.amount,
                "batch": [batch_data]
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