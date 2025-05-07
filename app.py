from flask import Flask, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return '''
        <h1>Welcome to Banyar's Web Page</h1>
        <a href="/page1">Go to Page 1</a>
    '''

@app.route('/page1')
def page1():
    return '''
        <h2>Page 1</h2>
        <form action="/home" method="get" style="display:inline;">
            <button type="submit">home</button>
        </form>
        <form action="/page2" method="get" style="display:inline;">
            <button type="submit">Page2</button>
        </form>
    '''

@app.route('/page2', methods=['GET', 'POST'])
def page2():
    message = ''
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        message = f'<p>Hello {user_input}</p>'
    return f'''
        <h2>Page 2</h2>
        {message}
        <form method="post">
            <input type="text" name="user_input" placeholder="Enter something">
            <button type="submit">Submit</button>
        </form>
        <br>
        <a href="/home">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 