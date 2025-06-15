import bisect

class CustomDataStructure:
    def __init__(self):
        self.data = []
        self.total_sum = 0

    def add(self, x):
        bisect.insort(self.data, x)
        self.total_sum += x

    def remove(self, x):
        index = bisect.bisect_left(self.data, x)
        if index < len(self.data) and self.data[index] == x:
            del self.data[index]
            self.total_sum -= x

    def find_min(self):
        return self.data[0] if self.data else -1

    def find_max(self):
        return self.data[-1] if self.data else -1

    def find_sum(self):
        return self.total_sum

# Read input
def read_input():
    q = int(input().strip())
    queries = []
    for _ in range(q):
        query = input().strip().split()
        queries.append(query)
    return q, queries

# Process queries
def process_queries(q, queries):
    structure = CustomDataStructure()
    for query in queries:
        if query[0] == '1':
            structure.add(int(query[1]))
        elif query[0] == '2':
            structure.remove(int(query[1]))
        elif query[0] == '3':
            print(structure.find_min())
        elif query[0] == '4':
            print(structure.find_max())
        elif query[0] == '5':
            print(structure.find_sum())

# Main function
def main():
    q, queries = read_input()
    process_queries(q, queries)

if __name__ == "__main__":
    main()
