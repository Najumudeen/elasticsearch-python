from elasticsearch import Elasticsearch

# Setup Connection
es=Elasticsearch([{"host":"localhost","port":9200}])
print(es.ping) # return True or False

# display all indices
indices=es.indices.get_alias("*")
print(indices)
for index in indices:
    print(index)

# Create a Index
es.indices.create(index="tutorial1-16_10_2021")