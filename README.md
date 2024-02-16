# CS_361_project

- Directions for clean install

    - Start the project by creating a virtual environment:
        - $ python3 -m venv venv

    - Activate the venv
        - $ source venv/bin/activate
        - (hint use an alias to activate)

    - Install dependencies
        - $ pip3 install -r requirements.txt

    - Run Project
        - $ make run

    - Deactivate the venv when done
        - $ deactivate

- Directions for sending requests and receiving response from calculate microservice
    - The API endpoint is designed to take in two input paramters input_1 and input_2 in the form of a poylnomial functions. The server will use the FFT/IFFT algorithm to muliply the functions and returns back a single poylnomial function in json format.
    - Sending GET Request:
        - Curl example 1: 
            - curl --location 'http://flip1.engr.oregonstate.edu:63861/api/v1.0.0/calculate/input_1=x^3&input_2=x^5'
        - Curl example 2:
            - curl --location 'http://flip1.engr.oregonstate.edu:63861/api/v1.0.0/calculate/input_1=x^2+2 - x^3&input_2=x%5E5'
    -      
    - UML sequence diagram via Lucidchart 
        - https://lucid.app/lucidchart/4f7f271f-dfd9-4e4d-8098-d71a9c222b90/edit?viewport_loc=-73%2C1219%2C3602%2C1786%2C0_0&invitationId=inv_58bf306c-930f-43db-af31-113b6fc7357f
