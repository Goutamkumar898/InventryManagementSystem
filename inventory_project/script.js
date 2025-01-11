// Function to fetch and display product data
document.getElementById('load-products-btn').addEventListener('click', function() {
    fetch('http://127.0.0.1:8000/api/products/')  // Replace with the actual URL of your API endpoint
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#product-table tbody');
            tableBody.innerHTML = ''; // Clear any existing data
            data.forEach(product => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${product.name}</td>
                    <td>${product.description}</td>
                    <td>${product.price}</td>
                    <td>${product.stock_quantity}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error loading products:', error));
});

// Function to fetch and display supplier data
document.getElementById('load-suppliers-btn').addEventListener('click', function() {
    fetch('http://127.0.0.1:8000/api/suppliers/')  // Replace with the actual URL of your API endpoint
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#supplier-table tbody');
            tableBody.innerHTML = ''; // Clear any existing data
            data.forEach(supplier => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${supplier.name}</td>
                    <td>${supplier.email}</td>
                    <td>${supplier.phone}</td>
                    <td>${supplier.address}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error loading suppliers:', error));
});

// Function to fetch and display sale order data
document.getElementById('load-sale-orders-btn').addEventListener('click', function() {
    fetch('http://127.0.0.1:8000/api/sale-orders/')  // Replace with the actual URL of your API endpoint
        .then(response => response.json())
        .then(data => {
            const tableBody = document.querySelector('#sale-order-table tbody');
            tableBody.innerHTML = ''; // Clear any existing data
            data.forEach(order => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${order.product.name}</td>
                    <td>${order.quantity}</td>
                    <td>${order.total_price}</td>
                    <td>${order.status}</td>
                `;
                tableBody.appendChild(row);
            });
        })
        .catch(error => console.error('Error loading sale orders:', error));
});
