from flask import Flask, request, jsonify
import uuid
from datetime import datetime
import math

app = Flask(__name__)

receipts = {}

def calculate_points(receipt):
    points = 0

    retailer = receipt.get("retailer", "")
    points += sum(c.isalnum() for c in retailer)

    total = float(receipt.get("total", 0))
    if total.is_integer():
        points += 50


    if total % 0.25 == 0:
        points += 25


    items = receipt.get("items", [])
    points += (len(items) // 2) * 5

   
    for item in items:
        desc = item.get("shortDescription", "")
        price = float(item.get("price", 0))
        if len(desc.strip()) % 3 == 0:
            points += math.ceil(price * 0.2) 
    
    purchase_date = datetime.strptime(receipt.get("purchaseDate", ""), "%Y-%m-%d")
    if purchase_date.day % 2 != 0:
        points += 6

    purchase_time = datetime.strptime(receipt.get("purchaseTime", ""), "%H:%M").time()
    if datetime.strptime("14:00", "%H:%M").time() <= purchase_time <= datetime.strptime("16:00", "%H:%M").time():
        points += 10
    
    return points

@app.route('/receipts/process', methods=['POST'])
def process_receipt():
    try:
        receipt = request.json

        if not receipt or not all(key in receipt for key in ["retailer", "purchaseDate", "purchaseTime", "items", "total"]):
            return jsonify({"error": "Please verify input."}), 400

        receipt_id = str(uuid.uuid4())
        points = calculate_points(receipt)

        receipts[receipt_id] = {
            "receipt": receipt,
            "points": points
        }

        return jsonify({"id": receipt_id}), 200
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred: " + str(e)}), 400

@app.route('/receipts/<receipt_id>/points', methods=['GET'])
def get_points(receipt_id):
    receipt_data = receipts.get(receipt_id)
    if not receipt_data:
        return jsonify({"error": "No receipt found for that ID."}), 404

    return jsonify({"points": receipt_data["points"]}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)