import requests

url = "https://drive.google.com/uc?export=download&id=1lU04U972Jubfr6FwtCvK2-YCi6zGfJQb"
local_filename = "animal_identifier.zip"

response = requests.get(url, stream=True)
with open(local_filename, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print(f"Downloaded {local_filename} from Google Drive!")

