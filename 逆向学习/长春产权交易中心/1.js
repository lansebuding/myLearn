var pubPass = "BX1o65CoobwcDP33iQW6ld1OyIPsNzF1"
var projectKey = 'honsan_cloud_ccprec'
var clientKey = 'rtd5q8a5csw4cxyb'
var pubPassNum = []
var uuidCount = 0
setPass(pubPass)

function entrycode(e) {
    for (var t = encodeURI(e), n = [], i = 0, r = "", o = random(16, 32), a = randomStr(o), s = stringChangeASCIINumberArrs(a), l = 0, c = 0, u = 0, h = 0; h < t.length; h++)
        i = t.charCodeAt(h),
        l == pubPassNum.length && (l = 0),
        i += pubPassNum[l],
        l++,
        c == s.length && (c = 0),
        i += s[c],
        c++,
        u += i,
        u > 65535 && (u -= 65535),
        r = i.toString(36),
        r = ("00" + r).substr(-2, 2),
        1 == r.length && (r = "0" + r),
        n.push(r);
    var d = "";
    return d = u.toString(36),
    d = ("0000" + r).substr(-4, 4),
    n.unshift(a),
    n.unshift(o.toString(36)),
    n.unshift(d),
    n.join("")
}

function random(e, t) {
    return void 0 === e && (e = 0),
    void 0 === t && (t = 1e4),
    Math.floor(Math.random() * (t - e) + e)
}

function randomStr(e) {
    for (var t = [], n = 0; n < e; n++)
        t.push(random(0, 35).toString(36));
    return t.join("")
}

function stringChangeASCIINumberArrs(e) {
    for (var t = [], n = 0; n < e.length; n++)
        t.push(e.charCodeAt(n));
    return t
}

function setPass(e) {
    pubPassNum = stringChangeASCIINumberArrs(e)
}

// 返回数据解密
function decryptCode(e) {
    var t = ""
      , n = 0
      , i = ""
      , r = []
      , o = []
      , a = 0
      , s = 0;
    t = e.substr(4, 1),
    n = parseInt(t, 36),
    i = e.substr(5, n),
    r = stringChangeASCIINumberArrs(i),
    t = e.substr(5 + n, e.length - 5 - n);
    for (var l = "", c = 0, u = 0, h = 0; h < t.length / 2; h++)
        l = t.substr(u, 2),
        u += 2,
        c = parseInt(l, 36),
        s == r.length && (s = 0),
        c -= r[s],
        s++,
        a == pubPass.length && (a = 0),
        c -= pubPassNum[a],
        a++,
        l = String.fromCharCode(c),
        o.push(l);
    return t = o.join(""),
    t = decodeURI(t),
    t
}

function uuid(t, n) {
    void 0 === t && (t = 16),
    void 0 === n && (n = !1),
    !n && t < 16 && (console.error("uuid useCase=false 时 len 不能小于 16"),
    t = 16),
    n && t < 12 && (console.error("uuid useCase=true 时 len 不能小于 12"),
    t = 12);
    var i = ((new Date).getTime() + 1e14).toString();
    return i += ("000" + (++uuidCount).toString()).substr(-3, 3),
    i = n ? parseInt(i).to62() : parseInt(i).toString(36),
    i += randomStr(t),
    i = i.substr(0, t),
    i
}
function getActs(e){
    const acts = [
        {
            id:uuid(),
            fullPath:'/ccprec.com.cn.web/client/info/cqweb_nonphy_cqzr',
            args:[e,20,null]
        }
    ]
    return acts
}

function main(datas){
   const data = JSON.stringify({id:uuid(),projectKey,clientKey,token:null,clientDailyData:{},acts:getActs(datas.page)}),a=entrycode(JSON.stringify(data))
   return a
}
function de(data){
    return decryptCode(data)
}



(function(){
    var org = window.XMLHttpRequest.prototype.open
    window.XMLHttpRequest.prototype.open = function(m,u,a){
        console.log(m,u,a);
        return org(this,arguments)
    }
})();