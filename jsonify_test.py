#-*-encoding: utf-8 -*-

import timeit
import json
from flask import Flask, jsonify, Response
app = Flask(__name__)


test_data_item = {
    "alert_type": "wrapper线路不合理,1个月内有点击量大于10,两个月没有订单",
    "ordernum": "0",
    "create_time": "2015-01-23 10:46:19.303311+08",
    "wrapperid": "qb2c_zkbf3",
    "id": "55498",
    "provinces": "",
    "sourceurl": "5370000",
    "area": "KA-华东",
    "sname": "汤琪珉",
    "price": "1427",
    "wrappername": "春秋旅游（乐游假期）",
    "traffic": "",
    "cities": "白山",
    "tuanqi": "",
    "day": "3",
    "dpv": "11",
    "samenum": "",
    "countries": "中国",
    "tuanqi_price": "",
    "pay_way": "1",
    "title": "滑雪温泉3人套餐 长白山万达套房假日酒店3天2晚自由行+2天完美滑雪+汉拿山温泉+免费接送飞机+酒店自助早餐",
    "departure": "null",
    "route_id": "8040715",
    "tts_enid": "2086035198"
}

datas = []

@app.route("/")
def hello():
    # result = timeit.repeat(stmt="jsonify(ret=1, data=datas)", setup="from flask import jsonify; from __main__ import datas", repeat=100, number=100)
    # result = timeit.repeat(stmt="Response(json.dumps(datas), mimetype='application/json')", setup="import json;from flask import Response; from __main__ import datas", repeat=100, number=100)
    _result = timeit.repeat(stmt="Response(json.dumps(datas), mimetype='application/json')", setup="import json;from flask import Response; from __main__ import datas", repeat=100, number=100)
    all_avgs = handle_avg(stmt="jsonify(ret=1, data=datas)", setup="from flask import jsonify; from __main__ import datas", repeat=100, number=100)

    result = []

    avg1 = handle_avg(stmt="jsonify(ret=1, data=datas)", setup="from flask import jsonify; from __main__ import datas", repeat=100, number=100)
    result.append({"name": "jsonify", "avg": avg1})

    avg1 = handle_avg(stmt="Response(json.dumps(datas), mimetype='application/json')", setup="import json;from flask import Response; from __main__ import datas", repeat=100, number=100)
    result.append({"name": "json dumps Response", "avg": avg1})
   
    avg1 = handle_avg(stmt="json.dumps(datas)", setup="import json;from flask import Response; from __main__ import datas", repeat=100, number=100)
    result.append({"name": "json dumps", "avg": avg1})

    return jsonify(ret=1, avg=result)
    # return Response(json.dumps(datas), mimetype="application/json")


def handle_avg(stmt="pass", setup="pass", repeat=10, number=100):
    all_result = []
    for i in [10, 20, 30, 40, 50]:
        _tmp_datas = []
        for j in range(i):
            _tmp_datas.append(test_data_item)
        global datas
        datas = _tmp_datas
        print len(datas)
        _result = timeit.repeat(stmt=stmt, setup=setup, repeat=repeat, number=number)
        avg = sum(_result) / (repeat * number)
        print avg
        all_result.append(avg)
    return all_result


if __name__ == "__main__":
    app.debug = True
    app.run()