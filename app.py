from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Helper functions to read and write JSON data
def read_data(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def write_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def home():
    doctors = read_data('data/doctors.json')
    return render_template('index.html', doctors=doctors)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "phone": request.form['phone'],
            "message": request.form['message']
        }
        contacts = read_data('data/contacts.json')
        contacts.append(data)
        write_data('data/contacts.json', contacts)
        return redirect(url_for('home'))
    return render_template('contact.html')

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    data = {
        "name": request.form['name'],
        "email": request.form['email'],
        "phone": request.form['phone'],
        "description": request.form['description']
    }
    appointments = read_data('data/appointments.json')
    appointments.append(data)
    write_data('data/appointments.json', appointments)
    return redirect(url_for('home'))

@app.route('/admin')
def admin():
    appointments = read_data('data/appointments.json')
    doctors = read_data('data/doctors.json')
    return render_template('admin.html', appointments=appointments, doctors=doctors, enumerate=enumerate)

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    data = {
        "name": request.form['name'],
        "designation": request.form['designation'],
        "photo": request.form['photo']
    }
    doctors = read_data('data/doctors.json')
    doctors.append(data)
    write_data('data/doctors.json', doctors)
    return redirect(url_for('admin'))

@app.route('/delete_appointment/<int:index>', methods=['POST'])
def delete_appointment(index):
    appointments = read_data('data/appointments.json')
    if 0 <= index < len(appointments):
        appointments.pop(index)
        write_data('data/appointments.json', appointments)
    return redirect(url_for('admin'))

@app.route('/delete_doctor/<int:index>', methods=['POST'])
def delete_doctor(index):
    doctors = read_data('data/doctors.json')
    if 0 <= index < len(doctors):
        doctors.pop(index)
        write_data('data/doctors.json', doctors)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(debug=True)
