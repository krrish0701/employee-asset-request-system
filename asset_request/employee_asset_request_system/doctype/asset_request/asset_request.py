import frappe
from frappe.utils import nowdate
from frappe.model.document import Document

class AssetRequest(Document):

    def validate(self):

        total = 0

        for item in self.items:

            if item.quantity <= 0:
                frappe.throw("Quantity must be greater than 0")

            item.amount = item.quantity * item.estimated_price
            total += item.amount

        self.total_estimated_cost = total

        if self.total_estimated_cost > 50000:
            frappe.throw("Total estimated cost cannot exceed ₹50,000")

def on_submit(self):

    if self.status == "Approved":

        for item in self.items:

            asset = frappe.new_doc("Asset")
            asset.asset_name = item.item_name
            asset.asset_category = "Electronic Equipment"
            asset.location = "Main Office"
            asset.insert(ignore_permissions=True)