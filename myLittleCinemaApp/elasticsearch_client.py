from elasticsearch import Elasticsearch

es = Elasticsearch(["http://localhost:9200"])

def check_connection():
    return es.ping()

def create_document(index, id, document):
    return es.index(index=index, id=id, body=document)

def get_document(index, id):
    return es.get(index=index, id=id)['_source']

def update_document(index, id, updated_fields):
    return es.update(index=index, id=id, body={"doc": updated_fields})

def delete_document(index, id):
    return es.delete(index=index, id=id)

def search_documents(index: str, query: dict):
    return es.search(index=index, body=query)