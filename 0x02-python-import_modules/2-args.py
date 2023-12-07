#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
argc = len(argv) - 1

print(f"{argc} {'argument' if argc == 1 else 'arguments'}:")
for i in range(1, argc + 1):
    print(f"{i}: {argv[i]}")
