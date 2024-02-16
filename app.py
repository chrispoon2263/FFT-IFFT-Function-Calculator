from flask import Flask, render_template, request, redirect, url_for, flash, make_response
import urllib.parse
from FFT import multiply_polynomials
from create_graph import save_graph
from roots_unity_graph import create_roots_unity_graph, get_x_y, get_point_representation
from string_to_list import convert_to_list
from list_to_string import convert_to_string
from convert_input_url import get_input_from_url

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'



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
        except:
            flash("Not a poylnomial function. Please enter something like x + 2x + 3x^2. Avoid ln, sin, cos, tan, log, or e^() type syntax", "info")
            return render_template('index.html')

        return redirect(url_for("result", f_input_value=f_input_value, g_input_value=g_input_value, f_point_rounded=f_point_rounded, g_point_rounded=g_point_rounded, h_output=h_output, h_point_rounded=h_point_rounded))
    else:
        return render_template('index.html')


@app.route('/result')
def result():
    f_input_value = request.args.get('f_input_value', None)
    g_input_value = request.args.get('g_input_value', None)
    f_point_rounded = request.args.get('f_point_rounded', None)
    g_point_rounded = request.args.get('g_point_rounded', None)
    h_point_rounded = request.args.get('h_point_rounded', None)
    h_output = request.args.get('h_output', None)
    return render_template('result.html', f_input_value=f_input_value, g_input_value=g_input_value, f_point_rounded=f_point_rounded, g_point_rounded=g_point_rounded, h_output=h_output, h_point_rounded=h_point_rounded)


@app.route('/about_me/')
def about_me():
    return render_template('/about_me.html')



# http://127.0.0.1:5000/api/v1.0.0/calculate/input_1=x^2%2B2*x^5&input_2=x^5
@app.route('/api/v1.0.0/calculate/<input1>&<input2>')
def calculate(input1, input2):
    try:
        # Grab inputs from user URL
        f_input_value = get_input_from_url(input1)
        g_input_value = get_input_from_url(input2)

        # Convert URL input1 and inpu2 to list inputs into f_list and g_list for FFT algorithm
        f_list = convert_to_list(f_input_value)
        g_list = convert_to_list(g_input_value)

        # Run FFT algorithm
        f_point, g_point, h_point, h_list = multiply_polynomials(f_list, g_list, 10)

        # Convert h(x) back to poylnomial reprsentation
        h_output = convert_to_string(h_list)

        return make_response({'result': h_output}, 200)
    except:
        return make_response({'result': "Bad query"}, 400)

if __name__ == "__main__":
    app.run(debug=True, port=63861)
