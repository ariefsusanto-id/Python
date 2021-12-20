import requests, schedule

def indo():
    api_url="https://api.kawalcorona.com/indonesia/"
    result= requests.get(api_url).json()
    print(result)

def jabar():
    api_url="https://data.covid19.go.id/public/api/prov.json"
    result= requests.post(api_url).json()
    cek=result["DKI JAKARTA"]
    ambil_dic= cek["key"]
    a=[ambil_dic]
    print(a)

r_indo=schedule.every(2).seconds.do(indo)
r_jabar=schedule.every(2).seconds.do(jabar)

while True:
    schedule.run_pending()

data_indo=indo()
data_jabar=jabar()
print(data_indo)
print(data_jabar)