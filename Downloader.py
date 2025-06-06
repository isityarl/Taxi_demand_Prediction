import os
import requests
from bs4 import BeautifulSoup

# URL of the TLC data page
url = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

# Create a folder to store the files
os.makedirs("yellow_taxi_data", exist_ok=True)

# Get the webpage content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find all links to parquet files containing "yellow"
links = soup.find_all('a', href=True)
yellow_links = [link['href'] for link in links if 'yellow_tripdata' in link['href'] and link['href'].endswith('.parquet')]

# Download each yellow taxi parquet file
for link in yellow_links:
    file_name = link.split('/')[-1]
    file_path = os.path.join("yellow_taxi_data", file_name)
    print(f"Downloading {file_name}...")
    with requests.get(link, stream=True) as r:
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f"{file_name} downloaded.")

print("All yellow taxi files downloaded!")
