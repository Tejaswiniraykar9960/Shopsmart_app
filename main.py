from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from routes.customer_routes import customer_bp
from routes.product_routes import product_bp
from routes.transaction_routes import transaction_bp
from models.customer import db  # Shared DB instance

app = Flask(__name__)

# MySQL connection (with URL-encoded @ as %40)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:teju%40123@localhost/shopsmart'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)


# Create all tables once
with app.app_context():
    db.create_all()

# Welcome route
@app.route('/')
def welcome():
    return jsonify({'message': 'Welcome to SHOPSMART API'}), 200

# Register Blueprints
app.register_blueprint(customer_bp, url_prefix='/customers')
app.register_blueprint(product_bp, url_prefix='/products')
app.register_blueprint(transaction_bp, url_prefix='/transactions')

if __name__ == '__main__':
    app.run(debug=True)

