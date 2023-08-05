from token_bucket import MemoryStorage, Limiter


def main():
    storage = MemoryStorage()
    limiter = Limiter(rate=1, capacity=1, storage=storage)

    print("Hello world!")
