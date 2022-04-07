from flask import Blueprint
from controllers.UserController import bakeryinventory, addtomenu, itemavailablty, removeitem #itemincr_decrement,notavailable
user_bp = Blueprint('user_bp', __name__)
user_bp.route('/oven', methods=['GET'])(bakeryinventory)
user_bp.route('/oven', methods=['POST'])(addtomenu)
user_bp.route('/oven/<item>', methods=['GET'])(itemavailablty)
user_bp.route('/oven/<item>', methods=['DELETE'])(removeitem)
