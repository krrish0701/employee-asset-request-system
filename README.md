# Employee Asset Request System

The **Employee Asset Request System** is a custom application built using the **Frappe Framework** that allows employees to request company assets such as laptops, monitors, keyboards, etc.

Managers can review these requests and approve or reject them through a workflow process. The system also includes automatic calculations, validation rules, inventory checking, reporting, and automatic asset creation after approval.

---

## Features

- Employees can create asset requests with multiple items
- Automatic calculation of item amount and total estimated cost
- Employee information auto-fetch (department)
- Validation rules:
  - Quantity must be greater than 0
  - Total estimated cost cannot exceed ₹50,000
- Approval workflow (Draft → Pending Approval → Approved / Rejected)
- Inventory check for requested items
- Summary report with filters (Date, Employee, Status)
- Automatic asset creation when request is approved

---

## Installation

Install the app using the **bench CLI**:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app https://github.com/krrish0701/employee-asset-request-system
bench --site your-site-name install-app asset_request
bench migrate
bench start