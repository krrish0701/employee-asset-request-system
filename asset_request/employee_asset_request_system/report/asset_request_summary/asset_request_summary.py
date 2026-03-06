import frappe

def execute(filters=None):

    if not filters:
        filters = {}

    columns = [
        {
            "label": "Employee",
            "fieldname": "employee",
            "fieldtype": "Link",
            "options": "Employee",
            "width": 150
        },
        {
            "label": "Item",
            "fieldname": "item_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Quantity",
            "fieldname": "quantity",
            "fieldtype": "Int",
            "width": 100
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 140
        },
        {
            "label": "Status",
            "fieldname": "workflow_state",
            "fieldtype": "Data",
            "width": 120
        },
        {
            "label": "Request Date",
            "fieldname": "request_date",
            "fieldtype": "Date",
            "width": 120
        }
    ]

    conditions = "1=1"

    if filters.get("employee"):
        conditions += " AND ar.employee = %(employee)s"

    if filters.get("status"):
        conditions += " AND ar.workflow_state = %(status)s"

    if filters.get("from_date") and filters.get("to_date"):
        conditions += " AND ar.request_date BETWEEN %(from_date)s AND %(to_date)s"

    data = frappe.db.sql(f"""
        SELECT
            ar.employee,
            ari.item_name,
            ari.quantity,
            ari.amount,
            ar.workflow_state,
            ar.request_date
        FROM
            `tabAsset Request` ar
        LEFT JOIN
            `tabAsset Request Item` ari
        ON
            ar.name = ari.parent
        WHERE
            {conditions}
        ORDER BY
            ar.request_date DESC
    """, filters, as_dict=True)

    return columns, data