import os
import requests
from datetime import datetime


def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("This should be a list")

    # Make filename absolute to avoid NoneType / path issues
    filename = (f"log_{datetime.today().strftime('%Y%m%d')}.txt")

    # Write entries (even if empty)
    with open(filename, "w") as file:
        for entry in data:
            file.write(f"{entry}\n")

    return filename
    
def fetch_data():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        return response.json()
    return{}

if __name__ == "__main__":
    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))

   