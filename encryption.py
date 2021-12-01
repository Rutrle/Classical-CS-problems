from secrets import token_bytes
from typing import Tuple

def random_key(length):
    tb = token_bytes(length)
    print(tb)

    return int.from_bytes(tb, "big")

print(random_key(5))

def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy # XOR
    return dummy, encrypted