import multiprocessing
import random
import time


TIME_LIMIT = 60.0


def insertion_sort(array):
    """
    Sorts the array using insertion sort.
    """
    for i in range(1, len(array)):
        current_value = array[i]
        j = i - 1

        while j >= 0 and array[j] > current_value:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = current_value

    return array


def bubble_sort(array):
    """
    Sorts the array using bubble sort.
    """
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

    return array


def sorting_worker(sort_function, array, result_queue):
    """
    Runs a sorting algorithm and measures its execution time.
    """
    start_time = time.perf_counter()

    sorted_array = sort_function(array)

    end_time = time.perf_counter()
    elapsed_time = end_time - start_time

    result_queue.put(
        (elapsed_time, sorted_array)
    )


def run_with_time_limit(
    sort_function,
    array,
    time_limit=60.0
):
    """
    Runs a sorting algorithm in a separate process.

    If the algorithm exceeds the time limit,
    the process is terminated.
    """
    result_queue = multiprocessing.Queue()

    process = multiprocessing.Process(
        target=sorting_worker,
        args=(
            sort_function,
            array.copy(),
            result_queue
        )
    )

    process.start()
    process.join(timeout=time_limit)

    if process.is_alive():
        process.terminate()
        process.join()

        return None, None

    if result_queue.empty():
        return None, None

    elapsed_time, sorted_array = result_queue.get()

    return elapsed_time, sorted_array


def create_array(array_type, size):
    """
    Creates an increasing, random or decreasing array.
    """
    if array_type == "increasing":
        return list(range(1, size + 1))

    if array_type == "random":
        array = list(range(1, size + 1))
        random.shuffle(array)
        return array

    if array_type == "decreasing":
        return list(range(size, 0, -1))

    raise ValueError(
        f"Unknown array type: {array_type}"
    )


def print_array(array):
    """
    Prints all elements of an array in one line.
    """
    print(
        " ".join(
            str(value)
            for value in array
        )
    )


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

    active = {}

    for algorithm_name in algorithms:
        for array_type in array_types:
            active[(algorithm_name, array_type)] = True

    exponent = 1

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

            for algorithm_name, sort_function in algorithms.items():
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