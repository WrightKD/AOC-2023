import itertools

data = open('input.txt')

possible_sequences = {}
possible_groups = {}
valid_seq_count = 0

def get_possible_sequences(size):
    sequences = []
    for i in itertools.product(['.', '#'], repeat=size):
        v = ''.join(i)
        sequences.append(v)
        group = ','.join([str(x.count('#')) for x in v.split('.') if x != ''])
        if group in possible_groups:
            possible_groups[group].append(v)
        else:
            possible_groups[group] = [v]
        print(v)
        
    return sequences

for l in data:
    line = l.strip()
    seq, group = line.split()
    # seq = '?'.join([seq] * 5)
    # group = ','.join([group] * 5)

    if len(seq) not in possible_sequences:
        possible_sequences[len(seq)] = get_possible_sequences(len(seq))

    for v in possible_groups:
        if v == group:
            for k in possible_groups[v]:
                if len(k) != len(seq):
                    continue
                is_vaild = True
                for g,h in list(zip(k,seq)):
                    if h == '?':
                        continue
                    if g != h:
                        is_vaild = False
                        break
                if is_vaild:
                    print(k)
                    valid_seq_count += 1


print(valid_seq_count)