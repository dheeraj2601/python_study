from couchbase.admin import Admin
from couchbase.bucket import Bucket

admin = Admin('Administrator', 'password', host='127.0.0.1', port=8091)

def _insert_bucket(bucket_name):
	# create bucket
	admin.bucket_create(name=bucket_name,
        	            bucket_type='couchbase',
                	    ram_quota=100)

	# optionally wait for bucket to be ready
	admin.wait_ready(bucket_name,
        	         timeout=10.0)

	url = 'couchbase://localhost/'+bucket_name
	cb = Bucket(url)

	indexing = 'CREATE PRIMARY INDEX `write-primary-index` ON '+bucket_name
	cb.n1ql_query(indexing).execute()
# 'first' = doc id . can be no as well as alpha
        cb.upsert('first', {'hello': 'world', 'additional': True, 'dk': 'test'})

def _remove_bucket(bucket_name):
	admin.bucket_remove(bucket_name)
	

def _create_index_in_existing_bucket():
	url = 'couchbase://localhost/'+bucket_name
	cb = Bucket(url)
	indexing = 'CREATE PRIMARY INDEX `chat-primary-index` ON '+bucket_name
	cb.n1ql_query(indexing).execute()
	

#if __name__ == '__main__':
#	_insert_bucket()
#	_remove_bucket()
#	_create_index_in_existing_bucket()





