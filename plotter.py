import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np
from heaviside import heaviside_function  # Assuming heaviside_function is defined in 'heaviside.py'
matplotlib.use('Agg')

def plot_newton_raphson(results):
    # Create a graph of x on the Y-axis and number of iterations on the X-axis
    plt.figure()
    plt.plot(range(1, len(results) + 1), results)
    plt.xlabel('Iterations')
    plt.ylabel('Root Value (x)')
    plt.title('Newton-Raphson Root Estimation')
    plt.grid(True)

    # Save the plot to a BytesIO buffer
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Encode the binary image data as base64
    img_data = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to release memory

    return img_data


def plot_heaviside(x_input):
    x = np.linspace(x_input - 10, x_input + 10, 1000)
    y = heaviside_function(x)

    plt.plot(x, y)
    plt.title('Heaviside Step Function')
    plt.xlabel('x')
    plt.ylabel('Heaviside(x)')
    plt.grid()
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)

    y_val = heaviside_function(x_input)
    plt.plot(x_input, y_val, 'ro')  # Plot the point for user input x_val

    plt.xlim(x_input - 10, x_input + 10)  # Adjusting x-axis limits

    # Highlight entered x value
    plt.scatter(x_input, heaviside_function(x_input), color='red', s=50, label=f'x={x_input}')
    plt.legend()

    # Save plot to BytesIO buffer
    img_buffer = BytesIO()
    plt.savefig(img_buffer, format='png')
    img_buffer.seek(0)

    # Encode binary image data as base64
    img_data = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

    plt.close()  # Close the plot to release memory

    return img_data
