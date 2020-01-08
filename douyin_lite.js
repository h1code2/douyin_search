Java.perform(function () {
    var tt1 = Java.use("com.ss.sys.ces.gg.tt$1");
    tt1.a.implementation = function (s1, m1) {
        console.log(s1);
        console.log(m1);
        var ret = this.a(s1, m1);
        console.log(ret);
        return ret;
    }
});

rpc.exports = {
    "a": function (str1) {
        var ret = {};
        Java.perform(function () {
            var tt1 = Java.use("com.ss.sys.ces.gg.tt$1").$new();

            var url = str1;
            var ArrayList = Java.use("java.util.ArrayList").$new();
            var ObjectJava = Java.use("java.lang.Object");

            var map = Java.use("java.util.HashMap").$new();

            var m1 = ArrayList;
            var m2 = ArrayList;
            var m3 = ArrayList;
            var m4 = ArrayList;
            var m5 = ArrayList;

            m1.add("0");
            m2.add("install_id=96878478736; ttreq=1$43848e43e34b21534a1ca2414ffd601b004aa8d3; d_ticket=63d78f83c089eaf136d74173d3c011d653066; odin_tt=65491b63cd82b2bee5271d4a2388a20c48bdfd6dff90e1c6ddeaccf7890fc7af48083b29f1eddf71f2f8a1806aeb1a3cae6b13a26512ba506191449493737617; msh=YQRjF4WUqts_4g3BlYEPYD8kCjg; sid_guard=7cfef1edc69f83bc1fd54ec3279ad01f%7C1577626550%7C5184000%7CThu%2C+27-Feb-2020+13%3A35%3A50+GMT; uid_tt=4b500edbde752f07e69686631933cb1a; sid_tt=7cfef1edc69f83bc1fd54ec3279ad01f; sessionid=7cfef1edc69f83bc1fd54ec3279ad01f");
            m3.add("gzip");
            m4.add("com.ss.android.ugc.aweme.lite/242 (Linux; U; Android 6.0; zh_CN; HTC M8w; Build/MRA58K; Cronet/58.0.2991.0)");
            m5.add((new Date()).valueOf().toString());

            var mm1 = Java.cast(Java.cast(m1, ArrayList), ObjectJava);
            var mm2 = Java.cast(Java.cast(m2, ArrayList), ObjectJava);
            var mm3 = Java.cast(Java.cast(m3, ArrayList), ObjectJava);
            var mm4 = Java.cast(Java.cast(m4, ArrayList), ObjectJava);
            var mm5 = Java.cast(Java.cast(m5, ArrayList), ObjectJava);

            map.put("x-ss-tc", mm1);
            map.put("cookie", mm2);
            map.put("accept-encoding", mm3);
            map.put("user-agent", mm4);
            map.put("x-ss-req-ticket", mm5);

            var result = tt1.a(url, map);
            ret["X-Gorgon"]=result.get("X-Gorgon").toString();
            ret["X-Khronos"]=result.get("X-Khronos").toString();
        });
        return ret;
    }
};