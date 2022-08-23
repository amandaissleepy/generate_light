from generate_land import ask_for_number, generate_land
import os

os.makedirs("outputs", exist_ok=True)

noise_levels = [1, 5, 10, 20,50, 100, 250, 500]

for i in noise_levels:
    output = generate_land(200, 200, i)
    filename = os.path.join("outputs", f"test-{i}.txt")

    with open(filename, "w") as f:
        f.write(output)