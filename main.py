from flask import Flask, render_template, request, redirect, url_for
from FFT import multiply_polynomials
from create_graph import save_graph
from roots_unity_graph import create_roots_unity_graph, get_x_y, get_point_representation
from string_to_list import convert_to_list
from list_to_string import convert_to_string

app = Flask(__name__)


@app.route('/',  methods=["POST", "GET"])
def index():
    if request.method == "POST":
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


if __name__ == "__main__":
    app.run(debug=True)
