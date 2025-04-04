from elasticsearch import Elasticsearch
import io

# Setup Connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic", "Password"))
print(es.ping) # return True or False

# Create Multiple Indices

index_basename = "october"

for i in range(1,11):
    response=es.indices.create(index=index_basename+"_"+str(i))
    print(response)


## Index creation in bulk using input file

with io.open("input.txt", "r",encoding="utf-8") as f1:
    data = f1.read()
    f1.close()

print(data)
# Converting data value string to list, Everyone one element in the list is a single object
data = data.split("\n")
print(data)

for index in data:
    response = es.indices.create(index=index)
    print(response)