from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.secret_key = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sailu66%2A@localhost/contact_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# model
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    address = db.Column(db.String(200))
    email_id = db.Column(db.String(120), unique=True)
    phone_number = db.Column(db.String(15))


# validation
def valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

@app.route('/')
def home():
    return render_template('index.html')


# create a record
@app.route('/add', methods=['POST'])
def add_contact():
    email = request.form.get('email')
    phone = request.form.get('phone')

    if not valid_email(email):
        flash("Invalid Email")
        return redirect('/')
    
    if not valid_phone(phone):
        flash("Phone number must be exactly 10 digits numbers")
        return redirect('/')

    if Contact.query.filter_by(email_id=email).first():
        flash("Email already exists")
        return redirect('/')

    new_contact = Contact(
        first_name=request.form.get('first_name'),
        last_name=request.form.get('last_name'),
        address=request.form.get('address'),
        email_id=email,
        phone_number=phone
    )

    db.session.add(new_contact)
    db.session.commit()

    flash("Contact created successfully ✅")
    return redirect('/display')


# display a records
@app.route('/display', methods=['GET'])
def display_contacts():
    contacts = Contact.query.all()
    return render_template('display.html', contacts=contacts)


# update a record
@app.route('/update/<int:id>', methods=['POST'])
def update_contact(id):
    contact = Contact.query.get(id)

    phone = request.form.get('phone')

    if not valid_phone(phone):
        flash("Phone number must be exactly 10 digits numbers")
        return redirect('/display')

    if contact:
        contact.first_name = request.form.get('first_name')
        contact.last_name = request.form.get('last_name')
        contact.address = request.form.get('address')
        contact.email_id = request.form.get('email')
        contact.phone_number = phone

        db.session.commit()
        flash("Contact Updated Successfully ✅")

    return redirect('/display')


# delete a record
@app.route('/delete/<int:id>', methods=['POST'])
def delete_contact(id):
    contact = Contact.query.get(id)

    if contact:
        db.session.delete(contact)
        db.session.commit()
        flash("Contact Deleted Successfully")

    return redirect('/display')


# run
if __name__ == '__main__':
    app.run(debug=True)