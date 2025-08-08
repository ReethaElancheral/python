from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for feedbacks
feedback_list = []

# Route: Show feedback form
@app.route('/feedback-form')
def feedback_form():
    return """
    <html>
    <head><title>Feedback Form</title></head>
    <body>
        <h2>Customer Feedback Form</h2>
        <form method="POST" action="/submit-feedback">
            <label>Name:</label><br>
            <input type="text" name="name" required><br><br>

            <label>Email:</label><br>
            <input type="email" name="email" required><br><br>

            <label>Message:</label><br>
            <textarea name="message" rows="4" cols="40" required></textarea><br><br>

            <input type="submit" value="Submit Feedback">
        </form>
    </body>
    </html>
    """

# Route: Handle POST and redirect
@app.route('/submit-feedback', methods=['POST'])
def submit_feedback():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")

    feedback = {
        "name": name,
        "email": email,
        "message": message
    }

    feedback_list.append(feedback)
    return redirect(url_for('thank_you'))

# Route: Thank you page
@app.route('/thank-you')
def thank_you():
    return """
    <html>
    <head><title>Thank You</title></head>
    <body>
        <h2>Thank you for your feedback!</h2>
        <a href="/feedbacks">View all feedbacks</a>
    </body>
    </html>
    """

# Route: Filter feedbacks using query parameter
@app.route('/feedbacks')
def view_feedbacks():
    user = request.args.get('user')
    filtered = feedback_list

    if user:
        filtered = [fb for fb in feedback_list if fb['name'].lower() == user.lower()]

    result_html = "<h2>All Feedbacks</h2>"
    for fb in filtered:
        result_html += f"""
        <hr>
        <p><b>Name:</b> {fb['name']}</p>
        <p><b>Email:</b> {fb['email']}</p>
        <p><b>Message:</b> {fb['message']}</p>
        """

    return result_html

# Route: Dynamic route showing user-specific data
@app.route('/user/<username>')
def user_feedback(username):
    user_fbs = [fb for fb in feedback_list if fb['name'].lower() == username.lower()]

    if not user_fbs:
        return f"<h3>No feedback found for {username}</h3>"

    html = f"<h2>Feedback from {username}</h2>"
    for fb in user_fbs:
        html += f"""
        <hr>
        <p><b>Email:</b> {fb['email']}</p>
        <p><b>Message:</b> {fb['message']}</p>
        """
    return html

if __name__ == '__main__':
    app.run(debug=True)
