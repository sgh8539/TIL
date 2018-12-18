
from darksky import forecast
mulcam = forecast('7c71e1611a4f23e6a408501808cc1b2b',37.501801, 127.039767)
# url = "https://api.darksky.net/forecast/7c71e1611a4f23e6a408501808cc1b2b/37.501801,127.039767"

# # res = requests.get(url)
# # data = res.json()
# # print(data['currently']['summary'])

print (mulcam['currently']['summary'])
print (mulcam['currently']['temperature'])