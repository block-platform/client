import requests
import time

URL = "http://34.193.203.14:8080/policies"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0QGdtYWlsLmNvbSIsImV4cCI6MTY2OTE5OTIyMX0.As3CS6ER-VOoTS1osMdgQdNmGNYXbCrdW4od5DVjk6sTs3REIoOzv9Vz4xjtt12iGGtgrOCjA1gz24aUb2ewew"


def create_policy(device_id, accessing_device_id, accessing_user_id):
    # Send post request to register device with authorization token
    headers = {'Content-type': 'application/json',
               'Authorization': f'Bearer {TOKEN}'}
    response = requests.post(URL, json={
                             "device_id": device_id, "accessing_device_id": [], "accessing_user_id": [accessing_user_id]}, headers=headers)

    if response.status_code != 200:
        print("Error creating policy: ", response.status_code)
        print(response.text)
        return

    print(f"Response: {response.text}")


def main():
    start = time.time()
    create_policy("dev-test-7", "", "test7@gmail.com")
    end = time.time()
    print(f"Time taken: {end - start}")


if __name__ == "__main__":
    main()
