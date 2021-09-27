

if __name__ == "__main__":

    print("Starting...")

    COUNT = 0
    n = 8
    sequence = []
    chosen = [False for i in range(n)]

    def check_queens(sequenceX, n):
        result = True
        sequenceY = [i for i in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                if abs(sequenceX[i] - sequenceX[j]) == abs(sequenceY[i] - sequenceY[j]):
                    result = False
        return result

    def generate_sequence_without_repetitions(sequence, chosen, n):
        global COUNT
        if len(sequence) == n:
            if check_queens(sequence, n):
                print("Found = ", *sequence)
                COUNT += 1
        else:
            for i in range(n):
                if chosen[i]:
                    continue
                chosen[i] = True
                sequence.append(i)
                generate_sequence_without_repetitions(sequence, chosen, n)
                chosen[i] = False
                sequence.pop()

    generate_sequence_without_repetitions(sequence, chosen, n)
    print("COUNT = ", COUNT)
