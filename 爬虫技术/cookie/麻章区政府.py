import requests

cookies = {
    'zh_choose': 'n',
    'XSRF-TOKEN': 'eyJpdiI6IjViT0xFcHF1cmlkWjhRK1wvXC9WenROUT09IiwidmFsdWUiOiJTQ01xZ3JpRWNFU3VlS3QzSFI5eEJQdFBzUUxPZFdkdHRxNWJTUXlOV3UyMWRBTFJIaVBhUVZrZnZyeVZ1ZHoxIiwibWFjIjoiMTc2M2Y2YjZmZWFmNmEyZDQyNGJlYWZmNDg1MTE0YzIxODgwMzBhY2I0ZTdmZGQ5N2QzNTdjMjI0NWMxNmQ2MSJ9',
    'szxx_session': 'eyJpdiI6Ikt1bFVTdDJcL1wveVRBTkdvV2VFUVVtUT09IiwidmFsdWUiOiJhVE9uZGp3V1ViXC8xcnVvQ3YwRVBNQWxLdkFPYU5sXC8rdXl3SzJFRE5TY2NlbXJSZ0ZcL2kxWENaTTR5Y1JHdXB6IiwibWFjIjoiY2M4YzU5N2I3MGQ1MWMzMjMxY2VjMDlkOTZhNmM2ZTY3NjMyOWUzYzk4NmNlYjE4MGE5MDc5OWU0NjQ4YzhmOCJ9',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'zh_choose=n; XSRF-TOKEN=eyJpdiI6IjViT0xFcHF1cmlkWjhRK1wvXC9WenROUT09IiwidmFsdWUiOiJTQ01xZ3JpRWNFU3VlS3QzSFI5eEJQdFBzUUxPZFdkdHRxNWJTUXlOV3UyMWRBTFJIaVBhUVZrZnZyeVZ1ZHoxIiwibWFjIjoiMTc2M2Y2YjZmZWFmNmEyZDQyNGJlYWZmNDg1MTE0YzIxODgwMzBhY2I0ZTdmZGQ5N2QzNTdjMjI0NWMxNmQ2MSJ9; szxx_session=eyJpdiI6Ikt1bFVTdDJcL1wveVRBTkdvV2VFUVVtUT09IiwidmFsdWUiOiJhVE9uZGp3V1ViXC8xcnVvQ3YwRVBNQWxLdkFPYU5sXC8rdXl3SzJFRE5TY2NlbXJSZ0ZcL2kxWENaTTR5Y1JHdXB6IiwibWFjIjoiY2M4YzU5N2I3MGQ1MWMzMjMxY2VjMDlkOTZhNmM2ZTY3NjMyOWUzYzk4NmNlYjE4MGE5MDc5OWU0NjQ4YzhmOCJ9',
    'Origin': 'http://www.zjmazhang.gov.cn',
    'Pragma': 'no-cache',
    'Referer': 'http://www.zjmazhang.gov.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': 'MLqU6SCNnQRo97gXNZDef0jv4FP4D0PiY3TfznqT',
}

data = {
    'offset': '0',
    'limit': '20',
    'site_id': '759010',
    'time_from': '1667577600',
    'time_to': '1699113599',
}

response = requests.post(
    'http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList',
    cookies=cookies,
    headers=headers,
    data=data,
    verify=False,
)

print(response.text)