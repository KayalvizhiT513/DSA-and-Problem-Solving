import os
import keyboard

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class TreeNode:
    def __init__(self, val):
        self.data = val
        self.children = {}
        self.end_of_word = False

word = []  # global input buffer
suggestions = []  # global suggestion list
sentence = [] # global sentence list

def main():
    global word, suggestions

    root = TreeNode('*')
    vocabulary = []

    with open("english-words.txt", "r") as file1:
        for i, line in enumerate(file1):
            clean_word = line.strip()
            if clean_word:
                vocabulary.append(clean_word)

    # Build Trie
    for vocab_word in vocabulary:
        node = root
        for char in vocab_word:
            if char not in node.children:
                node.children[char] = TreeNode(char)
            node = node.children[char]
        node.end_of_word = True

    def suggest_words(prefix, node):
        results = []

        def dfs(current_word, current_node):
            if current_node.end_of_word:
                results.append(current_word)
            for char, child in current_node.children.items():
                dfs(current_word + char, child)

        dfs(prefix, node)
        return results

    def on_type(event):
        global word, suggestions, sentence
        clear()
        curr_ch = event.name

        if curr_ch == 'space':
            word.append(' ')
            sentence.append(''.join(word))
            word = []
            print(f"Current text: {''.join(sentence)} {''.join(word)}")
            return
        elif curr_ch == '.':
            word.append('. ')
            sentence.append(''.join(word))
            word = []
            print(f"Current text: {''.join(sentence)} {''.join(word)}")
            return

        if curr_ch == 'esc':
            print("\nExiting...")
            keyboard.unhook_all()
            return

        # Handle suggestion selection
        if curr_ch in ['0', '1', '2'] and len(suggestions) > int(curr_ch):
            selected = suggestions[int(curr_ch)]
            word = list(selected)  # replace current word with selection
            print(f"Selected suggestion: {selected}")
        elif curr_ch.isalpha():
            word.append(curr_ch)
        elif curr_ch == 'backspace' and word:
            word.pop()

        # Find node corresponding to current prefix
        node = root
        valid = True
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                valid = False
                break

        if valid:
            suggestions = suggest_words(''.join(word), node)
            print(f"Current text: {''.join(sentence)} {''.join(word)}")
            print("Suggestions:")
            for ind, suggestion in enumerate(suggestions[:3]):
                print(f"{ind}: {suggestion}")
        else:
            suggestions = []
            print(f"'{''.join(word)}' not found in dictionary.")

    keyboard.on_press(on_type)
    keyboard.wait('esc')

if __name__ == "__main__":
    main()
