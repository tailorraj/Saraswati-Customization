from . import __version__ as app_version

app_name = "saraswati_customization"
app_title = "Saraswati Customization"
app_publisher = "Raaj tailor"
app_description = "Private Customization"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "tailorraj111@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/saraswati_customization/css/saraswati_customization.css"
# app_include_js = "/assets/saraswati_customization/js/saraswati_customization.js"

# include js, css files in header of web template
# web_include_css = "/assets/saraswati_customization/css/saraswati_customization.css"
# web_include_js = "/assets/saraswati_customization/js/saraswati_customization.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "saraswati_customization/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {
	"Sales Order" : "custom_script/sales_order.js",
	"Sales Invoice": "custom_script/sales_invoice.js"
	}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "saraswati_customization.install.before_install"
# after_install = "saraswati_customization.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "saraswati_customization.uninstall.before_uninstall"
# after_uninstall = "saraswati_customization.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "saraswati_customization.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Sales Order": {
		# "validate": "saraswati_customization.saraswati_customization.doctype_triggers.sales_order.validate"
	}
}

# jenv = {
# 		"methods": {["get_sales_invoice_data:saraswati_customization.saraswati_customization.jinja_function.get_sales_invoice_data.get_sales_invoice_data"]},

# 		"methods": ["get_delivery_note_data:saraswati_customization.saraswati_customization.jinja_function.get_delivery_note_data.get_delivery_note_data"]
# }


# jenv = {
#         "methods":
# 		[
# 			"get_sales_invoice_data:saraswati_customization.saraswati_customization.jinja_function.get_sales_invoice_data.get_sales_invoice_data",
# 			"get_sales_invoice_data_pricelist:saraswati_customization.saraswati_customization.jinja_function.get_sales_invoice_data_pricelist.get_sales_invoice_data_pricelist",
# 			"get_delivery_note_data:saraswati_customization.saraswati_customization.jinja_function.get_delivery_note_data.get_delivery_note_data"
# 		]
# }

jinja ={
    "methods":
		[
			"saraswati_customization.saraswati_customization.jinja_function.get_sales_invoice_data.get_sales_invoice_data",
			"saraswati_customization.saraswati_customization.jinja_function.get_sales_invoice_data.get_sales_invoice_data_with_letter_head",
			"saraswati_customization.saraswati_customization.jinja_function.get_sales_invoice_data_pricelist.get_sales_invoice_data_pricelist",
			"saraswati_customization.saraswati_customization.jinja_function.get_delivery_note_data.get_delivery_note_data"
		]
}
# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"saraswati_customization.tasks.all"
#	],
#	"daily": [
#		"saraswati_customization.tasks.daily"
#	],
#	"hourly": [
#		"saraswati_customization.tasks.hourly"
#	],
#	"weekly": [
#		"saraswati_customization.tasks.weekly"
#	]
#	"monthly": [
#		"saraswati_customization.tasks.monthly"
#	]
# }


fixtures = [
	{"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Sales Order-freight_charges_custom","Sales Invoice Item-product_description","Delivery Note Item-product_description"
            ]
        ]
    ]}
]

# Testing
# -------

# before_tests = "saraswati_customization.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "saraswati_customization.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "saraswati_customization.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"saraswati_customization.auth.validate"
# ]

