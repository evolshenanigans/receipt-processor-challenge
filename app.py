from flask import Flask, request, jsonify
import uuid
import math
from datetime import datetime

app = Flask(__name__)

receipts_db = {}

def calculate_points(receipt):
    points = 0
    points += sum(char.isalnum() for char in receipt['retailer'])
    
    total = float(receipt['total'])
    if total == int(total):
        points += 50
    
    if total % 0.25 == 0:
        points += 25
    
    num_items = len(receipt['items'])
    points += (num_items // 2) * 5
    
    for item in receipt['items']:
        desc = item['shortDescription'].strip()
        price = float(item['price'])
        if len(desc) % 3 == 0:
            points += math.ceil(price * 0.2)
    
    if total > 10.00:
        points += 5
    
    purchase_date = datetime.strptime(receipt['purchaseDate'], '%Y-%m-%d')
    if purchase_date.day % 2 != 0:
        points += 6
    
    purchase_time = datetime.strptime(receipt['purchaseTime'], '%H:%M').time()
    if datetime.strptime('14:00', '%H:%M').time() < purchase_time < datetime.strptime('16:00', '%H:%M').time():
        points += 10
    
    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    receipt = request.json
    receipt_id = str(uuid.uuid4())
    points = calculate_points(receipt)
    receipts_db[receipt_id] = points
    return jsonify({"id": receipt_id})

@app.route('/receipts/<id>/points', methods=['GET'])
def get_points(id):
    points = receipts_db.get(id)
    if points is None:
        return jsonify({"error": "Receipt not found"}), 404
    return jsonify({"points": points})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)