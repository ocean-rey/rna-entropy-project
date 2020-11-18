import math
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-k", help="k size", type=int)
args = parser.parse_args()

def get_paretto_values(seq):
    k_mer_dict = {}
    length = len(seq)-1
    window_open = 0
    window_close = 0 + args.k
    while(window_close<=length):
        k_mer = seq[window_open:window_close]
        if k_mer in k_mer_dict.keys():
            k_mer_dict[k_mer] += 1
        else:
            k_mer_dict[k_mer] = 1
        window_open += 1
        window_close +=1
    return k_mer_dict

def main():
    seq_array = []
    name_array = []
    dict_array = []
    f = open("sine-sequence-reference.fa", "r")
    i = 0
    for x in f:
        if i % 2:
            seq_array.append(x)
        else:
            name_array.append(x)
        i += 1
    f.close()
    k_mer_array = []
    for seq in seq_array:
       dict_array.append(get_paretto_values(seq))
    for _dict in dict_array:
        _keys = list(_dict.keys())
        k_mer_array = k_mer_array + _keys
    k_mer_array = list(set(k_mer_array))

    with open('paretto.csv', 'w', newline='') as csv_file:
        fieldnames = ['name']
        fieldnames = fieldnames + k_mer_array
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        index = 0
        while index < len(seq_array):
            dict_array[index]["name"] = name_array[index]
            writer.writerow(dict_array[index])
            index +=1

if __name__ == "__main__":
    main()