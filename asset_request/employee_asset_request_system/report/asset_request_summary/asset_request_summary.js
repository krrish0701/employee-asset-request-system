frappe.query_reports["Asset Request Summary"] = {
    "filters": [

        {
            "fieldname": "from_date",
            "label": "From Date",
            "fieldtype": "Date"
        },

        {
            "fieldname": "to_date",
            "label": "To Date",
            "fieldtype": "Date"
        },

        {
            "fieldname": "employee",
            "label": "Employee",
            "fieldtype": "Link",
            "options": "Employee"
        },

        {
            "fieldname": "status",
            "label": "Status",
            "fieldtype": "Select",
            "options": [
                "",
                "Draft",
                "Pending Approval",
                "Approved",
                "Rejected"
            ]
        }

    ]
};