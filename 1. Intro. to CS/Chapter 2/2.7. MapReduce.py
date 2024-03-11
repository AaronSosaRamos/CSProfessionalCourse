from multiprocessing import Pool

def mapper(sentence):
    # Split the sentence into words and count each word
    word_count = {}
    for word in sentence.split():
        word_count[word] = word_count.get(word, 0) + 1
    return [(word, count) for word, count in word_count.items()]

def reducer(item):
    # Aggregate the word counts
    word, counts = item
    return (word, sum(counts))

def mapreduce(data, num_processes=4):
    # Map phase
    with Pool(num_processes) as pool:
        mapped_data = pool.map(mapper, data)

    # Flatten the mapped data
    mapped_data = [pair for sublist in mapped_data for pair in sublist]

    # Reduce phase
    reduced_data = {}
    for key, value in mapped_data:
        reduced_data[key] = reduced_data.get(key, []) + [value]

    # Apply reduce function
    result = [reducer(item) for item in reduced_data.items()]

    return result

if __name__ == "__main__":
    # Example input data
    sentences = [
        "Hello world",
        "This is a test",
        "Hello world again"
    ]

    # Perform MapReduce
    result = mapreduce(sentences)

    print("MapReduce result:")
    for word, count in result:
        print(f"{word}: {count}")
