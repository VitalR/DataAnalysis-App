import matplotlib.pyplot as plt
import seaborn as sns
import base64
from io import BytesIO


def get_image():
    # create a bytes buffer for the image to save
    buffer = BytesIO()
    # create the plot with the user of BytesIO as its 'file'
    plt.savefig(buffer, format='png')
    # set the cursor to the beginning of the stream
    buffer.seek(0)
    # retreive the entire content of the 'file'
    image_png = buffer.getvalue()

    graph = base64.b64encode(image_png)
    print(graph)
    print(type(graph))

    graph = graph.decode('utf-8')
    print(graph)

    # free the memory of the buffer
    buffer.close()

    return graph


def get_simple_plot(chart_type, *args, **kwargs):
    # https://matplotlib.org/tutorials/introductory/usage.html
    plt.switch_backend('AGG')
    fig = plt.figure(figsize=(10, 4))
    x = kwargs.get('x')
    y = kwargs.get('y')
    data = kwargs.get('data')

    if chart_type == 'bar plot':
        title = 'title'
        plt.title(title)
        plt.bar(x, y)
    elif chart_type == 'line plot':
        title = 'title'
        plt.title(title)
        plt.plot(x, y)
    else:
        title = 'title'
        plt.title(title)
        sns.countplot('name', data=data)
    plt.tight_layout()

    graph = get_image()
    return graph
