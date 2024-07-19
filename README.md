# UAS Pemrograman Sisi Server
Seto Aryotomo (A11.2021.13747/A11.4601)
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
