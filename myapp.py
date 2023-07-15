from flask import Flask, render_template, request, flash
from flask import Flask, render_template, request, redirect, session
from flask import session, redirect, url_for, render_template
from flask import flash, redirect, render_template, request, url_for
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo

from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
from pymongo import MongoClient
import random
import string
import pymongo
import json
import spacy
import os
from datetime import datetime
app = Flask(__name__, static_folder='static')
# configure the MongoDB connections
app.config['SECRET_KEY'] = 'your_secret_key'  # Set a secret key for session security
app.config['MONGO_URI'] = 'mongodb://localhost:27017/medical11'  # Update with your MongoDB URI
mongo = PyMongo(app)
bcrypt = Bcrypt(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['medical11']
collection = db['abc11']
colors = {
        "MICROORGANISM": "#D291BC",
        "CELL": "#39CCCC",
        "GENE": "#2ECC40",
        "COMPOUND": "#6B3FA0",
        "DIESEASE": "#FF4136",
        "SYMPTOMS": "#FF851B",
        "ORG": "#0074D9",
        "PROTEIN": "#B10DC9",
        "AGENT": "#001F3F",
        "MEDICINE": "#AF7AC5",
        "TREATMENT": "#F012BE",
        "TOOL": "#B7950B",
        "PERCENTAGE": "#FF00FF",
        "ENZYME": "#3D9970",
        "NUCLEIC_ACID": "#FFC125",
        "CARDINAL": "#AAAAAA",
        "DATE": "#001F3F",
        "LOC": "#444444",
        "CONDITION": "#FFDAB9",
        "AMINO_ACID": "#FFDB58"
    }

@app.route('/')
@app.route('/index.html')
def index():
    
    username = session.get('username')
    # get the total number of articles
    total_articless = db.abc11.count_documents({})
    # get the total number of authors
    with open('authors_by_year.json') as f:
    #The json.load(f) method is used to load the contents of the file into a Python dictionary called data
        data = json.load(f)
    num_authors = sum(year_data['num_authors'] for year_data in data)
   
    publish_time_type = type(collection.find_one()['publish_time'])
    print(publish_time_type)
    pipeline = [
        {
            "$group": {
                "_id": {"$year": "$publish_time"},
                "count": {"$sum": 1},
                "titles": {"$push": "$title"}
                
            }
        },
        {
            "$sort": {
                "_id": 1
            }
        }
    ]
    # Create a dictionary to store the year and article count
    data_dict={}
    print('{data_dict}')
    # Execute the pipeline and loop through the result to store the data in a dictionary
    result = list(collection.aggregate(pipeline))
    #print (result)
    for doc in result:
        year = doc['_id']
        count = doc['count']
        titles = doc['titles']
        data_dict[year] = {'count': count, 'titles': titles}

    # Convert the data_dict to a JSON string
    data_json = json.dumps(data_dict)

    # Pass the data_dict variable to the template
    context = {
        'data_dict': data_dict,
        'data_json': data_json
    }
    return render_template('index.html', total_articles=total_articless, num_authors=num_authors, username=username, **context)
@app.route('/abstract/<title>')
def abstract(title):
    model_path = 'model-last'
    nlp = spacy.load(model_path)

    # Define entity colors
    colors = {
        "MICROORGANISM": "#D291BC",
        "CELL": "#39CCCC",
        "GENE": "#2ECC40",
        "COMPOUND": "#6B3FA0",
        "DIESEASE": "#FF4136",
        "SYMPTOMS": "#FF851B",
        "ORG": "#0074D9",
        "PROTEIN": "#B10DC9",
        "AGENT": "#001F3F",
        "MEDICINE": "#AF7AC5",
        "TREATMENT": "#F012BE",
        "TOOL": "#B7950B",
        "PERCENTAGE": "#FF00FF",
        "ENZYME": "#3D9970",
        "NUCLEIC_ACID": "#FFC125",
        "CARDINAL": "#AAAAAA",
        "DATE": "#001F3F",
        "LOC": "#444444",
        "CONDITION": "#FFDAB9",
        "AMINO_ACID": "#FFDB58"
    }
    abstract = collection.find({"title": title}, {"abstract": 1})
    abstract = abstract.next()
    abstract_text = abstract['abstract']
    doc = nlp(abstract_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Build entity options with colors
    options = {"ents": [ent.label_ for ent in doc.ents], "colors": colors}
    tagged_text = spacy.displacy.render(doc, style='ent', jupyter=False, options=options)
    return render_template('predictions.html', entities=entities, tagged_text=tagged_text)


@app.route('/search')
def search():
     if 'username' not in session:
       
        return redirect(url_for('login'))
     else:
        
         previous_searches = session.get('previous_searches', [])
         return render_template('search.html', previous_searches=previous_searches)

@app.route('/tag', methods=['POST'])
def tag_entities():
    model_path = 'model-last'
    nlp = spacy.load(model_path)
    text = request.form['input_text']
    if not text:
        flash('Please enter some text!', 'error')
        return render_template('search.html')

    # Perform entity tagging
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    # Update previous searches
    previous_searches = session.get('previous_searches', [])
    previous_searches.append(text)
    session['previous_searches'] = previous_searches

    # Build entity options with colors
    options = {"ents": [ent.label_ for ent in doc.ents], "colors": colors}
    tagged_text = spacy.displacy.render(doc, style='ent', jupyter=False, options=options)
    
    return render_template('predictions.html', entities=entities, tagged_text=tagged_text)

bcrypt = Bcrypt()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Get user input from registration form
        username = request.form['username']
        password = request.form['password']
        full_name = request.form['full_name']
        cell_no = request.form['cell_no']
        email = request.form['email']
        category = request.form['category']

        # Check if the username already exists in the database
        existing_user = mongo.db.users.find_one({'username': username})
        if existing_user:
            error_message = 'Username already exists'
            return render_template('register.html', error_message=error_message)

        # Insert the new user into the database with plain text password
        mongo.db.users.insert_one({
            'username': username,
            'password': password,
            'full_name': full_name,
            'cell_no': cell_no,
            'email': email,
            'category': category
        })

        # Redirect to the login page with a success message
        return redirect('/login')

    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get user input from login form
        username = request.form['username']
        password = request.form['password']
        
        # Check if the username exists in the database
        existing_user = mongo.db.users.find_one({'username': username})
        if existing_user:
            # Verify the password
            if existing_user['password'] == password:
                # Store the user's session data
                session['username'] = username
                return redirect(url_for('index'))  # Redirect to the index page or any other desired route
        
        # Display an error message if login fails
        error_message = 'Invalid username or password'
        return render_template('login.html', error_message=error_message)
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))



