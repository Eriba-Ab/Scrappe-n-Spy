import requests
from bs4 import BeautifulSoup
import smtplib
import time
import os

# Constants
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
CONFIG_FILE = 'config.txt'
LOG_FILE = 'log.txt'

def send_email(product_title, product_link, price):
    # Load email configuration from config file
    sender_email, sender_password, receiver_email = load_email_configuration()

    # Compose email message
    subject = f'Price Drop Alert for {product_title}'
    body = f'The price of {product_title} has reduced to {price}. You can check it out at {product_link}.'
    message = f'Subject: {subject}\n\n{body}'

    try:
        # Connect to SMTP server and send email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)
        log_message(f'Email notification sent for {product_title}')
    except Exception as e:
        log_message(f'Failed to send email notification: {str(e)}')

def scrape_product_price(url):
    headers = {'User-Agent': USER_AGENT}

    try:
        # Send GET request to the product page
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the relevant information (product title, price, etc.)
        product_title = soup.find('h1').text.strip()
        price = soup.find('span', class_='product-price').text.strip()

        # Convert the price to a numerical value
        price = float(price.replace('$', '').replace(',', ''))

        return product_title, price
    except Exception as e:
        log_message(f'Failed to scrape product price: {str(e)}')
        return None, None

def monitor_price_change(url, desired_price):
    while True:
        try:
            product_title, current_price = scrape_product_price(url)
            if product_title and current_price:
                log_message(f'Current price of {product_title}: {current_price}')

                if current_price <= desired_price:
                    send_email(product_title, url, current_price)
                    break

            # Sleep for some time (e.g., 1 hour) before checking again
            time.sleep(3600)
        except KeyboardInterrupt:
            log_message('Monitoring stopped by user')
            break

def load_email_configuration():
    config = {}
    try:
        with open(CONFIG_FILE, 'r') as file:
            lines = file.readlines()
            for line in lines:
                key, value = line.strip().split('=')
                config[key] = value
    except Exception as e:
        log_message(f'Failed to load email configuration: {str(e)}')
    return config.get('sender_email'), config.get('sender_password'), config.get('receiver_email')

def log_message(message):
    with open(LOG_FILE, 'a') as file:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f'{timestamp}: {message}'
        print(log_entry)
        file.write(log_entry + '\n')

#Example usage
#product_url = 'https://www.example.com/product-url'
#desired_price = 50.00

#monitor_price_change(product_url, desired_price)*/
