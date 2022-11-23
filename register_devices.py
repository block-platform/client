import random
import requests
import time

URL = "http://34.193.203.14:8080/devices"
TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0QGdtYWlsLmNvbSIsImV4cCI6MTY2OTE5OTIyMX0.As3CS6ER-VOoTS1osMdgQdNmGNYXbCrdW4od5DVjk6sTs3REIoOzv9Vz4xjtt12iGGtgrOCjA1gz24aUb2ewew"


def register_device(name, id, owner, region):
    # Send post request to register device with authorization token
    headers = {'Content-type': 'application/json',
               'Authorization': f'Bearer {TOKEN}'}
    response = requests.post(URL, json={
                             "name": name, "id": id, "owner": owner, "region": region}, headers=headers)

    if response.status_code != 200:
        print("Error registering device: ", response.status_code)
        print(response.text)
        return

    # print(f"Response: {response.text}")


def main():
    start = time.time()
    # for i in range(1940, 2940):
    #     register_device("Stress Test Device", f"dev-{i}", "Stress Tester",
    #                     random.choice(["US West", "US East", "US Central"]))
    # end = time.time()

    register_device("Stress Test Device", f"dev-test-7", "Stress Tester",
                    random.choice(["US West", "US East", "US Central"]))
    end = time.time()

    print(f"Time taken: {end - start}")


if __name__ == "__main__":
    main()
