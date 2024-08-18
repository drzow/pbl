import os

#def get_cache(cache_type="NONE"):
def get_cache(cache_type=None):
    if cache_type == None:
        cache_type = os.environ.get('PBL_CACHE')
    if cache_type == 'REDIS':
        import pbl.redis_cache as cache
    elif cache_type == 'LEVELDB':
        import pbl.leveldb_cache as cache
    else:
        import pbl.nocache as cache

    print ('cache', cache.name)
    return cache
