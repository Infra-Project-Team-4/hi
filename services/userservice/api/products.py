from flask import Blueprint, jsonify
from services.product_service import PRODUCTS

products_bp = Blueprint("products", __name__)


@products_bp.route("/products", methods=["GET"])
def get_products():
    # Dictionary(Mock DB)를 리스트 형태로 변환
    product_list = []

    for barcode, product in PRODUCTS.items():
        product_list.append({
            "barcode": barcode,
            "name": product["name"],
            "stock": product["stock"],
            "location": product["location"]
        })

    return jsonify(product_list)
