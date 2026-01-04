# Beginer Final Projects

# Starter Code - Import Required Libraries
# ======================================
import requests
import pandas as pd
from datetime import datetime
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry



# Website URL
url = "https://www.citymall.com.mm/citymall/my/c/id05011"



# Request Headers (to behave like a browser)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36",
    "Accept-Encoding": "identity"
}


# Create Session and Retry Strategy
session = requests.Session()

retry = Retry(
    total=5,                      # total retry attempts
    backoff_factor=1,              # delay between retries
    status_forcelist=[429, 500, 502, 503, 504]  # retry on these errors
)

session.mount("https://", HTTPAdapter(max_retries=retry))


# Send HTTP Request
response = session.get(url, headers=headers, timeout=30)

print("Status Response Code:", response.status_code)
print("\n")


# Parse HTML Content
soup = BeautifulSoup(response.text, "html5lib")


# Extract Raw HTML Data
web_data = response.text
# print("Web Data:", web_data)


# Clean and Re-Parse HTML
bso = BeautifulSoup(web_data, "html5lib")
# print(bso)


# Find All Product Containers
main_tags = bso.find_all("div", class_="product-info")
# print(main_tags)


# Extract First Product (for testing)
dummy_tag = main_tags[0]
# print(dummy_tag)
# print("\n")


# Create Lists to Store Extracted Data
product_name_list = []     # store product names
product_price_list = []    # store product prices



def main():
    
    # Loop Through Each Product
    for dummy_tag in main_tags:
        try:
            
            print("\n")
            
            # Extract Product Name
            product_name_tag = dummy_tag.find("a", class_="name")
            product_name = product_name_tag.text.strip()
            print(product_name)
            product_name_list.append(product_name)

            try:
                # Extract Normal Product Price
                product_price_tag = dummy_tag.find("p", class_="product-price mt-1")
                product_price = product_price_tag.text
                product_price = product_price.replace("K", "")
                product_price = product_price.replace(",", "")
                product_price = product_price.replace("s", "")
                product_price = int(product_price)

                print(product_price)
                product_price_list.append(product_price)

            except ValueError:
                # Extract Sale Product Price
                product_price_tag = dummy_tag.find("span", class_="product-sale-price")
                product_price = product_price_tag.text
                product_price = product_price.replace("K", "")
                product_price = product_price.replace(",", "")
                product_price = product_price.replace("s", "")
                product_price = int(product_price)

                print(product_price)
                product_price_list.append(product_price)

        except:
            raise
            break

    # Print Extracted Lists
    #print(product_name_list)
    #print(product_price_list)


    # Convert Data to Dictionary
    name_n_price_dict = {
        "Product Name": product_name_list,
        "Prodcut Price": product_price_list
    }


    # Create DataFrame
    df = pd.DataFrame(name_n_price_dict)


    # Generate Timestamp for File Name
    time_str = datetime.now().strftime("%H-%M-%S")
    #print(time_str)


    # Export Data to Excel
    df.to_excel("Extracted Data " + time_str + ".xlsx",  index=False)

    print("\n")
    print("Completed.")

if __name__ == "__main__":
    main()
