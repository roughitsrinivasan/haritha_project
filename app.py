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
        return redirect(url_for('login'))
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
    if request.method=='GET':
        return render_template('cart.html',cart=session['purchased'])
    
    count= request.form.get('count')
    price=request.form.get('prod-price').replace('Rs.','')
    name=request.form.get('prod-name')
    product_id=request.form.get('prod-id')
    print('redirect from details ',request.form.to_dict())
    total_price=int(count)*int(price)      
    import uuid
    id=uuid.uuid1() 
    session['cart']={"name":name,"count":int(count),"price":float(price),"total_price":float(total_price),"product_id":product_id,"id":str(id)}
    print(session['cart'])
    session['purchased'].append(session['cart'])
    session['cart']={}
    return render_template('cart.html',cart=session['purchased'])


@app.route('/checkout')
def checkout():
    if not session.get("name"):
        return "Not a valid user"
    print(session.get('cart'),session.get('purchased'))
    if session.get('purchased',None)==None:
        session['purchased']=[]
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
        item=[]
       
        for i in session['purchased']:
            item.append({
                "name":i["name"],
                "price":i["price"],
                "quantity":i["count"],
                "total":i["total_price"],
                "address":address
            })
        
        insert_order(name,email,phone,address,item)
        from email_utils import index
        from datetime import date
        username=session.get('name')
        cur_date=date.today()
        order_id= random.randint(100000,999999)
        check=index(email,username,cur_date,order_id,address,phone)
        print(check)
        session['purchased']=[]
        session['cart']={}
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
    

@app.route('/edit-order',methods=['POST','GET'])
def edit():
    print(session.get('purchased'))
    print(request.args.get('id'),request.args.get('count'))
    id=request.args.get('id')
    operation=request.args.get('op')
    if operation=='rem':
        for i in session['purchased']:
            if i['id']==id:
                session['purchased'].remove(i)
        return redirect(url_for('cart'))
    for i in session['purchased']:
        if i['id']==id:
            if operation=='plus':
                i['count']=int(i['count'])+1
            else:
                i['count']=int(i['count'])-1
            count=i['count']
            i['total_price']=int(count)*i['price']
    return redirect(url_for('cart'))


@app.route('/clear-cart',methods=['GET'])
def clearCart():
    session['purchased']=[]  
    return redirect(url_for('cart'))

@app.route('/logout',methods=['POST','GET'])
def logout():
    if not session.get("name"):
        return "Not a valid user"
    session.pop('name',None)
    return redirect(url_for('login'))
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=7000,debug = True)