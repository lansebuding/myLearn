var arr = [
    "66",
    "72",
    "6f",
    "6d",
    "43",
    "68",
    "61",
    "72",
    "43",
    "6f",
    "64",
    "65",
  ];

function v(t) {
  t = encodeURIComponent(t)["replace"](/%([0-9A-F]{2})/g, function (n, t) {
    return o("0x" + t);
  });
  try {
    return btoa(t);
  } catch (n) {
    return Buffer.from(t).toString("base64");
  }
}
function o(n) {
  (t = ""),
    arr.forEach(function (n) {
      t += unescape("%u00" + n);
    });
  var t,
    e = t;
  return String[e](n);
}
function y(n, t, e) {
  var H = 0,
    B = 1;
  for (var r = void 0 === e ? 2166136261 : e, a = H, i = n.length; a < i; a++)
    r =
      (r ^= n.charCodeAt(a)) +
      ((r << B) + (r << 4) + (r << 7) + (r << 8) + (r << 24));
  return t ? ("xyz" + (r >>> H).toString(16) + "efgh").substr(-16) : r >>> H;
}
function h(n, t) {
  var H = 0,
    R = "length",
    q1 = "charCodeAt";
  // t = t || u();
  for (var e = (n = n.split(""))[R], r = t[R], a = q1, i = H; i < e; i++)
    n[i] = o(n[i][a](H) ^ t[(i + 10) % r][a](H));
  return n.join("");
}

// function getParam(){}


function main(a) {
//   var a = ["all", "ipad", "cn", "36"];
  var r = new Date() - 1661224081041;
  a = a["sort"]()["join"]("");
  a = v(a);
  a =
    (a += "@#" + "/rank/index".replace("https://api.qimai.cn", "")) +
    ("@#" + r) +
    ("@#" + 3);
  var d = y("qimai@2022&Technology", 1);
  var e = v(h(a, d));
  return e;
}
