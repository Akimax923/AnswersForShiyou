def check_parentheses(string):
    stack = []
    unmatched_indices = []

    for index, char in enumerate(string):
        if char == '(':
            stack.append(index)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                unmatched_indices.append(index)
    
    while stack:
        unmatched_indices.append(stack.pop())
    
    result = [' '] * len(string)
    for index in unmatched_indices:
        if string[index] == '(':
            result[index] = 'x'
        elif string[index] == ')':
            result[index] = '?'
    print(unmatched_indices)
    return ''.join(result)

def main():
    #user_input = input("Please input some characters: ")
    # if user_input.lower() == 'exit':
    #     break

    print("Here is the result:")
    user_input = "bge)))))))))"
    print(f'{user_input}')
    print(f'{check_parentheses(user_input)}')

if __name__ == "__main__":
    main()
