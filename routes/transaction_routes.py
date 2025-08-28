from flask import Blueprint, request, jsonify
from models.transaction import Transaction
from models.customer import db

transaction_bp = Blueprint('transaction_bp', __name__)

@transaction_bp.route('/', methods=['POST'])
def add_transaction():
    data = request.get_json()
    transaction = Transaction(customer_id=data['customer_id'], product_id=data['product_id'], quantity=data['quantity'])
    db.session.add(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction added'}), 201

@transaction_bp.route('/', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    return jsonify([
        {'id': t.id, 'customer_id': t.customer_id, 'product_id': t.product_id, 'quantity': t.quantity}
        for t in transactions
    ])
