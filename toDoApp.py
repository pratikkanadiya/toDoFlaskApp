from flask import Flask, request, jsonify

app = Flask(__name__)

items = [
    {'id' : 1, 'name' : 'Item-1', 'description' : 'This is Item-1.'},
    {'id' : 2, 'name' : 'Item-2', 'description' : 'This is Item-2.'}
]

@app.route('/')
def homePage():
    return 'Welcome To Home Page Of To Do List App.'

# get : Retrive all the items
@app.route('/items', methods = ['GET'])
def get_items():
    return jsonify(items)

# Get : Retrive a specific items by Id
@app.route('/items/<int:item_id>', methods = ['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error" : "item is not found"})
    return jsonify(item)

# Post : Create New Items
@app.route('/items', methods = ['POST'])
def create_item():
    if not request.is_json or not 'name' in request.json:
        return jsonify({"error" : "item is not found"})
    new_item = {
        "id" : items[-1]["id"] + 1 if items else 1,
        "name" : request.json['name'],
        "description" : request.json['description']
    }
    items.append(new_item)
    return jsonify(new_item)

# Update an existing items
@app.route('/items/<int:item_id>', methods = ['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item is None:
        return jsonify({"error" : "item is not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# Delete an existing items
@app.route('/items/<int:item_id>', methods = ['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"result" : "Item Deleted"})

if __name__ == '__main__':
    app.run()