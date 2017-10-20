package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"net/url"
	"os"
)

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe("localhost:8000", nil))
}

func handler(w http.ResponseWriter, r *http.Request) {
	originURL := r.URL.Query().Get("url")

	log.Printf("originURL: %s\n", originURL)
	if len(originURL) <= 0 {
		log.Println("originURL length == 0. %s", originURL)
		return
	}

	resp, err := proxyByEnv(originURL)

	//resp, err := proxyByURL(originURL)

	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Println("readall error.", err, body)
		return
	}

	fmt.Println(resp)
	w.Write(body)
}

func proxyByEnv(originURL string) (resp *http.Response, err error) {
	os.Setenv("HTTP_PROXY", "http://127.0.0.1:18080")
	os.Setenv("HTTPS_PROXY", "https://127.0.0.1:18080")

	resp, err = http.Get(originURL)
	if err != nil {
		log.Println("proxyByURL error.", originURL, err)
		return
	}
	return
}

func proxyByURL(originURL string) (resp *http.Response, err error) {
	proxyURL, err := url.Parse("http://127.0.0.1:18080")
	if err != nil {
		fmt.Println("proxyByURL error.", originURL, err)
		return
	}
	myClient := &http.Client{Transport: &http.Transport{Proxy: http.ProxyURL(proxyURL)}}

	return myClient.Get(originURL)
}
