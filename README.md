# client
Client Node for the Distributed and Decentralized IoT Platform

## API Contract With Manager Node

- Fetch the IFPS hash for a given device ID

`[PUT] /ifps-hash/{device_id}`

Request body:
```json
{
    "email": "<email>",
    "password": "<password>"
}
```

Response:
- For successfully authenticated user - 200 OK with IFPS hash
```json
{
    "ipfsHash": "<IFPS hash>"
}
```

- For unsuccessfully authenticated user - 401 Unauthorized
