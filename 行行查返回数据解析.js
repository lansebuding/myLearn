const crypto = require("crypto-js");

var  r = "3sd&d2"
, c = "4h@$udD2s"
, a = "*";
function decrypt(n, o) {
    o = o || "".concat(r).concat(c).concat(a);
    var t = crypto.enc.Utf8.parse(o)
      , e = crypto.AES.decrypt(n, t, {
        mode: crypto.mode.ECB,
        padding: crypto.pad.Pkcs7
    });
    return crypto.enc.Utf8.stringify(e).toString()
}

function main(str){
  const x =decrypt(str)
  return x
}