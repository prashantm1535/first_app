from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    # my_value = "Neural Nine"
    # my_result = 10 + 50
    mylist = [10,20,30,40,50,60,70]
    return render_template("index.html", list=mylist)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)



# @app.route('/')  # This binds the root URL ('/') to the index() function
# def index():
#     return "<h1>Hello, World</h1>"

# # Multiple routes to the same function using different route patterns


# @app.route('/hello')
# @app.route('/hello/')
# def hello():
#     return '<b>Hello, World !'


# @app.route('/greet/<username>')  # Dynamic route with <username> as a variable
# def greet(username):
#     return f"User: {username}"


# @app.route('/add/<int:num1>/<int:num2>')  # Dynamic route with integer type
# def add(num1, num2):
#     return f"{num1} + {num2} = {num1 + num2}"


# @app.route('/product/<float:price>')  # Dynamic route with float type
# def product_price(price):
#     return f"Price: {price}"

# # Dynamic route with Multiple Parameters


# @app.route('/user/<username>/post/<int:post_id>')
# def show_user_post(username, post_id):
#     return f"User: {username}, Post ID: {post_id}"


# @app.route('/book/<title>/author/<author_name>')
# def show_book(title, author_name):
#     return f"Book: {title}, Author: {author_name}"

# # Dynamic route with Query Parameters :
# # Query parameters are appended to the URL after a ? and can be accessed via request.args
# # (you need to import request from flask).
# # fastpath : handle_url_params?name=mike&greetings=Hello


# @app.route('/handle_url_params')
# def handle_params():
#     if 'greetings' in request.args.keys() and 'name' in request.args.keys():
#         greetings = request.args['greetings']
#         name = request.args.get('name')
#         return f"{greetings}, {name}"
#     else:
#         return 'Some parameters are missing'


# @app.route('/files/<path:subpath>')  # Dynamic route with path
# def show_subpath(subpath):
#     return f"Subpath: {subpath}"


# # Flask routes can handle different HTTP methods such as GET (default) and POST.
# # Example of a route that handles both GET and POST methods:


# @app.route('/http_methods', methods=['GET', 'POST'])
# def http_methods():
#     if request.method == 'GET':
#         return "You made a GET request\n"
#     elif request.method == 'POST':
#         return "You made a POST request\n"
#     else:
#         return "You will never see this message\n"
    
    

