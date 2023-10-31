import requests
import execjs


cookies = {
    '__lg_stoken__': 'f814c6625c7d3ff260cb3b91e8791f91bfe26c60ca7c512075c710eaa9ba8dfd62789cc88f67588c433c6662c73f8c4c0e65fb880c1bc3ec211e88d9fbc0022d77067b30d3c1',
    'X_HTTP_TOKEN': '42daf4b72327b2812387548961bf5e71415983ed09',
    'WEBTJ-ID': '20231028095034-18b73f9d344ad6-0d4345bd4bb909-26031151-2073600-18b73f9d345687',
    'JSESSIONID': 'ABAAAECABIEACCA0D827D00D50BDA1EB96854C7D071ACE2',
    'sajssdk_2015_cross_new_user': '1',
    'sensorsdata2015session': '%7B%7D',
    'Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1698457980',
    'user_trace_token': '20231028095300-6b31d822-4b7d-4043-81c5-efa00e509f4d',
    'LGUID': '20231028095300-a901b4ef-614b-495f-ad7d-64e55535ecc7',
    '_ga': 'GA1.2.79649013.1698457980',
    '_gid': 'GA1.2.1689931146.1698457980',
    'Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1698457985',
    'LGRID': '20231028095305-6a1949cb-eb01-402f-b2da-719dbd87fcb5',
    '_ga_DDLTLJDLHH': 'GS1.2.1698457980.1.1.1698457985.55.0.0',
    'sensorsdata2015jssdkcross': '%7B%22distinct_id%22%3A%2218b73f9d3a6128e-08598abaf0daaf-26031151-2073600-18b73f9d3a715e1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22118.0.0.0%22%7D%2C%22%24device_id%22%3A%2218b73f9d3a6128e-08598abaf0daaf-26031151-2073600-18b73f9d3a715e1%22%7D',
}

data = {"first":"true","needAddtionalResult":"false","city":"全国","pn":"2","cl":"false","fromSearch":"true","labelWords":"sug","suginput":"python","kd":"python"}
code = open('./逆向学习/拉勾网/1.js','r',encoding='utf-8').read()
params = execjs.compile(code)

xsheader = params.call("getXSHeader",data)
param = params.call("getParams",data)

headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': '__lg_stoken__=f814c6625c7d3ff260cb3b91e8791f91bfe26c60ca7c512075c710eaa9ba8dfd62789cc88f67588c433c6662c73f8c4c0e65fb880c1bc3ec211e88d9fbc0022d77067b30d3c1; X_HTTP_TOKEN=42daf4b72327b2812387548961bf5e71415983ed09; WEBTJ-ID=20231028095034-18b73f9d344ad6-0d4345bd4bb909-26031151-2073600-18b73f9d345687; JSESSIONID=ABAAAECABIEACCA0D827D00D50BDA1EB96854C7D071ACE2; sajssdk_2015_cross_new_user=1; sensorsdata2015session=%7B%7D; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1698457980; user_trace_token=20231028095300-6b31d822-4b7d-4043-81c5-efa00e509f4d; LGUID=20231028095300-a901b4ef-614b-495f-ad7d-64e55535ecc7; _ga=GA1.2.79649013.1698457980; _gid=GA1.2.1689931146.1698457980; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1698457985; LGRID=20231028095305-6a1949cb-eb01-402f-b2da-719dbd87fcb5; _ga_DDLTLJDLHH=GS1.2.1698457980.1.1.1698457985.55.0.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218b73f9d3a6128e-08598abaf0daaf-26031151-2073600-18b73f9d3a715e1%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24os%22%3A%22Windows%22%2C%22%24browser%22%3A%22Chrome%22%2C%22%24browser_version%22%3A%22118.0.0.0%22%7D%2C%22%24device_id%22%3A%2218b73f9d3a6128e-08598abaf0daaf-26031151-2073600-18b73f9d3a715e1%22%7D',
    'Origin': 'https://www.lagou.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.lagou.com/wn/jobs?pn=3&cl=false&fromSearch=true&labelWords=sug&suginput=python&kd=python',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',

    'X-K-HEADER': 'F8CHcB2RI0Il2Io1trl+dtrE/DDw+SJrn4WXO/TO34n7Ju1qA/aaJPulDNcbJEpY',
    'X-S-HEADER': xsheader,
    'X-SS-REQ-HEADER': '{"secret":"F8CHcB2RI0Il2Io1trl+dtrE/DDw+SJrn4WXO/TO34n7Ju1qA/aaJPulDNcbJEpY"}',

    'accept': 'application/json, text/plain, */*',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',

    # 'traceparent': '00-f230b4d9d3eb1df9cf2a3e039a8fee95-6f15bce292fa3e2f-01',

    'x-anit-forge-code': '0',
    'x-anit-forge-token': 'None',
}

data = {
    'data': param,
}

response = requests.post('https://www.lagou.com/jobs/v2/positionAjax.json', cookies=cookies, headers=headers, data=data).json()
texts = params.call("Decrypt",response['data'])
print(texts)