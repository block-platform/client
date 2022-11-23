import requests
import time

# URL = "http://34.193.203.14:8080/ipfs-hash/%s"
URL = "http://34.193.203.14:8080/ipfs-hash/%s"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0QGdtYWlsLmNvbSIsImV4cCI6MTY2OTE5OTIyMX0.As3CS6ER-VOoTS1osMdgQdNmGNYXbCrdW4od5DVjk6sTs3REIoOzv9Vz4xjtt12iGGtgrOCjA1gz24aUb2ewew"


def get_ipfs_hash(email, password, device_id):
    url = URL % device_id
    print(f"Hitting URL {url}")
    # Send post request to register device with authorization token
    headers = {'Content-type': 'application/json',
               'Authorization': f'Bearer {TOKEN}'}
    response = requests.put(
        url, json={"email": email, "password": password}, headers=headers)

    if response.status_code != 200:
        print("Error getting IPFS hash: ", response.status_code)
        print(response.text)
        return

    print(f"Response: {response.text}")


def main():
    start = time.time()
    get_ipfs_hash("test@gmail.com", "password", "dev-0")
    end = time.time()
    print(f"Time taken: {end - start}")


if __name__ == "__main__":
    main()
