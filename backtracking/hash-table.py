class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for j in range(size)]

    def hashing(self, name, N):
        hash_val = 0
        for char in name:
            hash_val += ord(char)
        return hash_val % N

    def find_group(groups, name):
        for group in groups:
            if sorted(group[0]) == sorted(name):
                return group
        return None

    def create_group(groups, name):
        groups.append([name])

    def add_to_group(groups, name, index):
        groups[index].append(name)

    def join_groups(groups, name, index):
        group = hash_table.find_group(groups, name)
        if group:
            hash_table.add_to_group(groups, name, groups.index(group))

        else:
            hash_table.create_group(groups, name)


N = int(input())
hash_table = HashTable(size=N)
groups = []

while True:
    name = input("")
    if name == "FIM":
        break

    hash_val = hash_table.hashing(name, N)

    if not hash_table[hash_val]:
        hash_table[hash_val].append(name)
        hash_table.join_groups(groups, name, hash_val)
    else:
        found_group = hash_table.find_group(groups, hash_table[hash_val][0])
        if found_group and sorted(found_group[0]) == sorted(name):
            hash_table[hash_val].append(name)
            print(f"{name} entrou no grupinho")
        else:
            print(f"{name} tentou entrosar, mas foi descoberto")

print("Grupinhos:", groups)