import matplotlib.pyplot as plt

def plot_chunk_distribution(all_chunks):

    chunk_lengths = [len(chunk) for chunk in all_chunks]

    plt.figure(figsize=(8,5))
    plt.hist(chunk_lengths, bins=20, alpha=0.7)
    plt.title("Distribution of Chunk Lengths")
    plt.xlabel("Chunk Length (characters)")
    plt.ylabel("Frequency")
    plt.grid(True)

    plt.savefig("outputs/chunk_distribution.png")
    plt.close()