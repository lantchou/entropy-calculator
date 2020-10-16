import matplotlib.pyplot as plt
from src.entropy import compute_entropy


N = 14
INPUT_FILES = ["random.txt", "rest.txt", "lonely-boy.txt"]
COLORS = ["red", "green", "blue"]
MARKERS = ["o", "s", "v"]

fig, ax = plt.subplots()

for i, filename in enumerate(INPUT_FILES):
    with open(f'../input/{filename}') as f:
        text = "".join(f.readlines())
        x = []
        y = []
        for n in range(N + 1):
            entropy = compute_entropy(text, n)
            # print(f"{filename}, {n}, {entropy}")
            x.append(n)
            y.append(entropy)
        ax.plot(x, y, color=COLORS[i], marker=MARKERS[i])

plt.xlim(0)
plt.ylim(0)
plt.xlabel("N")
plt.ylabel("Entropie")
plt.legend(INPUT_FILES)
plt.show()

fig.savefig("benchmark.png")
