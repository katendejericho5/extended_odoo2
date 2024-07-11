# Odoo Customization Setup Guide

This guide provides instructions for setting up Odoo, creating a new PostgreSQL database, and running the server. It also includes troubleshooting tips for common issues.

## Prerequisites

- Python 3.x
- PostgreSQL
- Odoo 17 source code

## Step-by-Step Instructions

### 1. Install Odoo Dependencies

#### Install System Dependencies

First, install necessary system packages:

```bash
sudo apt-get update
sudo apt-get install git python3-pip build-essential wget python3-dev python3-venv libpq-dev libxml2-dev libxslt1-dev zlib1g-dev libsasl2-dev libldap2-dev libjpeg-dev libjpeg8-dev liblcms2-dev libblas-dev libatlas-base-dev
```

#### Install PostgreSQL

```bash
sudo apt-get install postgresql
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

### 2. Set Up PostgreSQL

#### Create PostgreSQL User and Database

```bash
sudo -u postgres createuser -s odoo
sudo -u postgres createdb odoo_db -O odoo
```

#### Set PostgreSQL User Password

```bash
sudo -u postgres psql
postgres=# \password odoo
Enter new password: 
postgres=# \q
```

### 3. Set Up Odoo

#### Clone the Odoo Repository

```bash
# git clone https://github.com/odoo/odoo.git --branch 17.0 --depth=1
cd odoo


#### Create and Activate a Virtual Environment

```bash

# python3 -m venv odoo-venv 

source odoo-venv/bin/activate
```

#### Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Running the Odoo Server

#### Start the Odoo Server

```bash
./odoo-bin -c odoo.conf
```

Open your web browser and go to `http://localhost:8081`.

### 6. Managing the Odoo Server

#### Stop the Odoo Server

Press `Ctrl+C` in the terminal where the server is running.

#### Kill Running Odoo Processes

If the server is not stopping properly, you can kill the processes:

```bash
sudo pkill -f odoo
```

#### Restart the Odoo Server

```bash
./odoo-bin -c odoo.conf
```

### Troubleshooting Tips

- **Server Not Starting:** Ensure PostgreSQL is running and that the Odoo configuration file (`odoo.conf`) has the correct database user and password.
- **Port Conflicts:** If Odoo is not starting due to port conflicts, ensure no other services are running on port 8069.

## Conclusion

This guide provides the necessary steps to set up and run Odoo with the custom RFQ module. Follow the instructions carefully, and refer to the troubleshooting tips if you encounter any issues. If you need further assistance, consult the [Odoo documentation](https://www.odoo.com/documentation/17.0/).# extended_odoo2
