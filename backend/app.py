# Adding, Deleting, & Fetching firewall rules

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Store firewall rules in-memory
firewall_rules = []


# Endpoint to add a new firewall rule
@app.route("/add_rule", methods=["POST"])
def add_rule():
    data = request.get_json()
    firewall_rules.append(data)
    return jsonify({"msg": "Rule added successfully", "rules": firewall_rules})


# Endpoint to get all firewall rules
@app.route("/get_rules", methods=["GET"])
def get_rules():
    return jsonify(firewall_rules)


# Endpoint to delete a firewall rule by index
@app.route("/delete_rule/<int:index>", methods=["DELETE"])
def delete_rule(index):
    if 0 <= index < len(firewall_rules):
        del firewall_rules[index]
        return jsonify({"msg": "Rule deleted successfully", "rules": firewall_rules})
    else:
        return jsonify({"msg": "Invalid index"}), 400


if __name__ == "__main__":
    app.run(debug=True)
