# FlexStart - Flask Version

Your website has been successfully converted from static HTML to Flask!

## Project Structure

```
FlexStart/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── .flaskenv              # Flask environment configuration
├── templates/             # Jinja2 templates
│   ├── base.html          # Base template with header/footer
│   ├── index.html         # Home page
│   ├── blog.html          # Blog listing
│   ├── blog-details.html  # Blog post detail
│   ├── portfolio-details.html
│   ├── service-details.html
│   └── starter-page.html
├── static/                # Static files (CSS, JS, images)
│   ├── css/
│   ├── js/
│   ├── img/
│   ├── scss/
│   └── vendor/
└── forms/                 # Legacy PHP forms (can be removed)
```

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Flask Development Server

```bash
python app.py
```

The application will start at `http://localhost:5000`

## Key Features Implemented

✅ **Routing**: All pages have Flask routes configured
- `/` - Home page
- `/blog` - Blog listing
- `/blog-details` - Blog detail page
- `/service-details` - Service detail page
- `/portfolio-details` - Portfolio detail page
- `/starter-page` - Template page

✅ **Forms**: Contact and Newsletter forms now use Flask API endpoints
- POST `/api/contact` - Handle contact form submissions
- POST `/api/newsletter` - Handle newsletter subscriptions

✅ **Template System**: Jinja2 templates with base template inheritance
- Uses `{{ url_for() }}` for dynamic URL generation
- Uses `{{ static() }}` for static file references
- Maintains all original Bootstrap styling and functionality

## Next Steps

### 1. Configure Email Sending (Optional)
In `app.py`, update the contact and newsletter form handlers to send actual emails. You can use `flask-mail` or `smtplib`:

```bash
pip install flask-mail
```

### 2. Add Database Support (Optional)
To store form submissions:

```bash
pip install flask-sqlalchemy
```

### 3. Environment Variables
Update `.flaskenv` with your configuration:
```
FLASK_APP=app.py
FLASK_ENV=development
FLASK_DEBUG=1
```

For production:
```
FLASK_ENV=production
FLASK_DEBUG=0
SECRET_KEY=your-secret-key-here
```

### 4. Static File Handling
The `static/` folder is automatically served by Flask in development. For production, use a reverse proxy like Nginx or configure static file serving with Whitenoise:

```bash
pip install whitenoise
```

## Common Issues & Solutions

**Issue**: Templates not found
- **Solution**: Ensure the `templates/` folder exists in the same directory as `app.py`

**Issue**: Static files (CSS/JS) not loading
- **Solution**: Verify the `static/` folder exists with proper subdirectories

**Issue**: Forms not submitting
- **Solution**: Check browser console for AJAX errors, ensure `url_for()` functions generate correct URLs

## Deployment

### For Production:

1. Install a production WSGI server:
```bash
pip install gunicorn
```

2. Run with Gunicorn:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

3. Use Nginx or Apache as a reverse proxy

4. Set environment variables:
```bash
export FLASK_ENV=production
export SECRET_KEY=your-very-secure-secret-key
```

## Support

For Flask documentation, visit: https://flask.palletsprojects.com/

For Jinja2 template documentation: https://jinja.palletsprojects.com/

Enjoy your Flask-powered website!
