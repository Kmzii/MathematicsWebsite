from flask import Flask, request, render_template, jsonify
from heaviside import heaviside_function
from plotter import plot_newton_raphson  # Import the plot_newton_raphson function
from plotter import plot_heaviside
from newton_raphson import calculate_root  # Assuming calculate_root is defined in 'newton_raphson.py'
from waitress import serve

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/newton_raphson.html')
def newton_raphson_page():
    return render_template('newton_raphson.html')


@app.route('/heaviside.html')
def heaviside_page():
    return render_template('heaviside.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/calculate', methods=['POST'])
def calculate_root_route():
    data = request.get_json()

    # Ensure required fields are present in the request
    if 'function' not in data or 'guess' not in data or 'iterations' not in data:
        return jsonify({'error': 'Missing data in the request'})

    try:
        function_str = data['function']
        initial_guess = data['guess']
        iterations = data['iterations']

        results = calculate_root(function_str, initial_guess, iterations)

        # Get plot data from the separate plotting module
        img_base64 = plot_newton_raphson(results)

        results_str = [str(result) for result in results]

        return jsonify({'result': results_str, 'plot': img_base64})

    except ValueError as ve:
        return jsonify({'error': 'Invalid input. Check your function or initial guess.'})

    except ZeroDivisionError as ze:
        return jsonify({'error': 'Division by zero error. Check your function or initial guess.'})

    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/calculate_heaviside', methods=['POST'])
def calculate_heaviside():
    data = request.get_json()
    x = float(data['x'])

    # Calculate Heaviside function
    result = heaviside_function(x)

    # Get plot data from the separate plotting module with adjusted x-axis limits
    img_base64 = plot_heaviside(x)

    return jsonify({'result': result, 'plot': img_base64})


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
