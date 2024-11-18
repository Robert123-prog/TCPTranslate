package main

import (
	"fmt"
	"net"
)

func main() {
	RunClient()
}

func RunClient() {
	conn, err := net.Dial("tcp", "localhost:8080")
	if err != nil {
		fmt.Println("Error connecting:", err)
		return
	}
	defer conn.Close()

	_, err = conn.Write([]byte("Hello, server!"))
	if err != nil {
		fmt.Println("Error writing:", err)
		return
	}
}
