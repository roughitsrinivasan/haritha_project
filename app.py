from flask import Flask, render_template, request , redirect,url_for, session
from flask_session import Session

from utils import *
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route('/')
def start():
    return redirect(url_for('login'))
    return render_template('start.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        pwd = request.form['pwd']
        print(user)
        print(pwd)

        
        if user=="haritha" and pwd == "haritha@123":
            session["name"] = user
            
            return redirect(url_for('home'))
        elif user=="admin" and pwd == "admin":
            session["name"] = "admin"
            return redirect(url_for('home'))
        else:
            return render_template('not.html')
    session['purchased']=[]
    session['cart']={}
            
    return render_template('login.html')
    # else:
    #     user = request.args.get('nm')
    #     return redirect(url_for('home', name=user))

@app.route('/home')
def home():
    if not session.get("name"):
        return "Not a valid user"
    return render_template('home.html')

@app.route('/details1')
def details1():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('details1.html')

@app.route('/details2')
def details2():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('details2.html')

@app.route('/details3')
def details3():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('details3.html')

@app.route('/details4')
def details4():
    if not session.get("name"):
        return "Not a valid user"

    return render_template('details4.html')


@app.route('/cart',methods=['POST','GET'])
def cart():
    if not session.get("name"):
        return "Not a valid user"
    if request.method=='post':
        count= request.form.get('count')
        price=request.form.get('prod-price')
        name=request.form.get('prod-name')
        print(request.form.to_dict())
        total_price=int(count)*int(price)      
        session['cart']={"name":name,"count":count,"price":price,"total_price":total_price}
        print(session['cart'])
    return render_template('cart.html')

@app.route('/checkout')
def checkout():
    if not session.get("name"):
        return "Not a valid user"
    print(session.get('cart'))
    if session.get('purchased',None)==None:
        session['purchased']=[]
    session["purchased"].append(session['cart'])
    return render_template('cash.html')

@app.route('/order',methods=['POST','GET'])
def order():
    if not session.get("name"):
        return "Not a valid user"
    if request.method=='POST':
        name=request.form.get('con_name')
        email=request.form.get('con_email')
        phone=request.form.get('con_phone')
        address=request.form.get('con_address') 
        import random
        item=[{
                "name":"Printed round neck T-shirt",
                "price":"299.99",
                "quantity":random.randint(1,10),
                "total":random.randint(1,10)*299.99
            },
            {
                "name":"Blue White crop top",
                "price":"599.99",
                "quantity":random.randint(1,10),
                "total":random.randint(1,10)*599.99
            }]
        
        insert_order(name,email,phone,address,item)
        from email_utils import index
        from datetime import date
        username=session.get('name')
        cur_date=date.today()
        order_id= random.randint(100000,999999)
        check=index(email,username,cur_date,order_id,address,phone)
        print(check)

        return redirect(url_for('order'))
    return render_template('thankyou.html')

@app.route('/orders')
def orders():
    if not session.get("name"):
        return "Not a valid user"
    print(session.get('name'))
    if session.get('name')=="admin":
        print("admin")
        # products    =   load_orders_from_json()
        products    =   load_orders_from_json()
    # print(products,session.get("name")) 
        return render_template('orders.html',orders=products)
    else:
        return redirect(url_for('login'))
    
@app.route('/logout',methods=['POST','GET'])
def logout():
    if not session.get("name"):
        return "Not a valid user"
    session.pop('name',None)
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7000,debug = True)