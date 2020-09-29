import math
import csv


def is_modified(seq):
    if seq[29] == 'A':
        return True
    else:
        if seq[101] == 'A':
            return True
        else:
            if seq[102] == 'A':
                return True
            else:
                return False


def get_entropy(seq):
    length = len(seq)
    a_count = 0
    g_count = 0
    c_count = 0
    t_count = 0
    for char in seq:
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
    entropy = -(a_count/length * math.log((a_count if a_count != 0 else 1)/length, 2)) - \
        (g_count/length * math.log((g_count if g_count != 0 else 1)/length, 2)) - \
        (t_count/length * math.log((t_count if t_count != 0 else 1)/length, 2)) - \
        (c_count/length * math.log((c_count if c_count != 0 else 1)/length, 2))
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
        entropy_array.append(get_entropy(seq=seq))
        modified_array.append(is_modified(seq=seq))
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
