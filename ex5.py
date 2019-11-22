"""
Author: <Natalia Brndiarova>
"""


def count_bases_and_subsequence(data_as_string:str, subsequence:str):
    #Split the file into lines
    data_1 = list(data_as_string.split("\n"))
    new_list = []
    for line in data_1:
        if "Data" in line:
            break
        elif line.startswith('#'):
            continue
        elif len(line) == 0 or line.startswith('\n'):
            continue
        else:
            new_list.append(line)
    print(new_list)
    info = []
    base = []
    quality = []
    for line in new_list:
        "".join(line)
        splitted = line.split(";")
        info.append(splitted[0])
        base.append(splitted[1])
        quality.append(splitted[2])


# Check the substring
    new_base = []
    quality_float = [float(i) for i in quality]
    for i in range(len(new_list)):
        if 0.05 <= quality_float[i]:
            new_base.append(base[i])
        else:
            continue
    joined = "".join(new_base)
    substring = subsequence.lower()
    subsequence_count = joined.count(substring)
    count_a = joined.count("a")
    count_A = joined.count("A")
    count_g = joined.count("g")
    count_G = joined.count("G")
    count_t = joined.count("t")
    count_T = joined.count("T")
    count_c = joined.count("c")
    count_C = joined.count("C")
    base_counts = {'a': (count_a + count_A), 'c': (count_c + count_C), 'g': (count_g + count_G),
                   't': (count_t + count_T)}

    return base_counts, subsequence_count














        







