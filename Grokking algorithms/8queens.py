

if __name__ == "__main__":

    print("Starting...")

    n = 3
    sequence = []
    chosen = [False for i in range(n)]


    def generate_sequence_without_repetitions(n):
        if len(sequence) == n:
            print(*sequence)
        else:
            for i in range(n):
                if chosen[i]:
                    continue
                chosen[i] = True
                sequence.append(i)
                generate_sequence_without_repetitions(n-1)
                chosen[i] = False
                sequence.pop()

    generate_sequence_without_repetitions(n)
