import collections

def wide_Search(dict, index, searched_name):
    searched = []
    deque = collections.deque()
    for element in dict[index]:
        deque.append(element)
    while deque:
        print(" Deque = ", deque)
        person = deque.popleft()
        print(" Person = ", person)
        if not person in searched:
            if person == searched_name:
                print("Found!")
                return True
            else:
                for element in dict[person]:
                    deque.append(element)
                searched.append(person)
    print(" not Found...")        
    return False

if __name__ == "__main__":
    d = {}
    d['you'] = ['1', '2', '3']
    d['1'] = ['Jessie']
    d['2'] = ['Paulie', 'Sam']
    d['3'] = ['Heizenberg']
    d['Jessie'] = []
    d['Paulie'] = []
    d['Sam'] = []
    d['Heizenberg'] = []
    wide_Search(d, 'you', '')
     
            
