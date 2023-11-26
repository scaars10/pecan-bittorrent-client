import random
import string
from urllib.parse import urlencode


def generateIdWithPrefix(prefix, size):
    if len(prefix) > size:
        raise RuntimeError('Size of prefix greater than size of ID')
    random_size = size - len(prefix)
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=random_size))
    return prefix + random_id


async def connect_to_torrent_tracker(decoded_torrent, peer_id, first: bool=None, uploaded: int = 0, downloaded: int = 0):
    params = {...}
    params['peer_id'] = peer_id
    params['uploaded'] = uploaded
    params['downloaded'] = downloaded
    params['info_hash'] = decoded_torrent.info
    url = decoded_torrent.announce+'?'+urlencode(params)