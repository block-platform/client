package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"syscall"

	"golang.org/x/term"
)

type IpfsHash struct {
	ipfsHash string
}

func sendRequest(email, password, deviceID string, target interface{}) error {
	client := &http.Client{}
	url := "http://localhost:5000/ipfs-hash/" + deviceID
	fmt.Printf("Sending request to manager node at URL %v", url)
	putBody, _ := json.Marshal(map[string]string{"email": email, "password": password})
	resp, err := http.NewRequest(http.MethodPut, url, bytes.NewBuffer(putBody))
	if err != nil {
		log.Fatalf("Error sending request to manager node: %v", err)
		os.Exit(1)
	}

	respClient, err := client.Do(resp)
	if err != nil {
		log.Fatalf("Error sending request to manager node: %v", err)
		os.Exit(1)
	}

	fmt.Printf("Response from manager node: %v", respClient)

	defer resp.Body.Close()

	return json.NewDecoder(resp.Body).Decode(target)
}

func main() {
	fmt.Println("Starting the client")

	var email string
	var password string
	var deviceID string

	fmt.Println("Enter your email: ")
	fmt.Scanln(&email)

	fmt.Println("Enter your password: ")
	bytePassword, err := term.ReadPassword(int(syscall.Stdin))
	if err != nil {
		log.Fatal(err)
		os.Exit(1)
	}

	password = string(bytePassword)

	fmt.Println("Enter the device ID whose data you want: ")
	fmt.Scanln(&deviceID)

	ipfsHash := IpfsHash{}
	err = sendRequest(email, password, deviceID, &ipfsHash)
	if err != nil {
		log.Fatalf("Error decoding respone from manager node: %v", err)
		os.Exit(1)
	}

	fmt.Println("IPFS hash: ", ipfsHash.ipfsHash)
}
