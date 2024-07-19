# UAS Pemrograman Sisi Server
Seto Aryotomo (A11.2021.13747 / A11.4601)
----------

## Installation


Clone repository

    git clone https://github.com/setoaryotomo/backend-shopify-like-application.git

Menjalankan perintah berikut untuk build image dan run container

    docker-compose up -d --build

Menjalankan perintah berikut untuk migrasi basis data

    docker-compose exec django python manage.py makemigrations 
    docker-compose exec django python manage.py migrate

Untuk mengimport dummy data jalankan perintah berikut

    docker-compose exec django python importer.py

    
----------
## Endopoint

Customer
- [GET] All Customers (customers.json)
- [GET] Single Customers (customers/{id_cust}.json)
- [GET] Search Customer (customers/search.json) params query : first name, last name, email
- [GET] Count Customers (customers/count.json)
- [POST] Create Customer (customers.json)
- [PUT] Update Customer (customers/{id_cust}.json)
- [DELETE] Customer (customers/{id_cust}.json)

Customer Address
- [GET] All Address (customers.json)
- [GET] Single Address (customers/{id_cust}.json)
- [POST] Add Address (customers/{id_cust}/addresses.json)
- [PUT] Set Default Address (customers/{id_cust}/addresses/{id_addr}/default.json)
- [PUT] Update Address (customers/{id_cust}/addresses/{id_addr}.json)
- [DELETE] Address (customers/{id_cust}/addresses/{id_addr}.json)

PriceRule
- [GET] All PriceRule (price_rules.json)
- [GET] Single PriceRule (price_rules/{id}.json)
- [GET] Count PriceRule (price_rules.json)
- [POST] Create PriceRule (price_rules.json)
- [PUT] Update PriceRule (price_rules/{id}.json)
- [DELETE] Delete PriceRule (price_rules/{id}.json)
