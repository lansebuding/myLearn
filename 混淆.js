 const crypto = require('crypto-js')

function getResCode() {
    var _0xfc0ed3 = crypto['AES']['encrypt'](crypto['enc']['Utf8']['parse'](Math['floor'](gxgNE(new Date()['getTime'](), 1000))), crypto['enc']['Utf8']['parse']
      ('1234567887654321'), 
      {
        'iv': crypto['enc']['Utf8']['parse']('1234567887654321'),
        'mode': crypto['mode']['CBC'],
        'padding': crypto['pad']['Pkcs7']
    });
    return crypto['enc']['Base64']['stringify'](_0xfc0ed3['ciphertext']);

}


function gxgNE(_0x5d0c06, _0x5c2e80) {
    return tk(_0x5d0c06, _0x5c2e80);
}

function tk(_0x60c3f3, _0x1beeba) {
    return _0x60c3f3 / _0x1beeba;
}
