import frappe
from frappe import _

AI_BOT_ROLE = "AI Bot User"


def can_use_ai_bot(user=None):
    user = user or frappe.session.user
    if not user or user == "Guest":
        return False
    return AI_BOT_ROLE in frappe.get_roles(user)


def require_ai_bot_access(user=None):
    if not can_use_ai_bot(user):
        frappe.throw(_("You do not have access to AI Bot. Please contact your administrator."), frappe.PermissionError)


def boot_session(bootinfo):
    bootinfo.ai_bot_allowed = can_use_ai_bot()
    
# import frappe
# from frappe import _

# AI_BOT_ROLE = "AI Bot User"


# def can_use_ai_bot(user=None):
#     user = user or frappe.session.user
#     if not user or user == "Guest":
#         return False
#     return AI_BOT_ROLE in frappe.get_roles(user)


# def require_ai_bot_access(user=None):
#     if not can_use_ai_bot(user):
#         frappe.throw(_("You are not allowed to use the AI chatbot."), frappe.PermissionError)


# @frappe.whitelist()
# def can_access_chatbot():
#     return {"allowed": can_use_ai_bot()}

