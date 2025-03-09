# FFT/IFFT RESTful API

This RESTful API performs function multiplication using the Fast Fourier Transform (FFT) and Inverse Fast Fourier Transform (IFFT). Users can send two input functions, and the API computes their product efficiently in the frequency domain using FFT, then transforms the result back using IFFT.

### Features:
- Accepts two input functions via API request
- Uses FFT for efficient function multiplication
- Returns the final result using IFFT
- Built for high-speed computation

--- 
### Directions for clean install
- Start the project by creating a virtual environment:
```python
$ python3 -m venv venv
```

- Activate the venv
```python
$ source venv/bin/activate
```

- Install dependencies
```python
$ pip3 install -r requirements.txt
```

- Run Project
```python
$ make run
```

- Deactivate the venv when done
```python
$ deactivate
```


---

### Directions for sending requests and receiving response from calculate microservice
- The API endpoint is designed to take in two input parameters input_1 and input_2 in the form of a poylnomial functions. The server will use the FFT/IFFT algorithm to multiply the functions and returns back a single poylnomial function in json format.
       
- A) Sending HTTP GET Request:
  - The API endpoint will allow for two parameters. input_1 and input_2.
     - NOTE: Only use functions of the variable "x" for both or else you will get a 400 status bad request.
     - NOTE: Only use polynomial functions or you will get a 400 status bad request.
     - NOTE: You can use "x^2" for poylnomials  or URL encodings "x%5E2".
     - NOTE: For polynomials like "x^2+3+2x^2" which is the equivalent of "x%5E2%2B3%2B2x%5E2" YOU MUST USE URL ENCODINGS FORM for longer inputs.
          - "^"     = %5E
          - " " = %20
          - "+"     = %2B
          - "-"      = %2D
          - "*"     = %2A
          (https://www.tutorialspoint.com/html/html_url_encoding.htm)
           
 -  Example 1:
     - curl --location 'http://localhost:63861/api/v1.0.0/calculate?input_1=x^3&input_2=x^5'
  
     - HTTP GET Request info:
         - Host: "http://localhost:63861"
         - Port: "63861"
         - Path: "/api/v1.0.0/calculate?"
         - Params: {
             - input_1: "x^3"
             - input_2: "x^5"}
         - url = 'http://localhost:63861/api/v1.0.0/calculate?input_1=x^3&input_2=x^5'
         - send_request(url)
           
 - Example 2:
     - curl --location 'http://localhost:63861/api/v1.0.0/calculate?input_1=x%5E2%2B2*x%5E5&input_2=x%5E5'
            
     - HTTP GET Request info:
         - Host: "http://flip1.engr.oregonstate.edu"
         - Port: "63861"
         - Path: "/api/v1.0.0/calculate?"
         - Params: {
             - input_1: "x%5E2%2B2*x%5E5"
             - input_2: "x%5E5"} 
         - url = 'http://localhost:63861/api/v1.0.0/calculate?input_1=x%5E2%2B2*x%5E5&input_2=x%5E5'
         - send_request(url)

- B) Receiving Reponse back:
 - Once a request is made to receive back the response use a variable and convert the data into json
 - Use a dictionary data structure and look for the "result" key to get back the value
 - Response example:
     - response = send_request(url)
     - response = response.json()
     - answer = response["result]
---
### Documentation
- API Documentation [Postman](https://documenter.getpostman.com/view/23973343/2sAYdoG8FL)  
- UML sequence diagram via [Lucidchart](https://lucid.app/lucidchart/4f7f271f-dfd9-4e4d-8098-d71a9c222b90/edit?invitationId=inv_58bf306c-930f-43db-af31-113b6fc7357f&page=0_0#)


