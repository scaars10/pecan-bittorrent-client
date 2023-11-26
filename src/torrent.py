from src.util.common_helper import read_binary_file
import util.bencode as bencoder
from hashlib import sha1


class Torrent:
    def __init__(self, file_path):
        file_content = read_binary_file(file_path)
        self.torrent = bencoder.decode(file_content)

        print(self.torrent.keys())
        self.announce = self.torrent[b'announce']
        self.announce_list = self.torrent[b'announce-list']
        self.info = self.torrent[b'info']
        self.hash_info = sha1(self.info).digest()
        print(self.torrent.keys())
