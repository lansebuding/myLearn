var nodeRsa = require('node-rsa')

var key = new nodeRsa().generateKeyPair(1024),pubKey = key.exportKey('pkcs8-public'),privateKey = key.exportKey('pkcs8-private'),text = '你好'

// console.log('公钥===',pubKey);
// console.log('%c =================','color:red');
// console.log('私钥===',privateKey);

function en(text){
    const enData = new nodeRsa(pubKey).encrypt(text,'base64')
    return enData
}

console.log(en('你好'));