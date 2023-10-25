const crypto =require('crypto')

const decodeKey="ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl",
  decodeIv="ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"
function fn(t){
    if (!t)
        return null;
        const a = Buffer.alloc(16, y(decodeKey))
        , c = Buffer.alloc(16, y(decodeIv))
        , r = crypto.createDecipheriv("aes-128-cbc", a, c);
    let s = r.update(t, "base64", "utf-8");
    return s += r.final("utf-8"),
    s
}

function y(e) {
    return crypto.createHash("md5").update(e).digest()
}