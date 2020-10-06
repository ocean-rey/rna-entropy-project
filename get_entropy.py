import math
import csv
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("window", help="Window size", type=int)
args = parser.parse_args()

def is_modified(seq):
    if seq[29] == 'A':
        return 29
    else:
        if seq[101] == 'A':
            return 101
        else:
            if seq[102] == 'A':
                return 102
            else:
                return False


def get_entropy(seq):
    entropy = []
    window_size = args.window
    window_open = 0;
    window_close = window_open+window_size;
    while(window_close < len(seq)-1):
        a_count = 0
        g_count = 0
        c_count = 0
        t_count = 0
        window_seq = seq[window_open:window_close]
        for char in window_seq:
            if char == 'A':
                a_count += 1
            else:
                if char == 'G':
                    g_count += 1
                else:
                    if char == 'C':
                        c_count += 1
                    else:
                        if char == 'T':
                            t_count += 1
        entropy.append(-(a_count/window_size * math.log((a_count if a_count != 0 else 1)/window_size, 2)) - \
            (g_count/window_size * math.log((g_count if g_count != 0 else 1)/window_size, 2)) - \
            (t_count/window_size * math.log((t_count if t_count != 0 else 1)/window_size, 2)) - \
            (c_count/window_size * math.log((c_count if c_count != 0 else 1)/window_size, 2)))
        window_open += 1
        window_close = window_open+window_size
    return(entropy)


def main():
    f = open("sine-sequence-reference.fa", "r")
    i = 0
    seq_array = []
    name_array = []
    modified_array = []
    entropy_array = []
    for x in f:
        if i % 2:
            seq_array.append(x)
        else:
            name_array.append(x)
        i += 1
    f.close()
    for seq in seq_array:
        entropies = get_entropy(seq)
        entropy_array.append(entropies)
        mod_index = is_modified(seq=seq)
        if mod_index is False:
            modified_array.append(mod_index)
        else:
            mods = []
            entropies_index = mod_index-(args.window-1)
            while entropies_index <= mod_index or entropies_index > len(entropies)-1:
                mods.append(entropies[entropies_index])
                entropies_index += 1
            modified_array.append(mods)
    with open('entropies.csv', 'w', newline='') as csv_file:
        fieldnames = ['seq', 'name', 'entropy', 'modified']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        index = 0
        while index < len(seq_array):
            writer.writerow({'seq': seq_array[index], 'name': name_array[index],
                             "entropy": entropy_array[index], "modified": modified_array[index]})
            index += 1


if __name__ == "__main__":
    main()