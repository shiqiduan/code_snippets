package main

import (
	"log"
	"net/http"

	"fmt"

	"strings"

	"github.com/elazarl/goproxy"
)

func main() {
	proxy := goproxy.NewProxyHttpServer()
	proxy.Verbose = true

	proxy.OnRequest().DoFunc(
		func(r *http.Request, ctx *goproxy.ProxyCtx) (*http.Request, *http.Response) {

			fmt.Println(r)
			fmt.Println(ctx)

			//return r, goproxy.NewResponse(r,
			//	goproxy.ContentTypeText, http.StatusForbidden,
			//	"Don't waste your time!")

			return r, nil
		})

	proxy.OnResponse().DoFunc(
		func(resp *http.Response, ctx *goproxy.ProxyCtx) *http.Response {
			fmt.Println("resp", resp)

			resp.Header.Add("XXXXX", "XXXXX")
			for x, y := range resp.Header {
				fmt.Println(x, y)
			}

			resp.Header.Del("Cxy_all")
			resp.Status = "2000000 OK"
			resp.StatusCode = 600

			resp.Proto = strings.ToLower(resp.Proto)
			fmt.Println("Proto:", resp.Proto, resp.ProtoMajor, resp.ProtoMinor)

			fmt.Println(resp)
			return resp
		})

	fmt.Println("main")
	log.Fatal(http.ListenAndServe(":18080", proxy))
}
