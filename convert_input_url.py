def get_input_from_url(url_input):
    output = url_input[8:]
    return output

def main():
    x = "input_1=x^2+2*x^5"
    print(get_input_from_url(x))
    
    
if __name__ == "__main__":
    main()
