from flask import Flask, render_template, request, jsonify
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/blog-details')
def blog_details():
    return render_template('blog-details.html')


@app.route('/service-details')
def service_details():
    return render_template('service-details.html')


@app.route('/portfolio-details')
def portfolio_details():
    return render_template('portfolio-details.html')


@app.route('/starter-page')
def starter_page():
    return render_template('starter-page.html')


@app.route('/api/contact', methods=['POST'])
def contact_form():
    """Handle contact form submissions"""
    try:
        data = request.form
        
        # Get form data
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')
        message = data.get('message')
        
        # Validation
        if not all([name, email, subject, message]):
            return jsonify({'success': False, 'message': 'Please fill all fields'}), 400
        
        # TODO: Add email sending functionality here
        # For now, just log it or store in database
        print(f"Contact form submission: {name} ({email}) - {subject}")
        
        return jsonify({
            'success': True, 
            'message': 'Your message has been sent successfully!'
        })
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.route('/api/newsletter', methods=['POST'])
def newsletter_form():
    """Handle newsletter subscriptions"""
    try:
        email = request.form.get('email')
        
        if not email:
            return jsonify({'success': False, 'message': 'Email is required'}), 400
        
        # TODO: Add email validation and storage
        print(f"Newsletter subscription: {email}")
        
        return jsonify({
            'success': True, 
            'message': 'Thank you for subscribing!'
        })
    
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
