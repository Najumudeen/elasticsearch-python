from elasticsearch import Elasticsearch
import io
# Setup Connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic", "Password"))
print(es.ping) # return True or False

with io.open("input.txt", "r", encoding="utf-8") as f1:
    data = f1.read()
    f1.close()

data = data.split("\n") # to get the value in single line

print(data)

for index in data:
    try:
        response = es.indices.delete(index=index)
        print(response)
    except Exception as e:
        print(f"error occured while deleting index:" + index + "__with exact error: " + str(e))

