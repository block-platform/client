from getpass import getpass
import requests

# URL = "http://127.0.0.1:5000/ipfs-hash/%s"
URL = "http://127.0.0.1:8080/ipfs-hash/%s"


def get_info():
    email = input("Email: ")
    password = getpass("Password: ")
    device_id = input("Device ID: ")
    return email, password, device_id


def get_ipfs_hash(email, password, device_id):
    url = URL % device_id
    headers = {'Content-type': 'application/json'}
    response = requests.put(
        url, json={"email": email, "password": password}, headers=headers)

    if response.status_code == 200:
        return response.json()["ipfsHash"]
    else:
        return None


def get_ipfs_data(ipfs_hash):
    params = (
        ('arg', ipfs_hash),
    )

    response = requests.post('https://ipfs.infura.io:5001/api/v0/block/get', params=params)

    return response.text


def main():
    email, password, device_id = get_info()
    ipfs_hash = get_ipfs_hash(email, password, device_id)
    
    if ipfs_hash is None:
        print(f"Error: Client doesn't have access to device - {device_id}")
        return

    print(f"\nIPFS hash returned is: {ipfs_hash}")

    data = get_ipfs_data(ipfs_hash)
    print(f"\nIPFS data returned is: {data}")


if __name__ == '__main__':
    main()
