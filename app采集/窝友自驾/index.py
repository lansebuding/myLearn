import requests

headers = {
    'X-Camper-APP-Sign': 'SUFAoVNce1lhdCMLhV1K4WJFtweyZ3uOZA5stD6FY0TY+AMjJ2jt0p55FtUoKfXcLwdfbpV72HCVgMBMgk/pBEXDN3G2VCi0onyvhQt7Ep2kqMhQL5ghy0pA8J38aqImaMRQDu4xsKRyzWsIt7i6eAlhRtwf95b8iXJ8aNBzVPGuSYI/RqjAaZUiO0uRfVNqlHiCExseFnxDkfiTKCDSUj5+Jg83pTGQUdcmPOAYu759xm8Bw+LVj2qbwMX4xh/vNIvf3gqiUn6QxGQdT1sVYMBxHS9kJN4FrMPTnk70R8wzzYnlv5r/U0ZWWjUwsp8JeLFbwV+NbHP/GJx09KHTcw==',
    'X-Camper-APP-Token': '3f3839373132353535663239366432663239353131343034363832396132663834316266623231333130',
    'X-Camper-APP-InstallationId': '525aad51ed314637a3a87097b9bb66b3',
    'Host': 'app.woyouzhijia.cn',
    'User-Agent': 'okhttp/3.12.0',
}

params = {
    'searchKey': '',
    'page': '2',
    'limit': '20',
    'sort': '',
    'order': '',
}

response = requests.get('https://app.woyouzhijia.cn/app/userCard/find', params=params, headers=headers)
response.encoding='utf8'
