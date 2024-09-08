import multiprocessing

def count_word(word, text):
    return text.count(word)

def process_file(names_filename, text, output_queue):
    with open(names_filename, 'r', encoding='utf-8') as f:
        names = f.read().splitlines()
        frequencies = {name: count_word(name, text) for name in names}
        output_queue.put(frequencies)

if __name__ == '__main__':
    text_filename = 'task1_3_text.txt'
    names_filename = 'task1_3_names.txt'
    output_filename = 'result.txt'

    with open(text_filename, 'r', encoding='utf-8') as f:
        text = f.read()

    output_queue = multiprocessing.Queue()

    # Start a process for counting frequencies
    process = multiprocessing.Process(target=process_file, args=(names_filename, text, output_queue))
    process.start()
    process.join()

    # Retrieve results from the queue
    result = output_queue.get()

    # Write results to output file
    with open(output_filename, 'w') as f:
        for name, count in result.items():
            f.write(f"{name}: {count}\n")