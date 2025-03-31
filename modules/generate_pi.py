import json
from mpmath import mp


def save_pi_chunks(chunk_length, n_chunks, save_path):

    required_digits = chunk_length * n_chunks
    mp.dps = required_digits + 2
    pi_str = str(mp.pi)[2:required_digits + 2]

    pi_chunks = {
        i + 1: "".join(pi_str[i * chunk_length:(i + 1) * chunk_length])
        for i in range(n_chunks)
    }

    with open(save_path, "w") as f:
        json.dump(pi_chunks, f, indent=4)


save_pi_chunks(
    chunk_length=200,
    n_chunks=20,
    save_path="__cache__/chunks.json"
)