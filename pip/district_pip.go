// 计算点是否在多边形里面， 暴力解决方法
package main

import (
	"fmt"
	"strconv"

	"io/ioutil"

	"encoding/json"
	"strings"

	"time"

	"github.com/JamesMilnerUK/pip-go"
)

type JSONDistrict struct {
	Name           string
	PositionBorder string `json:"position_border"`
	Longitude      string
	Latitude       string
}

type JSONCity struct {
	CityName  string
	Districts []*JSONDistrict
}

func readFile(filename string) ([]*JSONDistrict, error) {
	bytes, err := ioutil.ReadFile(filename)
	if err != nil {
		fmt.Println("ReadFile: ", err.Error())
		return nil, err
	}
	var ret JSONCity
	if err := json.Unmarshal(bytes, &ret); err != nil {
		fmt.Println("Unmarshal: ", err.Error())
		return nil, err
	}
	return ret.Districts, nil
}

func initPolygon(pointPairsRaw string) *pip.Polygon {
	pointPairs := strings.Split(pointPairsRaw, ";")
	points := make([]pip.Point, len(pointPairs), len(pointPairs))
	for _, pair := range pointPairs {
		point := strings.Split(pair, ",")
		if len(point) != 2 {
			continue
		}
		lat, err := strconv.ParseFloat(point[0], 64)
		if err != nil {
			continue
		}
		lng, err := strconv.ParseFloat(point[1], 64)
		if err != nil {
			continue
		}
		p := pip.Point{lat, lng}
		points = append(points, p)
	}
	rectangle := pip.Polygon{
		Points: points,
	}
	return &rectangle
}

func timeoutCheck(tag string, start time.Time) {
	dis := time.Since(start).Nanoseconds() / (1000 * 1000)
	fmt.Println(tag, dis, "ms")
}

func main() {
	ret, err := readFile("beijing_districts.json")

	if err != nil {
		panic(err)
	}

	allRegionMap := make(map[string]*pip.Polygon)

	for _, y := range ret {
		allRegionMap[y.Name] = initPolygon(y.PositionBorder)
	}

	fmt.Println(len(allRegionMap))

	defer timeoutCheck("main", time.Now())

	for i := 0; i < 10; i++ {
		for x, y := range allRegionMap {
			p := pip.Point{X: 116.642715, Y: 40.127111}
			in := pip.PointInPolygon(p, *y)
			fmt.Println(x, p, in)
		}
	}
}
