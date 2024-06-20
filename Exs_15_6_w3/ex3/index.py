from stack import Stack


def my_stack(capacity):
    stack = Stack(capacity=capacity)
    while stack.count != 0:
        new_data = input("Enter Data:")
        stack.push(new_data)
        stack.count -= 1
    return stack


current_stack = my_stack(3)

print("is_empty", current_stack.is_empty())
print("is_full", current_stack.is_full())

temp = current_stack.pop()
print("temp", temp)
print("push", current_stack.push(temp))
print("top", current_stack.top())