app.config['MAIL_SERVER'] = 'smtp.gmail.com'  #  your mail server
app.config['MAIL_PORT'] = 587  #  mail server port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'm.foggyfaisal@gmail.com'  #  your email username
app.config['MAIL_PASSWORD'] = 'qrtqgpninocrarsr'  #  your email password

mail = Mail(app)
client = MongoClient('mongodb://localhost:27017/')
db = client['medical11']
users_collection = db['users']


def generate_token():
    """Generate a unique token for password reset."""
    characters = string.ascii_letters + string.digits
    token = ''.join(random.choice(characters) for _ in range(15))
    return token


def send_reset_email(email, token):
    """Send password reset email to the user."""
    reset_link = url_for('reset_password', token=token, _external=True)
    subject = 'Password Reset Request'
    body = f'Hi, You requested to reset your password. Click the link below to reset your password:\n{reset_link}'
    msg = Message(subject, sender='your_email@example.com', recipients=[email])
    msg.body = body
    mail.send(msg)




@app.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = users_collection.find_one({'email': email})
        if user:
            token = generate_token()
            users_collection.update_one(
                {'email': email},
                {'$set': {'reset_token': token}}
            )
            send_reset_email(email, token)
            flash('Password reset link has been sent to your email. Please Check spam folder!')
            return redirect(url_for('forgot_password'))
        else:
            flash('Email not found.')
            return redirect(url_for('forgot_password'))
    return render_template('forgot_password.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = users_collection.find_one({'reset_token': token})
    if not user:
        flash('Invalid token.')
        return redirect(url_for('forgot_password'))

    if request.method == 'POST':
        new_password = request.form['new_password']
        users_collection.update_one(
            {'reset_token': token},
            {'$set': {'password': new_password}, '$unset': {'reset_token': ''}}
        )
        
        return redirect(url_for('login'))

    return render_template('reset_password.html', token=token)



if __name__ == '__main__':
    app.run(debug=True)
