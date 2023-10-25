 const crypto = require('crypto')

function k(e) {
    const t ='fsdsogkndfokasodnaso',d='fanyideskweb',u='webfanyi'
    return j(`client=${d}&mysticTime=${e}&product=${u}&key=${t}`)
}

function j(e) {
    return crypto.createHash("md5").update(e.toString()).digest("hex")
}

function main (time){
    return k(time)
}