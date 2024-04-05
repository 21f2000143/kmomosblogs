from flask import (Flask, request, jsonify, render_template)
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
db = SQLAlchemy(app)
app.app_context().push()


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer)  # Demographic: Age
    gender = db.Column(db.String(10))  # Demographic:
    city = db.Column(db.String(50))  # Geographic: City
    state = db.Column(db.String(50))  # Geographic: State
    country = db.Column(db.String(50))  # Geographic: Country
    competitor_location = db.Column(db.String(100))  # Competitor Location Data
    foot_traffic = db.Column(db.Integer)  # Foot Traffic Data
    favorite_cuisine = db.Column(db.String(50))  # Food Trends:
    social_media_followers = db.Column(db.Integer)  # Social Media Engagement 
    ad_conversion_rate = db.Column(db.Float)  # Advertising Performance Data
    # Add more fields as needed

    def __repr__(self):
        return f"<Customer {self.name}>"


db.create_all()


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        data = request.json
        name = data.get('name')
        email = data.get('email')
        age = data.get('age')
        gender = data.get('gender')  # Retrieve other fields as needed
        city = data.get('city')
        state = data.get('state')
        country = data.get('country')
        competitor_location = data.get('competitor_location')
        foot_traffic = data.get('foot_traffic')
        favorite_cuisine = data.get('favorite_cuisine')
        social_media_followers = data.get('social_media_followers')
        ad_conversion_rate = data.get('ad_conversion_rate')

        # Validate fields (example: age must be between 18 and 120)
        if not (18 <= age <= 120):
            raise ValueError("Invalid age. Must be between 18 and 120.")

        # Create a new customer record
        new_customer = Customer(
            name=name,
            email=email,
            age=age,
            gender=gender,
            city=city,
            state=state,
            country=country,
            competitor_location=competitor_location,
            foot_traffic=foot_traffic,
            favorite_cuisine=favorite_cuisine,
            social_media_followers=social_media_followers,
            ad_conversion_rate=ad_conversion_rate
        )
        db.session.add(new_customer)
        db.session.commit()

        # return jsonify({'message': 'Data saved successfully!'}), 201
        return render_template("index.html")
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(debug=True)
