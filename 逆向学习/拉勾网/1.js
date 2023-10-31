const crypto = require("crypto-js");

//加密
function It(t) {
  var Pt = crypto.enc.Utf8.parse("c558Gq0YQK2QUlMc");
  (kt = crypto.enc.Utf8.parse("qVXwXsFzTR9G26tvN8+dA/cQajVNHBOl")),
    (t = crypto.enc.Utf8.parse(t));
  t = crypto.AES.encrypt(t, kt, {
    iv: Pt,
    mode: crypto.mode.CBC,
    padding: crypto.pad.Pkcs7,
  });
  return t.toString();
}
// 解密
function Dt(t) {
  var Pt = crypto.enc.Utf8.parse("c558Gq0YQK2QUlMc");
  const kt = crypto.enc.Utf8.parse("qVXwXsFzTR9G26tvN8+dA/cQajVNHBOl");
  t = crypto.AES.decrypt(t, kt, {
    iv: Pt,
    mode: crypto.mode.CBC,
    padding: crypto.pad.Pkcs7,
  }).toString(crypto.enc.Utf8);
  return t;
}

function getXSHeader(data) {
  var e = { deviceType: 1 };
  var r = "https://www.lagou.com/jobs/v2/positionAjax.json";
  var t = JSON.stringify(e) + r + data;
  t = crypto.SHA256(t).toString().toUpperCase();
  var obj = JSON.stringify({
    originHeader: JSON.stringify(e),
    code: t,
  });
  return It(obj);
}

function getParams(data) {
  return It(JSON.stringify(data));
}

function Decrypt(data) {
  return Dt(data);
}
