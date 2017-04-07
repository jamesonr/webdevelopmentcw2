from app import *
 
app.secret_key = 'development key'

@app.route('/')
def rhome():
  return render_template('index.html')

@app.route('/about')
def rabout():
  return render_template('about.html')
  
@app.route('/new')
def rcontact():
  return render_template('new.html')
  
@app.route('/giantscauseway')
def rgiantscauseway():
  return render_template('giantscauseway.html')

@app.route('/gameofthrones')
def rgot():
  return render_template('gameofthrones.html')
  
@app.route('/titanic')
def rtitanic():
  return render_template('titanic.html')

@app.route('/bogside')
def rbogside():
  return render_template('bogside.html')
  
@app.route('/castle')
def rcastle():
  return render_template('castle.html')
  
@app.route('/mountains')
def rmountains():
  return render_template('mountains.html')

@app.route('/')
def show_all():
   return render_template('index.html', students = students.query.all() )

@app.route('/new', methods = ['GET', 'POST'])
def new():
   if request.method == 'POST':
      if not request.form['name'] or not request.form['city'] or not request.form['addr']:
         flash('Please enter all the fields', 'error')
      else:
         student = students(request.form['name'], request.form['city'],
            request.form['addr'], request.form['pin'])
         
         db.session.add(student)
         db.session.commit()

         return redirect(url_for('show_all'))
   return render_template('new.html')

   