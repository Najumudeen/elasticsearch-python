
from elasticsearch import Elasticsearch
# Setup Connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic", "Password"))
print(es.ping) # return True or False

# search specific index
index="hr"
try:
    response=es.search(index=index)
    print(response["_shards"]["total"])   ## Return value get 1
except Exception as e:
    print(str(e))

## Regex
# Search Index based on pattern
index="october_*"
try:
    response = es.search(Index=index)
    print(response["_shards"]["total"])
except Exception as e:
    print(str(e))

