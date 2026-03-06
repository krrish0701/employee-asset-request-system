frappe.ui.form.on('Asset Request Item', {
    quantity: function(frm, cdt, cdn) {
        calculate_amount(frm, cdt, cdn);
    },
    estimated_price: function(frm, cdt, cdn) {
        calculate_amount(frm, cdt, cdn);
    }
});

function calculate_amount(frm, cdt, cdn) {
    let row = locals[cdt][cdn];
    row.amount = row.quantity * row.estimated_price;

    frm.refresh_field("items");

    let total = 0;
    frm.doc.items.forEach(function(item){
        total += item.amount;
    });

    frm.set_value("total_estimated_cost", total);
}

frappe.ui.form.on("Asset Request", {
    employee: function(frm) {
        frappe.db.get_value("Employee", frm.doc.employee, "department")
        .then(r => {
            frm.set_value("department", r.message.department);
        });
    }
});

frappe.ui.form.on("Asset Request", {
    refresh(frm) {

        frm.add_custom_button("Check Inventory", function() {

            frm.doc.items.forEach(function(item){

                frappe.call({
                    method: "frappe.client.get_value",
                    args: {
                        doctype: "Bin",
                        filters: { item_code: item.item_name },
                        fieldname: ["actual_qty"]
                    },
                    callback: function(r){
                        frappe.msgprint(item.item_name + " Available Qty: " + r.message.actual_qty);
                    }
                });

            });

        });

    }
});