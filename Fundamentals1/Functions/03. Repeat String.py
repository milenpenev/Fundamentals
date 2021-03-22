input_string = input()
printed_times = int(input())

def repeat_string(string, times):
    result = ''
    for number in range(0, times):
        result += input_string
    return result


print(repeat_string(input_string, printed_times))