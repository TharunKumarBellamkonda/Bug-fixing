from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'session_user_management'

@app.route('/')
def index():
    notes = session.get('notes', [])
    return render_template('home_page.html', notes=notes)

@app.route('/add_note', methods=['POST'])
def add_note():
    note = request.form.get('note')
    session.setdefault('notes', []).append(note)
    return redirect('/')

@app.route('/delete_all')
def delete_all_notes():
    session.pop('notes', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
