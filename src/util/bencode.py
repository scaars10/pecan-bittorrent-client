import bencodepy as bencoder


def decode(encoded_data):
    return bencoder.decode(encoded_data)


def encode(data):
    return bencoder.encode(data)

