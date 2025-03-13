import random

class Node:
    def __init__(self, val):
        self.val = val
        self.prize = 0
        self.next = None
        self.prev = None
    
def main():
    prize_in_arc = [10000, 250, 750, 100, 1000, 500, 2500, 750, 5000, 250, 1500, 500, 2500, 100, 1500, 100]
    
    head = Node(prize_in_arc[0])
    node = head
    for prize in prize_in_arc[1:]:
        node.next = Node(prize)
        node.next.prev = node
        node = node.next
    node.next = head
    head.prev = node

    print("Default player number is: 1")
    print("Enter q to quit and see result")

    player_head = Node(1)
    while True:        
        player_n = input("Enter a player number to take turn ")
        if player_n == 'q':
            break
        player_n = int(player_n)
        spin_dir = input("Choose spin direction\na - anticlockwise, c - clockwise\n")
        prize_idx = random.randint(1,50)
        node = head
        if spin_dir == 'c':
            print(f"Player {player_n} spinning the wheel...")
            for i in range(prize_idx):
                print(node.val, end=" : ")
                node = node.next
            print(node.val)
        elif spin_dir == 'a':
            print(f"Player {player_n} spinning the wheel...")
            for i in range(prize_idx):
                print(node.val, end=" : ")
                node = node.prev
            print(node.val)
        else:
            print("Oops that isn't an expected direction you lose this chance.")
            continue
        head = node

        prize = node.val
        print(f"Hurray! Player {player_n} won ${prize}")
        node = player_head
        while node.val != player_n:
            prev = node
            node = node.next
            if node is None:
                node = Node(player_n)
                prev.next = node
                break
        
        node.prize = node.prize + prize
        print(f"Total prize with Player {player_n} = ${node.prize}")
        print()

    print("Player\tPrize($)")
    node = player_head
    while node:
        print(f"{node.val}\t{node.prize}")
        node = node.next    

if __name__ == '__main__':
    main()
