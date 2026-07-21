import multiprocessing
import random
import time


TIME_LIMIT = 60.0


def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1
#takes first element as a sorted one
        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1
#while element on the left is bigger we move it into the right
        array[j + 1] = current_value

    return array

#BUBBLE SORT - compares adjacent elements
def bubble_sort(array):
    n = len(array)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = (
                    array[j + 1],
                    array[j]
                )
                swapped = True

        if not swapped:
            break
#non-decreasing O(n)
    return array

#Runs a sorting algorithm and measures its execution time.
def sorting_worker(sort_function, array, result_queue):
    start_time = time.perf_counter() #remembers starting time

    sorted_array = sort_function(array) #runs any algorithm

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time #counts working time

    result_queue.put(
        (elapsed_time, sorted_array)
    )

 #Runs a sorting algorithm in a separate process. If the algorithm exceeds the time limit, the process is terminated.
def run_with_time_limit(
    sort_function,
    array,
    time_limit=60.0
):

    result_queue = multiprocessing.Queue() #is used to retrieve the result from the sorting process.

    process = multiprocessing.Process(
        target=sorting_worker,
        args=(
            sort_function,
            array.copy(), #every algorithm should have the same starting array
            result_queue
        )
    )

    process.start()
    process.join(timeout=time_limit)

    if process.is_alive():
        process.terminate()
        process.join()

        return None, None #None informs main function about exceeded limit

    if result_queue.empty():
        return None, None

    elapsed_time, sorted_array = result_queue.get() #if sorting ended on time, func returns time and sorted array

    return elapsed_time, sorted_array

#Creates an increasing, random or decreasing array.
def create_array(array_type, size):
    if array_type == "increasing": #nondecreasing
        return list(range(1, size + 1))

    if array_type == "random":
        array = list(range(1, size + 1))
        random.shuffle(array) #changes order of elements
        return array

    if array_type == "decreasing": #nonincreasing
        return list(range(size, 0, -1))

    raise ValueError(
        f"Unknown array type: {array_type}"
    )

#Prints all elements of an array in one line.
def print_array(array):
    print(
        " ".join(
            str(value)
            for value in array
        )
    )
#instead of [1, 2, 3, 4] we get 1 2 3 4

#joins algorithms name to its function
def main():
    algorithms = {
        "INSERT-SORT": insertion_sort,
        "BUBBLE-SORT": bubble_sort
    }

    array_types = [
        "increasing",
        "random",
        "decreasing"
    ]

    active = {} #remembers what tests to run

    for algorithm_name in algorithms:
        for array_type in array_types:
            active[(algorithm_name, array_type)] = True

    exponent = 1
#exponentiation
    while True:
        if not any(active.values()):
            print(
                "\nEvery sorting test exceeded "
                "the 60-second limit."
            )
            break

        size = 10 ** exponent

        print()
        print("=" * 60)
        print(f"Size: 10^{exponent}")
        print("=" * 60)

        for array_type in array_types:
            print(f"\n{array_type}:")

            should_create_array = any(
                active[(algorithm_name, array_type)]
                for algorithm_name in algorithms
            )

            if should_create_array:
                original_array = create_array(
                    array_type,
                    size
                )
            else:
                original_array = None

            if size == 10 and original_array is not None:
                print("Before sorting:")
                print_array(original_array)

            for algorithm_name, sort_function in algorithms.items(): #Each created array is tested by both algorithms.
                key = (
                    algorithm_name,
                    array_type
                )

                if not active[key]:
                    print(f"{algorithm_name}: 60+")
                    continue

                elapsed_time, sorted_array = run_with_time_limit(
                    sort_function,
                    original_array,
                    TIME_LIMIT
                )

                if elapsed_time is None:
                    print(f"{algorithm_name}: 60+")
                    active[key] = False
                    continue

                print(
                    f"{algorithm_name}: "
                    f"{elapsed_time:.6f} s"
                )

                if size == 10:
                    print("After sorting:")
                    print_array(sorted_array)

        exponent += 1


if __name__ == "__main__":
    main()