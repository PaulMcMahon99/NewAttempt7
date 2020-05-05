from flask import render_template,url_for,flash, redirect,request,Blueprint,session
from flask_login import current_user,login_required
from onlineshop import db
from onlineshop.models import Tea, User
# ^^^ Supplier is no longer imported from models.
from onlineshop.shop.forms import AddTeaForm, UpdateTeaForm, AddSupplierForm, UpdateSupplierForm

shop_items = Blueprint('blog_posts',__name__)


#  validation needs to occur here to prevent multiple tea_name s from occurring.
@shop.route('/add_tea', methods=['GET', 'POST'])
@login_required
def add_tea():
    form = AddTeaForm()

    if.form.validate_on_submit():

        shop_item = Tea(tea_name=form.tea_name.data,
                        description=form.description.data,
                        price=form.price.data,
                        stock_level=form.stock_level.data,
                        supplier_id=form.supplier_id.data)

        db.session.add(shop_item)
        db.session.commit()
        flash('Tea stock Added!')
        return redirect(url_for('shop.html'))


# This area could be about to be disabled as I cannot work out how to get
# a subsitute method for current.user to point at the current tea object.
@shop.route('/update_tea', methods=['GET','POST'])
@login_required
def update_tea():
    form = UpdateTeaForm()

    if form.validate_on_submit():
        print(form)
        if form.tea_picture.data:
            pic = add_tea_pic(form.tea_picture.data,tea_name)
            Tea.tea_picture = pic

        Tea.description = form.description.data
        Tea.price = form.price.data
        Tea.stock_level = form.stock_level.data
        Tea.supplier_name = form.supplier_name.data
        db.session.commit()
        flash('User Account Updated')
        return redirect(url_for('users.account'))

    tea_picture = url_for('static', filename='tea_pics/' + Tea.tea_picture)
    return render_template('shop.html', tea_picture=tea_picture, form=form)


# View all teas for sale.
# The login required decorator is enabled to ensure the user is logged in to access this area.
# This ideally would be universally viewable on the homepage as per brief, but it lies behind
# this requirement due to time constaints.
@shop.route("/<tea_name>")
@login_required
def tea_items(tea_name):
    page = request.args.get('page', 1, type=int)
    tea = Tea.query.filter_by(tea_name=tea_name).first_or_404()
    tea_items = Tea.query.order_by(Tea.tea_name.desc()).paginate(page=page, per_page=10)
    return render_template('shop.html', tea_items=tea_items, user=user)

@app.route("/add_to_cart/<int:book_id>")
def add_to_cart(book_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].append(book_id)

    flash("The book is added to your shopping cart!")
    return redirect("/cart")

# This cart is from the given example.
@app.route("/cart", methods=['GET', 'POST'])
def cart_display():
    if "cart" not in session:
        flash('There is nothing in your cart.')
        return render_template("cart.html", display_cart = {}, total = 0)
    else:
        items = session["cart"]
        cart = {}

        total_price = 0
        total_quantity = 0
        for item in items:
            tea = Tea.query.get_or_404(item)

            total_price += tea.price
            if tea.id in cart:
                cart[tea.id]["quantity"] += 1
            else:
                cart[tea.id] = {"quantity":1, "title": tea.tea_name, "price":tea.price}
            total_quantity = sum(item['quantity'] for item in cart.values())


        return render_template("cart.html", title='Your Shopping Cart', display_cart = cart, total = total_price, total_quantity = total_quantity)

    return render_template('cart.html')

@app.route("/delete_book/<int:tea_id>", methods=['GET', 'POST'])
def delete_tea(tea_id):
    if "cart" not in session:
        session["cart"] = []

    session["cart"].remove(book_id)

    flash("The tea has been removed from your shopping cart!")

    session.modified = True

    return redirect("/cart")
