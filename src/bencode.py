import bencodepy as bencoder


def decode(encodedData):
    return bencoder.decode(encodedData)


def encode(data):
    return bencoder.encode(data)
