
def recaman_sequence(n):

    sequence = [0]

    def helper(k):
        if k == n:
            return
        prev = sequence[-1]
        candidate = prev - k
        if candidate > 0 and candidate not in sequence:
            sequence.append(candidate)
        else:
            sequence.append(prev + k)
        helper(k + 1)

    helper(1)
    return sequence



if __name__ == "__main__":
    
    n = 7
    print(recaman_sequence(n))