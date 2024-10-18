
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# MySQL Configurations
app.config['MYSQL_HOST'] = 'http://localhost:3000.'
app.config['MYSQL_USER'] = 'rahul'
app.config['MYSQL_PASSWORD'] = 'yourpassword'
app.config['MYSQL_DB'] = 'testdb'

mysql = MySQL(app)

# Create a new registration
@app.route('/register', methods=['POST'])
def create_registration():
    try:
        details = request.json
        name = details['name']
        email = details['email']
        dob = details['dob'
        # Connect to MySQL and execute insert query
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Registration (name, email, dob) VALUES (%s, %s, %s)", (name, email, dob))
        mysql.connection.commit()

        return jsonify({'message': 'Registration created successfully'}), 201
    except MySQLdb.IntegrityError as e:
        return jsonify({'error': 'Email already exists'}), 409
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Get all registrations
@app.route('/registrations', methods=['GET'])
def get_registrations():
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM Registration")
        result = cursor.fetchall()
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


# Get a single registration by ID
@app.route('/registration/<int:id>', methods=['GET'])
def get_registration(id):
    try:
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("SELECT * FROM Registration WHERE id = %s", (id,))
        result = cursor.fetchone()
        if result:
            return jsonify(result), 200
        else:
            return jsonify({'message': 'Registration not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Update a registration by ID
@app.route('/registration/<int:id>', methods=['PUT'])
def update_registration(id):
    try:
        details = request.json
        name = details['name']
        email = details['email']
        dob = details['dob']

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE Registration SET name = %s, email = %s, dob = %s WHERE id = %s", (name, email, dob, id))
        mysql.connection.commit()
        if cursor.rowcount > 0:
            return jsonify({'message': 'Registration updated successfully'}), 200
        else:
            return jsonify({'message': 'Registration not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Delete a registration by ID
@app.route('/registration/<int:id>', methods=['DELETE'])
def delete_registration(id):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute("DELETE FROM Registration WHERE id = %s", (id,))
        mysql.connection.commit()
        if cursor.rowcount > 0:
            return jsonify({'message': 'Registration deleted successfully'}), 200
        else:
            return jsonify({'message': 'Registration not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
