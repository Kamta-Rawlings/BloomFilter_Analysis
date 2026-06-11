# datasets/generate_dna.py

import random

alphabet = "ACGT"

with open("datasets/dna.txt", "w") as f:
    for _ in range(10000):
        f.write(
            "".join(random.choice(alphabet)
                    for _ in range(30))
            + "\n"
        )