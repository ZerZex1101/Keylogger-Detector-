import os

def load_words_from_file(word_file):
    try:
        with open(word_file, 'r') as f:
            return set(word.strip() for word in f)
    except FileNotFoundError:
        print(f"Error: The word file '{word_file}' was not found.")
        return set()

def search_words_in_directory(directory, words):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r') as f:
                    content = f.read()
                    for word in words:
                        if word in content:
                            print(f'Found word "{word}" in file: {file_path}')
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

def main():
    directory = '/home/kali'
    word_file = 'sear.txt'

    words = load_words_from_file(word_file)
    if words:
        search_words_in_directory(directory, words)
    else:
        print("No words to search for. Make sure the word file is valid.")

if name == 'main':
    main()