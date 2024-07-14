from queue_ll import Queue


def my_queue(capacity):
    queue = Queue(capacity=capacity)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    return queue
    #
    # while queue.count != 0:
    #     new_data = input("Enter Data:")
    #     queue.enqueue(new_data)
    #     queue.count -= 1
    # return queue


queue = my_queue(capacity=3)
print("is_empty", queue.is_empty())
print("is_full", queue.is_full())
print(queue.print_queue())
# print()
# print()
# print()

# print()
# print()
