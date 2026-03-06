# Employee Asset Request System

## Overview

The **Employee Asset Request System** is a custom application built using the **Frappe Framework**.  
It allows employees to submit requests for company assets such as laptops, monitors, keyboards, and other equipment.

Managers can review these requests and approve or reject them through a workflow process. The system also includes validations, automatic calculations, inventory checking, reporting, and automatic asset creation after approval.

---

# Features

- Employees can submit asset requests with multiple items
- Automatic calculation of item amount and total estimated cost
- Auto-fetch employee department
- Validation rules:
  - Quantity must be greater than 0
  - Total estimated cost cannot exceed ₹50,000
- Workflow approval process:
  
  Draft → Pending Approval → Approved / Rejected

- Inventory availability checking
- Summary report with filters
- Automatic asset creation after approval (bonus feature)

---

# Installation

Follow the steps below to install the application.

First of all create a user
sudo adduser username && sudo usermod -aG sudo username
Switch to the user
su - username
And follow the commands below line-by-line


Frappe ERPNext Installation Guide

1. Prerequisites
Operating System: Updated Ubuntu 22.04
User: A user with sudo privileges
Software Requirements:
Python 3.10+
Node.js 18
Hardware Requirements:
4GB RAM
40GB Hard Disk

2. Steps for Installation
Step 1: Update the system and upgrade the packages
sudo apt-get update && sudo apt upgrade -y

Step 2: Install GIT
sudo apt-get install git -y

Step 3: Install Python
sudo apt-get install python3-dev python3.10-dev python3-setuptools python3-pip python3-distutils -y

Step 4: Install Python Virtual Environment
A virtual environment helps in managing the dependencies for one software at one place, without having to interfere with other sections in the computer or server in which the software is running.
sudo apt-get install python3.10-venv -y

Step 5: Install MariaDB
sudo apt-get install software-properties-common
sudo apt install mariadb-server mariadb-client -y
sudo mysql_secure_installation

Follow the prompts during mysql_secure_installation:
Enter current password for root (enter for none): PRESS ENTER
Switch to unix_socket authentication: Y
Change the root password: Y
Remove anonymous users: Y
Disallow root login remotely: Y
Remove test database and access to it: Y
Reload privilege tables: Y
Step 6: Add MariaDB Configuration
sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf

Add the following lines:
[mysqld]
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci

[mysql]
default-character-set = utf8mb4

Restart MariaDB:
sudo service mysql restart

Step 7: Install Redis
sudo apt-get install redis-server -y

Step 8: Install Curl
sudo apt-get install redis-server -y


Step 9: Install Node.js
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.profile
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \ . "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \ . "$NVM_DIR/bash_completion"  
nvm install 18

Step 10: Install Yarn
sudo apt-get install npm -y
sudo npm install -g yarn

Step 11: Install wkhtmltopdf
sudo apt-get install xvfb libfontconfig wkhtmltopdf -y

Step 12: Install Frappe Bench
sudo -H pip3 install frappe-bench

Initialize Frappe Bench:
bench init frappe-bench2 --frappe-path https://github.com/sigzen-fork/frappe.git --version version-15

Create a new site:

Go to the frappe bench path and run the command to create the new site:
bench new-site <sitename>

Step 13: Get ERPNext
bench get-app erpnext --branch version-15


Installation Complete
bench -–site <sitename> install-app <app_name>
