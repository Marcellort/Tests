from flask import Flask, render_template, request, redirect
from src.backend.controller.category_controller import CategoryController
from src.backend.model.category import Category

app = Flask(__name__)


@app.route('/')
def index():
    list_category = CategoryController().read_all()
    return render_template('/index.html', list_category=list_category)


@app.route('/create_category', methods=['GET', 'POST'])
def create_category():
    if request.form.get('name'):
        controller_category = CategoryController()
        name = request.form.get('description')
        description = request.form.get('description')
        cat = Category(name, description)
        controller_category.create(cat)
        return redirect('/')
    return render_template('form_create_category.html')

@app.route('/delete_category/<int:id>')
def delete_category(id):
    controller_category = CategoryController()
    list_ = controller_category.read_by_id(id)
    CategoryController().delete(list_)
    return redirect('/')
@app.route('/update_category/<int:id_>', methods=['GET','POST'])
def update_category(id_):
    controller_customer = CategoryController()
    cat = controller_customer.read_by_id(id_)
    if request.form.get('name'):
        name = request.form.get('name')
        description = request.form.get('description')
        cat.name = name
        cat.description = description
        controller_customer.create(cat)
        return redirect('/')
    return render_template('form_update_category.html', category=cat)
app.run(debug=True)
