from bs4 import BeautifulSoup
import requests
import csv



url = "https://app.theinspiredhomeshow.com/Connect365/Results/ByExpoDataTable"

data = {
    "columns": [{"data": None, "name": "", "searchable": True, "orderable": True, "search": {"value": "", "regex": False}}],
    "order": [{"column": 0, "dir": "asc"}],
    "start": 200,
    "length": 10,
    "search": {"value": "", "regex": False},
    "keyword": "",
    "badgeId": 0,
    "country": "",
    "expo": "clean + contain",
    "state": "",
    "interestId": 0,
    "showExpo": "",
    "showCategory": ""
}

response = requests.post(url, json=data)
response_json = response.json()
print(response_json)
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Company Name', 'Result Type', 'Booth Number', 'Description']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for item in response_json['data']:
        description_html = item.get('description', '') or ''
        description_text = BeautifulSoup(description_html, 'html.parser').get_text()
        writer.writerow({
            'Company Name': item['name'],
            'Result Type': item['resultType'],
            'Booth Number': item.get('boothNumbers', '').strip(),
            'Description': description_text
        })

print("CSV file generated successfully.")
