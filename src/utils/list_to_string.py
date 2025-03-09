

# Converts list of numbers back to string of function
def convert_to_string(list_input):
    output = ""
    for i in range(len(list_input)):
        if list_input[i] != 0:
            if i == 0:
                output += str(list_input[i].real) + " + "
            elif list_input[i].real == 1.0:
                output += "x^" + str(i) + " + "
            else:
                output += str(list_input[i].real) + "x^" + str(i) + " + "
    output = output.rstrip(" + ")
    return output


def main():
    x = [0j, 0j, 0j, (1 + 0j)]
    print(convert_to_string(x))
    
    
if __name__ == "__main__":
    main()
