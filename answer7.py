import multiprocessing

def calculate_square(num):
    square = num * num
    print(f"Process {multiprocessing.current_process().name}: Square of {num} is {square}")

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    processes = []
    for num in numbers:
        process = multiprocessing.Process(target=calculate_square, args=(num,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()


