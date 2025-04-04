from elasticsearch import Elasticsearch
# Setup Connection
es=Elasticsearch([{"host":"localhost","port":9200}],http_auth=("elastic", "Password"))
print(es.ping) # return True or False

# Search and Index Delete

index_pattern="october_*"
response=es.search(index=index_pattern)
print(response)

# Print all the indices
response=es.indices.get_alias(index_pattern)
if (len(response)>0):
    for index in response:
        print(index)
else:
    print("no index has been found for the given search pattern")

# Search and Index Delete

if (len(response)>0):
    for index in response:
        delete_response = os.indices.delete(index=index)
        print(delete_response)
else:
    print("no index has been found for the given search pattern")
