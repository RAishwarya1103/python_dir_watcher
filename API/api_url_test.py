import requests

BASE = "http://127.0.0.1:5000/"


## get config
response = requests.get(BASE + "/config")
print(response.json())
# input()
# get active config
# response = requests.get(BASE + "/activeConfig")
# print(response.json())
# input()

# inputConfig = {
#     "directory": "c:\program files",
#     "interval": 5,
#     "period": "seconds",
#     "isActive": False,
#     "magicString": "Aish",
# }

# response = requests.post(BASE + "/config", inputConfig)
# print(response.json())
# input()
# response = requests.put(BASE + "/config", {"isActive": False, "id": 1})
# print(response.json())
# input()

# ## get task_detail
response = requests.get(BASE + "/taskDetail/1")
print(response.json())
input()
# ## get all task details
response = requests.get(BASE + "/taskDetails")
print(response.json())
# input()