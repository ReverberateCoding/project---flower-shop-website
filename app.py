from flask import Flask, render_template, redirect, url_for, request
import os

class Flower:
    def __init__(self, name, image_absolute_url, description, price):
        self.name = name
        self.image_absolute_url = image_absolute_url
        self.description = description
        self.price = price
    def __repr__(self) -> str:
        return f"Flower name: {self.name}. Flower image absolute url: {self.image_absolute_url}. Flower description: {self.description}. Flower price: ${round(float(self.price/100),2)}"

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gallery")
def gallery():
    flowers = [
        Flower("Rose", None, "A classic red rose", 1000),
        Flower("Sunflower", None, "A bright and cheerful sunflower", 800),
        Flower("Daisy", None, "A simple yet charming daisy", 500),
        Flower("Lily", None, "An elegant white lily", 1200),
        Flower("Tulip", None, "A vibrant and colorful tulip", 900)
    ]

    return render_template("gallery.html", flowers = flowers)

@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        Name = request.form.get('Name')
        Email = request.form.get('Email')
        PhoneNumber = request.form.get('PhoneNumber')
        Message = request.form.get('Message')
        print(Name,Email,PhoneNumber,Message)
        return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/api/add_to_cart/<id>")
def add_to_cart(id):
    id = int(id)
    id -= 1
    basket = None
    with open('basket.txt', 'r') as file:
        basket = file.readlines()
    if f"{id}\n" not in basket:
        basket.append(f"{id}\n")
    os.remove('basket.txt')
    with open('basket.txt', 'w') as file:
        file.writelines(basket)
    return redirect(url_for('gallery'))
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)