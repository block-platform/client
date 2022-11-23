import random
import requests
import string
import time

from concurrent.futures import ThreadPoolExecutor

URL = "http://34.193.203.14:8080/iot/ipfs-hash/"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0QGdtYWlsLmNvbSIsImV4cCI6MTY2OTE5OTIyMX0.As3CS6ER-VOoTS1osMdgQdNmGNYXbCrdW4od5DVjk6sTs3REIoOzv9Vz4xjtt12iGGtgrOCjA1gz24aUb2ewew"
API_KEY = "OGqwsyc8u8"


def update_ipfs_hash(device_id):
    while True:
        ipfs_hash = "".join(random.choices(
            string.ascii_letters + string.digits, k=25))
        headers = {'Content-type': 'application/json',
                   'Authorization': f'Bearer {TOKEN}'}
        response = requests.put(URL, json={
            "device_id": device_id, "api_key": API_KEY, "ipfs_hash": ipfs_hash}, headers=headers)

        if response.status_code != 200:
            print("Error updating IPFS hash: ", response.status_code)
            print(response.text)

        time.sleep(30)


def main():
    print("Starting threads...")

    with ThreadPoolExecutor(100) as executor:
        for i in range(100):
            executor.submit(update_ipfs_hash, f"dev-{i}")


if __name__ == "__main__":
    main()
