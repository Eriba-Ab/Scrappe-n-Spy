# Web Scraper Price Monitor

This is a Python script that monitors the price of a product on a website and sends email notifications when the price drops below a desired threshold.

## Prerequisites

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `smtplib` library

## Installation

1. Clone the repository or download the script files.

2. Install the required libraries by running the following command:

   ```shell
   pip install requests beautifulsoup4
## Configuration
1. Create a `config.txt file` in the same directory as the script.

2. Edit the `config.txt` file and provide the following information:

sender_email=your_sender_email@example.com

sender_password=your_sender_email_password

receiver_email=receiver_email@example.com

Replace `your_sender_email@example.com` with your actual sender email 
address and `your_sender_email_password` with the password for that email account. 
Also, provide the email address where you want to receive the notifications in `receiver_email@example.com`.

## Usage
1. Open the script file in a text editor.

2. Update the `product_url` variable with the URL of the product page you want to monitor.

3. Update the `desired_price` variable with the desired price threshold.Save the changes.

4. Run the script using the following command:
     `python script.py`
     
 The script will start monitoring the price of the product. If the price drops below 
 the desired threshold, it will send an email notification to the configured receiver email address.
 
 ## Customization
* You can modify the `USER_AGENT` constant in the script to change the user 
  agent string used in the HTTP requests. This can be useful if you want to mimic 
  a specific browser or device.

* The script uses a `log.txt` file to log messages and errors. You can customize 
  the log file name or location by modifying the `LOG_FILE` constant in the script.

* If you want to monitor a different element on the product page, you can modify the `scrape_product_info` function. 
  Update the `element_tag` parameter to the desired HTML element tag (e.g., 'h1', 'span', 'div').
 
## License
This script is licensed under the MIT License.

Feel free to modify the content of the README.md file according to your needs.

