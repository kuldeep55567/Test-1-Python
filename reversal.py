def reverse_string(input_string):
    return input_string[: :-1]

string = input("Type a String : ")
reversed_str = reverse_string(string)
print("Reversed String is ",reversed_str)