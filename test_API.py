import urllib.parse
import requests

def make_url_string(host, path, port, input_1, input_2):
    input_1_str = make_input(input_1, 1)
    input_2_str = make_input(input_2, 2)
    output = host + ":" + str(port) + path + input_1_str + "&" + input_2_str
    output = host + ":" + str(port) + path + input_1_str + "&" + input_2_str
    return output

def make_input(input_string, input_string_num):
    return "input_" + str(input_string_num) + "=" + urllib.parse.quote(input_string)


def main():
    #host = "http://flip1.engr.oregonstate.edu"
    host = "http://localhost"
    path = "/api/v1.0.0/calculate?"
    port = 63861
    input_1 = "x^2 + 2"
    input_2 = "x^5"
    url = make_url_string(host, path, port, input_1, input_2)
    
    # Send Request
    print("")
    print("**************************************")
    print("Test Microservice starting...")
    print("Sending inputs to server:")
    print("URL: ", url)
    print("    Input 1: " + input_1)
    print("    Input 2: " + input_2)
    print("")
    response = requests.get(url)

    # Get Response
    print("Server has responded back with: ")
    print("    Response: " + str(response.json()))
    print("**************************************")
    print("")


if __name__ == "__main__":
    main()
