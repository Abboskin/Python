import requests
import csv

resources = {
    "posts": "posts.csv",
    "comments": "comments.csv",
    "albums": "albums.csv",
    "photos": "photos.csv",
    "todos": "todos.csv",
    "users": "users.csv"
}

for resource, filename in resources.items():
    url = f"https://jsonplaceholder.typicode.com/{resource}"
    
    response = requests.get(url)
    data = response.json()
    
    with open(filename, mode="wt", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
            
        headers = data[0].keys()
        writer.writerow(headers)
            
        for item in data:
            writer.writerow(item.values())
        
    print(f"Data from {resource} has been written to {filename}")