Sustainable Food Platform
Overview
Sustainable Food Platform is a web application designed to connect consumers with farmers, processors, and distributors in the food supply chain. It enables consumers to order products directly from various stakeholders, choose payment methods, and track their orders. The platform promotes sustainable food sourcing and encourages direct engagement with local food producers.

Features

User Registration and Login: Users can create accounts, log in, and manage their profiles.
Product Ordering: Consumers can browse products from farmers, processors, and distributors, and place orders.
Order Tracking: Users can view the status of their orders and track deliveries.
Multiple Payment Methods: Consumers can pay using M-Pesa or cash upon delivery.
Consumer Dashboard: A personalized dashboard where users can manage their profile, view past orders, and track ongoing orders.
Sustainability Focus: The platform encourages local sourcing and direct engagement with food producers.
Models
Farmer: Manages information about the farmers who supply products.
Processor: Manages information about processors who handle the production process.
Distributor: Manages information about distributors who handle product deliveries.
Consumer: Represents the users who place orders.
Product: Stores product information linked to a farmer, processor, or distributor.
Order: Represents an order made by a consumer, including payment method and status tracking.

Setup and Installation
Prerequisites
Python 3.x
Django 4.x
A virtual environment (recommended)

Installation Steps
Clone the repository:

git clone https://github.com/yourusername/sustainable-food-platform.git
Navigate to the project directory:

cd sustainable-food-platform
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

pip install -r requirements.txt
Apply migrations:

python manage.py migrate
Run the development server:

python manage.py runserver
Open the app in your browser at http://127.0.0.1:8000/.

Usage
Register as a consumer to place orders.
Browse through available products from farmers, processors, and distributors.
Select products, choose your preferred payment method, and place your order.
Track your order through the consumer dashboard.

Contact
For any inquiries, please reach us at ngugiann87@gmail.com

