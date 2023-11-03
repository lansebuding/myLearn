// var nodeRsa = require('node-rsa')

// var key = new nodeRsa().generateKeyPair(1024),pubKey = key.exportKey('pkcs8-public'),privateKey = key.exportKey('pkcs8-private'),text = '你好'

// // console.log('公钥===',pubKey);
// // console.log('%c =================','color:red');
// // console.log('私钥===',privateKey);

// function en(text){
//     const enData = new nodeRsa(pubKey).encrypt(text,'base64')
//     return enData
// }

// console.log(en('你好'));

const jsEncrypt = require('jsencrypt')
const i = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCeiLxP4ZavN8qhI+x+whAiFpGWpY9y1AHSQC86qEMBVnmqC8vdZAfxxuQWeQaeMWG07lXhXegTjZ5wn9pHnjg15wbjRGSTfwuZxSFW6sS3GYlrg40ckqAagzIjkE+5OLPsdjVYQyhLfKxj/79oOfjl/lV3rQnk/SSczHW0PEyUbQIDAQAB'

function encrypt(data){
    const k = new jsEncrypt()
    k.setPublicKey(i);
    return k.encrypt(data)
}