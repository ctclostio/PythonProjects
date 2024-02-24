# A script by Clayton Clostio
from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import os

# Initialize Flask app
app = Flask(__name__)
# Configure secret key and database URI
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize Flask-Login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model definition
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    # Set user password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Check user password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# User loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Index route
@app.route('/')
def index():
    return render_template('index.html')

# User registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Hash password
        hashed_password = generate_password_hash(password, method='sha256')

        # Create new user instance
        new_user = User(username=username, email=email)
        new_user.set_password(password)

        # Add new user to database
        db.session.add(new_user)
        db.session.commit()

        # Redirect to login page
        return redirect(url_for('login'))
    return render_template('register.html')

# User login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Authenticate user
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('profile'))
        else:
            return 'Invalid username or password'
    return render_template('login.html')

# User profile route
@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.username)

# User logout route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

# Main entry point
if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
