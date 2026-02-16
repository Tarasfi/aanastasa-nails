from flask import Blueprint, render_template, request, redirect, url_for
from db import db
from forms import NewNailsForm, EditPriceForm
from price import Price
from flask_bootstrap import Bootstrap5

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/price")
def admin_price():
    result = db.session.execute(db.select(Price))
    prices = result.scalars().all()
    return render_template("admin/admin_price.html", prices=prices)

@admin_bp.route("/add_nails", methods=['POST', 'GET'])
def add_nails():
    form = NewNailsForm()
    if request.method == "POST":
        new_nails = Price(
            title=request.form.get('title'),
            description=request.form.get('description'),
            price=request.form.get('price'),
            service_type=request.form.get('service_type'),
        )
        db.session.add(new_nails)
        db.session.commit()

    return render_template("admin/add_nails.html", form=form)


@admin_bp.route('/delete')
def delete():
    nails = request.args.get("id")
    nails_to_delete = db.get_or_404(Price, nails)
    db.session.delete(nails_to_delete)
    db.session.commit()
    return redirect(url_for("admin.admin_price"))

@admin_bp.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditPriceForm()
    nails_id = request.args.get('id')
    nails_selected = db.get_or_404(Price, nails_id)

    if form.validate_on_submit():
        nails_selected.price = form.price.data
        nails_selected.title = form.title.data
        db.session.commit()

    form.id.data = nails_selected.id
    form.price.data = nails_selected.price
    form.title.data = nails_selected.title

    return render_template('edit.html', form=form)

