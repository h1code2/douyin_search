import json

from flask import Flask, jsonify, request
from main import start_hook
import time, random, requests
from urllib.parse import quote

app = Flask(__name__)
script = start_hook()


@app.route("/")
def index():
    return "/"


@app.route("/search/")
def search():
    action = request.args.get("action")
    if action == "douyin":
        word = request.args.get("word")
        cursor = request.args.get("cursor")
        count = request.args.get("count")
        # response = script.exports.a(word, int(cursor), int(count), 1, 0, "")
        word = quote(word)
        print(word)
        current_timestamp = str(int(time.time() * 1000))
        url = "https://aweme.snssdk.com/aweme/v1/discover/search/?cursor=" + cursor + "&keyword=" + word + "&count=" + count + "&type=1&ts=" + current_timestamp[
                                                                                                                                               :-3] + "&app_type=lite&os_api=23&device_type=HTC%20M8w&device_platform=android&ssmix=a&iid=96273560785&manifest_version_code=242&dpi=480&uuid=990072002918973&version_code=242&app_name=douyin_lite&version_name=2.4.2&openudid=e2246348cbfb50f5&device_id=70181717931&resolution=1080*1776&os_version=6.0&language=zh&device_brand=htc&ac=wifi&update_version_code=2420&aid=2329&channel=tengxun&_rticket=" + current_timestamp + "&as=a111111111111111111111&cp=a000000000000000000000&mas"
        print(url)
        args = script.exports.a(url)
        x_gorgon = args.get("X-Gorgon")
        x_khronos = args.get("X-Khronos")
        print(args)
        response = requests.get(
            url=url,
            headers={
                "Host": "aweme-hl.snssdk.com",
                "Connection": "keep-alive",
                # "Cookie": "odin_tt=a900e5fd7ce1f4c2d49de90e1fb9af468bb3ae1fad94d142d34f42e0087338cfd7fe03b0080a5242e17d62769239142d",
                "Accept-Encoding": "gzip",
                "X-SS-REQ-TICKET": x_khronos + str(random.randint(125, 896)),
                "X-SS-TC": "0",
                "X-SS-RS": "0",
                "User-Agent": "com.ss.android.ugc.aweme.lite/242 (Linux; U; Android 6.0; zh_CN; HTC M8w; Build/MRA58K; Cronet/58.0.2991.0)",
                "X-Khronos": x_khronos,
                "X-Gorgon": x_gorgon,
            }
        )
        user_list = response.json().get("user_list")
        if user_list is None or user_list == []:
            users = []
            print(response.json())
        else:
            users = list()
            for user in user_list:
                current_user = user.get("user_info")
                tmp_d = dict()
                tmp_d["uid"] = current_user.get("uid")
                tmp_d["short_id"] = current_user.get("short_id")
                tmp_d["nickname"] = current_user.get("nickname")
                tmp_d["gender"] = current_user.get("gender")
                tmp_d["signature"] = current_user.get("signature")
                tmp_d["avatar_uri"] = current_user.get("avatar_uri")
                tmp_d["birthday"] = current_user.get("birthday")
                tmp_d["is_verified"] = current_user.get("is_verified")
                tmp_d["following_count"] = current_user.get("following_count")
                tmp_d["follower_count"] = current_user.get("follower_count")
                tmp_d["favoriting_count"] = current_user.get("favoriting_count")
                tmp_d["total_favorited"] = current_user.get("total_favorited")
                tmp_d["unique_id"] = current_user.get("unique_id")
                tmp_d["region"] = current_user.get("region")
                tmp_d["unique_id_modify_time"] = current_user.get("unique_id_modify_time")
                tmp_d["share_qrcode_uri"] = current_user.get("share_qrcode_uri")
                tmp_d["sec_uid"] = current_user.get("sec_uid")
                tmp_d["language"] = current_user.get("language")
                tmp_d["constellation"] = current_user.get("constellation")
                users.append(tmp_d)

        # print(json.dumps(response.json(), indent=4, ensure_ascii=False))
        return jsonify({
            "code": 0,
            "x_g": x_gorgon,
            "x_k": x_khronos,
            "data": users,
            "message": "success"
        })
    else:
        return jsonify({
            "code": 0,
            "data": [],
            "message": "no action"
        })


if __name__ == '__main__':
    app.run()
