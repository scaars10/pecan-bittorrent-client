import sys

from torrent import Torrent

if __name__ == "__main__":
    # file_name = sys.argv[1]
    print(sys.argv)

    file_name = '../data/ubuntu-22.04.3-desktop-amd64.iso.torrent'
    torrent = Torrent(file_name)
    # file_content = helper.read_binary_file(file_name)
    # decoded_file_content = bencode.decode(file_content)
    #
    # clientId = helper.generateIdWithPrefix('scaars-', 20)

    # print(decoded_file_content.keys())
