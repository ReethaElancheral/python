from flask import Flask

app = Flask(__name__)

# Home Route: Instructions and example banner link
@app.route('/')
def home():
    return """
    <html>
    <head><title>Text Banner Generator</title></head>
    <body>
        <h2>Enter your banner text</h2>
        <p>Try this sample: <a href='/banner/Hello'>/banner/Hello</a></p>
        <p>Or customize size like: <a href='/banner/Welcome/h3'>/banner/Welcome/h3</a></p>
    </body>
    </html>
    """

# Route for /banner/<text>
@app.route('/banner/<string:text>')
def banner(text):
    return f"""
    <html>
    <head><title>Banner: {text}</title></head>
    <body>
        <h1>{text}</h1>
        <p><a href="/">Back</a></p>
    </body>
    </html>
    """

# Route for /banner/<text>/<size>
@app.route('/banner/<string:text>/<string:size>')
def banner_with_size(text, size):
    # Validate size (h1 to h6), fallback to h3
    size = size.lower()
    if size not in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
        size = 'h3'

    return f"""
    <html>
    <head><title>Banner: {text}</title></head>
    <body>
        <{size}>{text}</{size}>
        <p><a href="/">Back</a></p>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)
