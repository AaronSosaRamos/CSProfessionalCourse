import random
import threading
import time

class BigDataProcessor:
    def __init__(self, data_size):
        self.data_size = data_size
        self.data = [random.randint(0, 100) for _ in range(data_size)]
        self.processed_data = [0] * data_size
        self.lock = threading.Lock()

    def process_data_chunk(self, start_index, end_index):
        for i in range(start_index, end_index):
            self.processed_data[i] = self.data[i] * 2

    def process_data_multithreaded(self, num_threads):
        start_time = time.time()
        chunk_size = self.data_size // num_threads
        threads = []
        for i in range(num_threads):
            start_index = i * chunk_size
            end_index = start_index + chunk_size if i < num_threads - 1 else self.data_size
            thread = threading.Thread(target=self.process_data_chunk, args=(start_index, end_index))
            thread.start()
            threads.append(thread)
        for thread in threads:
            thread.join()
        end_time = time.time()
        return end_time - start_time

    def process_data_singlethreaded(self):
        start_time = time.time()
        self.process_data_chunk(0, self.data_size)
        end_time = time.time()
        return end_time - start_time

if __name__ == "__main__":
    data_size = 10000000  # Size of the big data
    num_threads = 4  # Number of threads to use for processing

    big_data_processor = BigDataProcessor(data_size)

    # Processing with multithreading
    multithreaded_time = big_data_processor.process_data_multithreaded(num_threads)
    print("Data processed successfully with multithreading. Time taken:", multithreaded_time, "seconds")

    # Processing without multithreading
    singlethreaded_time = big_data_processor.process_data_singlethreaded()
    print("Data processed successfully without multithreading. Time taken:", singlethreaded_time, "seconds")
