# InventryManagementSystem
# Inventory Management System

## Overview
The **Inventory Management System** is a web application that helps in managing products, stock levels, suppliers, and sales. It allows users to add, list, update, and delete products, suppliers, and sales orders, along with keeping track of stock movements (incoming and outgoing). The system is built using Django for the backend, MongoDB as the database, and HTML, CSS, JavaScript for the frontend.

## Tech Stack
- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: MongoDB
- **Libraries/Tools**:
  - Django REST Framework
  - MongoEngine (for MongoDB integration with Django)
  - CORS headers (for frontend-backend communication)

## Features
- **Product Management**: Add, update, delete, and list products with details such as name, description, price, and stock quantity.
- **Supplier Management**: Add and list suppliers with details like name, email, phone number, and address.
- **Sale Order Management**: Create, cancel, and complete sale orders with status tracking (Pending/Completed/Cancelled).
- **Stock Movement Tracking**: Track incoming ("In") and outgoing ("Out") stock movements.
- **Stock Level Check**: Check and display the current stock levels of products.
- **Filtering**: Filter products by category and order status.

## Setup Instructions

### 1. Clone the repository
Clone the repository to your local machine:
```bash
git clone https://github.com/yourusername/inventory-management-system.git
cd inventory-management-system
