from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory warranty database (for demonstration)
warranty_data = {
    "ABC123": {"product": "Laptop", "valid_till": "2026-01-01"},
    "XYZ789": {"product": "Smartphone", "valid_till": "2025-12-31"},
    "LMN456": {"product": "Washing Machine", "valid_till": "2027-05-10"}
}

@app.route('/')
def home():
    return '''
        <h2>Product Warranty Checker</h2>
        <ul>
            <li><a href="/check-warranty">Check Warranty</a></li>
            <li><a href="/warranty/Laptop">Warranty by Product</a></li>
        </ul>
        <hr>
    '''

@app.route('/check-warranty', methods=['GET', 'POST'])
def check_warranty():
    if request.method == 'POST':
        serial = request.form['serial']
        return redirect(url_for('warranty_result', serial=serial))
    
    return '''
        <h2>Check Warranty</h2>
        <form method="POST">
            <label>Enter Product Serial Number:</label><br>
            <input type="text" name="serial" required><br><br>
            <input type="submit" value="Check Warranty">
        </form>
        <a href="/">Back to Home</a>
        <hr>
    '''

@app.route('/result')
def warranty_result():
    serial = request.args.get('serial')
    info = warranty_data.get(serial.upper())

    if info:
        return f'''
            <h2>Warranty Information</h2>
            <p><strong>Product:</strong> {info["product"]}</p>
            <p><strong>Serial:</strong> {serial.upper()}</p>
            <p><strong>Warranty Valid Till:</strong> {info["valid_till"]}</p>
            <a href="/">Back to Home</a>
            <hr>
        '''
    else:
        return f'''
            <h2>No Warranty Information Found</h2>
            <p>Serial: {serial.upper()}</p>
            <a href="/check-warranty">Try Again</a>
            <hr>
        '''

@app.route('/warranty/<product>')
def product_warranty(product):
    matched = [f"<li>{serial} (valid till {data['valid_till']})</li>" 
               for serial, data in warranty_data.items() 
               if data['product'].lower() == product.lower()]

    if matched:
        return f'''
            <h2>Warranty Details for Product: {product.title()}</h2>
            <ul>{''.join(matched)}</ul>
            <a href="/">Back to Home</a>
            <hr>
        '''
    else:
        return f'''
            <h2>No warranty records found for: {product}</h2>
            <a href="/">Back to Home</a>
            <hr>
        '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)
