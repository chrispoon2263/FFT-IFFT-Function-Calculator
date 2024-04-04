from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify
from FFT import multiply_polynomials
from create_graph import save_graph
from roots_unity_graph import create_roots_unity_graph, get_x_y, get_point_representation
from string_to_list import convert_to_list
from list_to_string import convert_to_string
import requests

# Flask Settings
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# Home page with calculate function
@app.route('/',  methods=["POST", "GET"])
def index():
    if request.method == "POST":
        try:
            # grab inputs from frontend using dictionary notation
            f_input_value = request.form["f_input_value"]
            g_input_value = request.form["g_input_value"]

            # Sanitize inputs to a list of ints
            f_list = convert_to_list(f_input_value)
            g_list = convert_to_list(g_input_value)
            
            # create graph_1 and graph_2
            save_graph("static/images/graph_1.png", f_list)
            save_graph("static/images/graph_2.png", g_list)
            
            # Run FFT algorithm
            f_point, g_point, h_point, h_list = multiply_polynomials(f_list, g_list, 10)

            # Create Roots of Unity Graph
            create_roots_unity_graph("static/images/roots_unity_graph.png", h_point)

            # Create cleaner version of h(x) point representation
            h_x, h_y = get_x_y(h_point)
            h_point_rounded = str(get_point_representation(h_x, h_y))

            # convert f(x) to point representation
            f_x, f_y = get_x_y(f_point)
            f_point_rounded = str(get_point_representation(f_x, f_y))

            # convert g(x) to point representation
            g_x, g_y = get_x_y(g_point)
            g_point_rounded = str(get_point_representation(g_x, g_y))
            
            
            # Convert h(x) back to poylnomial reprsentation
            h_output = convert_to_string(h_list)

            # Create h(x) graph
            h_graph = convert_to_list(h_output)
            save_graph("static/images/graph_3.png", h_graph)
            return redirect(url_for("result", f_input_value=f_input_value, \
                                              g_input_value=g_input_value, \
                                              f_point_rounded=f_point_rounded, \
                                              g_point_rounded=g_point_rounded, \
                                              h_output=h_output, \
                                              h_point_rounded=h_point_rounded))
        except:
            flash("Not a poylnomial function. Please enter something like x + 2x + 3x^2. Avoid ln, sin, cos, tan, log, or e^() type syntax", "info")
            return render_template('index.html')
    # default get request: go to home page
    else:
        return render_template('index.html')


# Sends a request to get to partner's Microservice Server and gets back two input functions in json format
@app.route('/proxyEndpoint', methods=['GET'])
def proxy():
    # Send response to get 2 random functions from microservice at the localport
    print("")
    print("********************************************")
    print("Asking partner microservice for 2 functions")
    print("Waiting...")
    response = requests.get('http://localhost:65398')

    if response.status_code == 200:
        data = response.json()
        input_1 = data['input_1']
        input_2 = data['input_2'] 
        print("")
        
        print("Received input 1: " + str(input_1))
        print("Received input 2: " + str(input_2))
        print("********************************************")
        return jsonify(response.json())
    else:
        print("Could not receive values")
        return response.status_code == 400; 


# Clicking the calculate button will send you to this route
@app.route('/result')
def result():
    f_input_value = request.args.get('f_input_value', None)
    g_input_value = request.args.get('g_input_value', None)
    f_point_rounded = request.args.get('f_point_rounded', None)
    g_point_rounded = request.args.get('g_point_rounded', None)
    h_point_rounded = request.args.get('h_point_rounded', None)
    h_output = request.args.get('h_output', None)
    return render_template('result.html', f_input_value=f_input_value, \
                                          g_input_value=g_input_value, \
                                          f_point_rounded=f_point_rounded, \
                                          g_point_rounded=g_point_rounded, \
                                          h_output=h_output,\
                                          h_point_rounded=h_point_rounded)


# About me Route
@app.route('/about_me/')
def about_me():
    return render_template('/about_me.html')


# Internal Rest API 
# http://127.0.0.1:63861/api/v1.0.0/calculate?input_1=x^2%2B2*x^5&input_2=x^5
@app.route('/api/v1.0.0/calculate')
def calculate():
    try:
        # Grab inputs from user URL
        print("")
        print("********************************************")
        print("Server Listening...")
        input1 = request.args.get("input_1")
        input2 = request.args.get("input_2")
        print("Inputs received:")
        print("    Input 1: " + input1)
        print("    Input 2: " + input2)
        print("")

        # Convert URL input1 and inpu2 to list inputs into f_list and g_list for FFT algorithm
        print("Microservice is calculating...")
        f_list = convert_to_list(input1)
        g_list = convert_to_list(input2)

        # Run FFT algorithm
        f_point, g_point, h_point, h_list = multiply_polynomials(f_list, g_list, 10)

        # Convert h(x) back to poylnomial reprsentation
        h_output = convert_to_string(h_list)
        print("    Answer: " + h_output)

        print("")
        print("Sending Response...")
        print("    Response: " + str({'result': h_output}))
        print("********************************************")
        return make_response({'result': h_output}, 200)
    
    except:
        # Send status code 400 if bad query
        print("BAD INPUTS")
        print("********************************************")
        return make_response({'result': "Bad query"}, 400)


if __name__ == "__main__":
    app.run(debug=True, port=63861)
