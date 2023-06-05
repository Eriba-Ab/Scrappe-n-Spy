import requests
from bs4 import BeautifulSoup
import smtplib

def send_email(product_title, product_link, price):
    # Email configuration
    sender_email = 'your_sender_email@example.com'
    sender_password = 'your_sender_email_password'
    receiver_email = 'receiver_email@example.com'
    
    # Compose email message
    subject = f'Price Drop Alert for {product_title}'
    body = f'The price of {product_title} has reduced to {price}. You can check it out at {product_link}.'
    message = f'Subject: {subject}\n\n{body}'
    
    # Connect to SMTP server and send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)

def scrape_product_price(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    
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

def monitor_price_change(url, desired_price):
    while True:
        try:
            product_title, current_price = scrape_product_price(url)
            print(f'Current price of {product_title}: {current_price}')
            
            if current_price <= desired_price:
                send_email(product_title, url, current_price)
                break
            
            # Sleep for some time (e.g., 1 hour) before checking again
            time.sleep(3600)
        
        except Exception as e:
            print('An error occurred:', str(e))
            break

# Example usage
product_url = 'https://www.example.com/product-url'
desired_price = 50.00

monitor_price_change(product_url, desired_price)