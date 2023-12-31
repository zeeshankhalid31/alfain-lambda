from . import __version__ as app_version

app_name = "alfain"
app_title = "Alfain"
app_publisher = "alfain"
app_description = "document review management"
app_email = "admin@alfain.co"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/alfain/css/alfain.css"
# app_include_js = "/assets/alfain/js/alfain.js"

# include js, css files in header of web template
# web_include_css = "/assets/alfain/css/alfain.css"
# web_include_js = "/assets/alfain/js/alfain.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "alfain/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
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

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "alfain.utils.jinja_methods",
#	"filters": "alfain.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "alfain.install.before_install"
# after_install = "alfain.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "alfain.uninstall.before_uninstall"
# after_uninstall = "alfain.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "alfain.utils.before_app_install"
# after_app_install = "alfain.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "alfain.utils.before_app_uninstall"
# after_app_uninstall = "alfain.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "alfain.notifications.get_notification_config"

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
#		"alfain.tasks.all"
#	],
#	"daily": [
#		"alfain.tasks.daily"
#	],
#	"hourly": [
#		"alfain.tasks.hourly"
#	],
#	"weekly": [
#		"alfain.tasks.weekly"
#	],
#	"monthly": [
#		"alfain.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "alfain.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "alfain.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "alfain.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["alfain.utils.before_request"]
# after_request = ["alfain.utils.after_request"]

# Job Events
# ----------
# before_job = ["alfain.utils.before_job"]
# after_job = ["alfain.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"alfain.auth.validate"
# ]

# Fixtures export

fixtures = [
    {
        "dt" : "DocType",
        "filters" : {
            "custom": 1
        }
    },
    {
        "dt" : "Custom Field"
    },
    {
        "dt" : "Workflow"
    },
    {
        "dt" : "Workflow State"
    },
    {
        "dt" : "Workflow Action Master"
    },
    {
        "dt":  "Role",
        "filters" : {
            "is_custom": 1
        }
    },
    {
        "dt":  "Role Profile"
    }
    # Not possible to export data form table when its starts with Doc keyword
    #  ,
    # {
    #     "doctype":  "DocPerm",
    #     "filters" : ["parent", "in", "Project,Building,Submittal,Task"]
    # }
]