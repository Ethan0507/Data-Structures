# python3

def read_input():
    return (input().rstrip(), input().rstrip())

def print_occurrences(output):
    print(' '.join(map(str, output)))

# def get_occurrences(pattern, text):
#     return [
#         i
#         for i in range(len(text) - len(pattern) + 1)
#         if text[i:i + len(pattern)] == pattern
#     ]


def precomputeHash(text, p, prime, x):
    hashes = [polyHash(text[len(text) - p:], prime, x)]
    for i in range(len(text) - p - 1, -1, -1):
        hashes.append(((((x * hashes[-1]) + ord(text[i])) - (ord(text[i + p]) * (x ** p)) % prime) + prime) % prime)
    return hashes


def polyHash(pattern, prime, x):
    hashed = 0
    for i in reversed(pattern):
        hashed = ((hashed * x) + ord(i)) % prime
    return hashed


def rabinKarp(pattern, text):
    prime = 10 ** 9 + 7
    x = 1
    T = len(text)
    P = len(pattern)
    pHash = polyHash(pattern, prime, x)
    H = precomputeHash(text, P, prime, x)
    matches = []
    for i in range(T - P, -1, -1):
        if H[(T - P) - i] != pHash:
            continue
        if text[i: i + P] == pattern:
            matches.append(i)
    return [x for x in reversed(matches)]


if __name__ == '__main__':
    print_occurrences(rabinKarp(*read_input()))

