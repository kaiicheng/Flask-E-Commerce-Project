# Flask-E-Commerce-Project

<img src="Demo.png" width="100%">

Testing demo on Flask:
https://flask-e-commerce-project.ue.r.appspot.com/

Testing demo on MongoDB:
https://mongodb-member-system.ue.r.appspot.com/

Welcome to our E-Commerce website, a modern and feature-rich online shopping platform powered by Python Flask, MongoDB, and hosted on Google Cloud Platform. This README provides an overview of the website, its features, and instructions for deployment.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

Our E-Commerce website offers a wide range of features to enhance the online shopping experience for both customers and administrators. Here are some of the key features:

- **User Authentication**: Secure user registration and login system.
- **Product Catalog**: A comprehensive catalog of products with detailed descriptions and images.
- **Search and Filtering**: Efficient search and filtering options for product discovery.
- **Shopping Cart**: An interactive shopping cart for adding and managing selected items.
- **Checkout and Payment**: Seamless checkout process with multiple payment options.
- **Order Tracking**: Real-time order tracking and history for customers.
- **Admin Dashboard**: A powerful admin dashboard for managing products, orders, and users.
- **Product Reviews**: Customer reviews and ratings for products.
- **Responsive Design**: A mobile-responsive website for a smooth shopping experience on all devices.
- **Security**: Security measures to protect user data and transactions.

## Technologies

Our E-Commerce website is built using the following technologies:

- **Python Flask**: A lightweight web framework for building the backend.
- **MongoDB**: A NoSQL database for storing product and user data.
- **Google Cloud Platform**: Hosting and server infrastructure.
- **HTML/CSS/JavaScript**: Frontend development for the user interface.
- **Bootstrap**: Frontend framework for responsive design.
- **Stripe**: Payment processing integration.
- **Python Libraries**: Various Python libraries and packages for specific functionalities.

## Installation

To run the website locally for development or testing purposes, follow these steps:

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/e-commerce-website.git

# Requirement for hosting on Google Cloud Platform (GCP)

* Create app.yaml file at root directory with below information
```
runtime: python311
```

* Create requirements.txt file
```
pip freeze > requirements.txt
```

# Hosting on Google Cloud Platform (GCP)

* Downlaod Google Cloud SDK

* Open Google Cloud SDK Shell (Run as Administrator)

* Change directory to the folder of project

* Check GCP version
```
gcloud --version
```

* (Optional) Update GCP to the latest version
```
gcloud components update
```

* Login GCP in terminal
```
gcloud auth login
```

* Allow access to GCP

* Set configuration
```
gcloud config set project "GCP ID"
```

* Deploy website application
```
gcloud app deploy
```

* View website application
```
gcloud app browse
```