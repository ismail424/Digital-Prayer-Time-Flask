#Kommentar
#Ahla dig
from flask import Flask, render_template, request, redirect, url_for,flash
from flask_sqlalchemy import SQLAlchemy 
import datetime
from datetime import datetime 
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///prayer.db'

#This dosent do anything important
app.secret_key = 'Secret key'

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
class Iqamah(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fajriq = db.Column(db.String(20), default="30")
    fromfajr = db.Column(db.String(1), default="1")
    fromsunrise= db.Column(db.String(1), default="0")
    dhuhriq = db.Column(db.String(20), default="8")
    asriq = db.Column(db.String(30),default="8")
    magribiq =db.Column(db.String(30), default="0")
    ishaiq = db.Column(db.String(30), default="8")
    b1 = db.Column(db.String(1), default="1")
    b2 = db.Column(db.String(30), default="0")
    b3 = db.Column(db.String(1), default="0")

class Translate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    monday = db.Column(db.String(30),default='Monday')
    tuesday = db.Column(db.String(30),default='Tuesday')
    wednesday = db.Column(db.String(30),default='Wednesday')
    thursday  = db.Column(db.String(30),default='Thursday')
    friday = db.Column(db.String(30),default='Friday')
    saturday = db.Column(db.String(30),default='Saturday')
    sunday = db.Column(db.String(30),default='Sunday')

    next1 = db.Column(db.String(30),default='Next...')
    prayer = db.Column(db.String(30),default='Prayer')
    begins = db.Column(db.String(30),default='Begins')
    iqamah = db.Column(db.String(30),default='Iqamah')
    
    fajrname = db.Column(db.String(30),default='Fajr')
    sunrisename = db.Column(db.String(50),default='Sunrise')
    dhuhrname = db.Column(db.String(30),default='Dhuhr')
    asrname = db.Column(db.String(30),default='Asr')
    magribname = db.Column(db.String(30),default='Magrib')
    ishaname = db.Column(db.String(30),default='Isha')

    mosque = db.Column(db.String(50),default='Gothenburg Mosque')
    shutphone = db.Column(db.String(50),default='Please, turn off your phones')
from bön import bönbön

@app.route('/')
def start(): 
    return render_template('start.html')
@app.route('/settings')
def settings():
    setting = Iqamah.query.first()
    if setting == None:
        setting =Iqamah()
        db.session.add(setting)
        db.session.commit()
    if setting.fromfajr == "fromfajrvalue":
        if setting.b1 == "b1":
            return render_template('settings.html', setting=setting, box1="checked", box3="checked")
        elif setting.b1 == "b2":
            return render_template('settings.html', setting=setting, box1="checked", box4="checked")
    elif setting.fromfajr == "fromsunrisevalue":
        if setting.b1 == "b1":
            return render_template('settings.html', setting=setting, box2="checked", box3="checked")
        elif setting.b1 == "b2":
            return render_template('settings.html', setting=setting, box2="checked", box4="checked")
@app.route('/addsettings', methods=['GET', 'POST'])
def addsettings():
    setting = Iqamah.query.first()
    setting.fajriq = request.form["fajriq"]
    if request.form["from"] == "fromfajrvalue":
        setting.fromfajr = "fromfajrvalue"
    else:
        setting.fromfajr = "fromsunrisevalue"

    setting.dhuhriq = request.form["dhuhriq"]
    setting.b2 = request.form["b2"]
    setting.asriq = request.form["asriq"]
    setting.magribiq = request.form["magribiq"]
    setting.ishaiq = request.form["ishaiq"]
    if request.form["bön"] == "b1":
        setting.b1 = "b1"
    elif request.form["bön"] == "b2":
        setting.b1 = "b2"


    db.session.commit()
    return redirect(url_for('start'))

@app.route('/translate')
def translate():
    post = Translate.query.first()
    if post == None:
        post = Translate()
        db.session.add(post)
        db.session.commit()
    else:
        return render_template('translate.html', post=post)

@app.route('/addtranslate', methods=['GET', 'POST'])
def addtranslate():
    post = Translate.query.first()
    post.monday = request.form["monday"]
    post.tuesday = request.form["tuesday"]
    post.wednesday = request.form["wednesday"]
    post.thursday  = request.form["thursday"]
    post.friday = request.form["friday"]
    post.saturday = request.form["saturday"]
    post.sunday = request.form["sunday"]

    post.next1 = request.form["next1"]
    post.prayer = request.form["prayer"]
    post.begins = request.form["begins"]
    post.iqamah = request.form["iqamah"]

    post.fajrname = request.form["fajrname"]
    post.sunrisename = request.form["sunrisename"]
    post.dhuhrname = request.form["dhuhrname"]
    post.asrname = request.form["asrname"]
    post.magribname = request.form["magribname"]
    post.ishaname = request.form["ishaname"]
    post.mosque = request.form["mosque"]
    post.shutphone = request.form["shutphone"]

    db.session.commit()
    return redirect(url_for('start'))

@app.route('/home')
def index():
    posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
    if not posts:
        flash("No posts")
        return redirect(url_for('start'))
    return render_template('index.html', posts=posts)
@app.route('/sendhome',methods=['POST'])
def sendhome():
    return redirect(url_for('index'))

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()

    return render_template('post.html', post=post)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = "Testtest"
    author = request.form['author']
    content = request.form['content']

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

@app.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Blogpost.query.get_or_404(post_id) 
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('start'))



@app.route('/bön1')
def bön1():
    post = Translate.query.first()
    now = datetime.now()
    fajrimon,dag,fajr,fajriqamah,solupgång,zuhr,zuhriqamah,asr,asriqamah,magrib,magribiqamah,isha, ishaiqamah = bönbön()
    return render_template('bön_vanliga.html', post=post,fajrimon= fajrimon,dag=dag,fajr=fajr,fajriqamah=fajriqamah,solupgång=solupgång,zuhr=zuhr,zuhriqamah=zuhriqamah,asr=asr, asriqamah = asriqamah,magrib=magrib, magribiqamah=magribiqamah ,isha=isha,ishaiqamah =ishaiqamah)


@app.route('/bön2')
def bön2():
    now = datetime.now()
    fajrimon,dag,fajr,fajriqamah,solupgång,zuhr,zuhriqamah,asr,asriqamah,magrib,magribiqamah,isha, ishaiqamah = bönbön()
    return render_template('bön_utaniqamah.html',fajrimon= fajrimon,dag=dag,fajr=fajr,fajriqamah=fajriqamah,solupgång=solupgång,zuhr=zuhr,zuhriqamah=zuhriqamah,asr=asr, asriqamah = asriqamah,magrib=magrib, magribiqamah=magribiqamah ,isha=isha,ishaiqamah =ishaiqamah)

if __name__ == '__main__':
    #LOCAL SERVER:
    app.run(debug=True)

    #LIVE SERVER MEN FÖR LAN:
    # app.run(host= '0.0.0.0')
