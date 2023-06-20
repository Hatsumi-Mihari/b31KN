from re import *
from xmlrpc.client import DateTime
from datetime import date
from flask import Flask, render_template, url_for, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import header_property
from threading import *
from sqlalchemy.types import BINARY 
from sqlite3 import *
from flask import send_file
from base64 import *


app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MAX_CONTENT_LANGTH = 999999999 * 999999999
db = SQLAlchemy(app)

class Article(db.Model):
    _tablename='Article'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    
    def __repr__ (self):
        return '<Article %r>' % self.id

class News(db.Model):
    _tablename='News'
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime)
    
    def __repr__ (self):
        return '<News %r>' % self.id

class menu(db.Model):
    _tablename='menu'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    link = db.Column(db.Text)

    def __repr__ (self):
        return '<menu %r>' % self.id

class menuSub(db.Model):
    _tablename='menuSub'
    id = db.Column(db.Integer, primary_key=True)
    idMenu = db.Column(db.Integer)
    idArt = db.Column(db.Integer)
    name = db.Column(db.String(200), nullable=False)
    link = db.Column(db.Text)

    
    def __repr__ (self):
        return '<menuSub %r>' % self.id

class schooleGalery(db.Model):
    _tablename='schooleGalery'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500000), nullable=False)
    link = db.Column(db.Text)
    photo = db.Column(db.LargeBinary)

    
    def __repr__ (self):
        return '<schooleGalery %r>' % self.id

class User(db.Model):
    _tablename='user'
    id=db.Column(db.Integer, primary_key=True)
    password=db.Column(db.String)
    email=db.Column(db.String)
    id_roel = db.Column(db.Integer)

    def __repr__ (self):
        return '<user %r>' % self.id


@app.route('/userDefinitions')
def userDef():
    return render_template('Definitions.html')


@app.route('/', methods=['POST', 'GET'])
def home():
    menuData = menu.query.order_by(menu.id).all()
    menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
    news = News.query.all()
    idNews = []
    for i in news: 
        idNews.append('/news/' + str(i.id) + '/')
    return render_template('home.html', menuData = menuData, menuData2 = menuData2, idN = idNews)

@app.route('/userDefinitions/AdminControlPanel')
def adminControlPanel():
    return render_template('AdminControlPanel.html')

@app.route('/news')
def news():
    idNews = []
    menuData = menu.query.order_by(menu.id).all()
    menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
    news = News.query.all()
    for i in news: 
        idNews.append('/news/' + str(i.id) + '/')

    oneRes = False
    res2 = 0
    res3 = 0
    whereStartIMG = 0
    artic = News.query.all()
    f = schooleGalery.query.all()
    img_arr = []
    a = []
    blocks_form_DB = ''
    contents = ''
    if len(artic) == 0:
        blocks_form_DB += str("""<center><h1 class="titleaArt">None News</h1></center>""")
    else:
        for j in artic:
            contents = j.text

            o = contents
            w = o.split('|')
            b = []
            h = 1
            for i in range(0,len(w)):
                if i == h:
                    b.append(w[i])
                    h += 2
            v = []
            for i in range(0,len(b)):
                v.append(b[i].split('-', 1))

            for i in range(0,len(v)):
                #generator img blocks 
                if str(v[i][0]) == 'imgBlock':
                    p1 = v[i][1].split(',')
                    p2 = str(p1[0])
                    p3 = str(p1[1])
                    p4 = str(p1[2])
                    res1 = 0
                    u = ''
                    u2 = ''
                    u3 = ''
                    for g in range(1,len(p2)):
                        u += str(p2[g])
                        res1 = int(u)
                    for h in range(0,len(p3)):
                        u2 += str(p3[h])
                        res2 = int(u2)
                        if oneRes == False:
                            whereStartIMG = res2
                        oneRes = True
                    for h in range(0,len(p4)-1):
                        u3 += str(p4[h])
                        res3 = int(u3)
                    blocks_form_DB += str(imgBlock(res1, res2, res3))
                    print(whereStartIMG,res3)
                #generator video from youtube 
                if str(v[i][0]) == 'includeYT':
                    u = v[i][1].split('(')
                    b = u[1]
                    res = ''
                    for h in range(0,len(b)-1):
                        res += b[h]
                    blocks_form_DB += str("""<center><div><iframe width="560" class="video1" height="315" src="%s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></center>"""%(res))
                #generator text block 
                if str(v[i][0]) == 'text':
                    u = v[i][1].split('(')
                    b = u[1]
                    res = ''
                    for h in range(0,len(b)-1):
                        res += b[h]
                    blocks_form_DB += str("""<p class="textFount">%s</p>"""%(res))
                #generator titel 
                if str(v[i][0]) == 'title':
                    u = v[i][1].split('(')
                    b = u[1]
                    res = ''
                    for h in range(0,len(b)-1):
                        res += b[h]
                    blocks_form_DB += str("""<center><h1 class="titleaArt">%s</h1></center>"""%(res))
                blocks_form_DB += str("""<center><h1 class="titleaArt">%s</h1></center><hr/>"""%(j.date))
    f = schooleGalery.query.all()
    img_arr = []
    name_f = []
    a = []
    for n in f:
        image = b64encode(n.photo).decode("utf-8")
        img_arr.append(image)
        name_f.append(n.name)
        a.append(str(n.name))

    return render_template('news.html', image = img_arr, contents=contents ,artic = artic, menuData = menuData, menuData2 = menuData2, name = a, blocks = blocks_form_DB, stopV = res3,startv = whereStartIMG, idN = idNews)

@app.route('/userDefinitions/AdminControlPanel/Publish', methods=['POST', "GET"])
def adminControlPanel_Publish():
    if request.method == "POST":
        title = request.form.get('title')
        text = request.form.get('text')
        article = Article (title = title, text = text, date= date.today())
        cMenu = request.form.get('cooseM')
        pointSub = menuSub( idMenu = cMenu, name = title)
        try:
            db.session.add(pointSub)
            db.session.add(article)
            db.session.commit()
            return redirect('/userDefinitions/AdminControlPanel/Publish')
        except:
            return "At edited new article came erorr"
    else:
        menuData = menu.query.order_by(menu.id).all()
        return render_template('AdminControlPanel_Publish.html', menuData = menuData)         

@app.route('/userDefinitions/AdminControlPanel/ADD_NEWS', methods=['POST', "GET"])
def adminControlPanel_ADD_NEWS():
    if request.method == "POST":
        title = request.form.get('title')
        text = request.form.get('text')
        article = News (title = title, text = text, date= date.today())
        cMenu = request.form.get('cooseM')
        pointSub = menuSub( idMenu = cMenu, name = title)
        try:
            db.session.add(pointSub)
            db.session.add(article)
            db.session.commit()
            return redirect('/userDefinitions/AdminControlPanel/ADD_NEWS')
        except:
            return "At edited new article came erorr"
    else:
        menuData = menu.query.order_by(menu.id).all()
        return render_template('AdminControlPanel_Publish.html', menuData = menuData)  


@app.route('/userDefinitions/AdminControlPanel/EditMenu', methods=['POST', "GET"])
def adminControlPanel_Edit():
    if request.method == "POST":
    	name = request.form.get('enterName')
    	link = request.form.get('enterLink')
    	idMenu = request.form.get('enterIDmenu')
    
    	menus = menu (name= name, link= link)

    	try: 
    		db.session.add(menus)
    		db.session.commit()
    		return redirect('/userDefinitions/AdminControlPanel/EditMenu')
    	except:
    		return "At edited new article came erorr"
    else:
        menuData = menu.query.all()
        return render_template('AdminControlPanel_Edit.html', menuData = menuData)
        
@app.route('/userDefinitions/AdminControlPanel/UpdataMenu', methods=['POST', "GET"])
def adminControlPanel_UadataMenu():
    if request.method == 'POST':
        id = request.form.get('enterID')
        menus = menu.query.get(id)
        menus.name = request.form.get('enterName')
        menus.link = request.form.get('enterLink')

        
        try:
            if menus.name == 'del':
                db.session.delete(menus)
                db.session.commit()
            if menus.name != 'del':
                db.session.commit()
            return redirect('/userDefinitions/AdminControlPanel/UpdataMenu')
        except:
            return 'Erorr'
    else:
        menuData = menu.query.order_by(menu.id).all()
        return render_template('AdminControlPanel_UpdataMenu.html', menuData = menuData)

     
@app.route('/userDefinitions/AdminControlPanel/PhotoAdd', methods=['POST', "GET"])
def adminControlPanel_PhotoAdd():
    f = schooleGalery.query.all()
    if request.method == 'POST':
        img_arr = []
        name_f = []
        for n in f:
            image = b64encode(n.photo).decode("utf-8")
            img_arr.append(image)
            name_f.append(n.name)

        return render_template('AdminControlPanel_PhotoAdd.html', image= img_arr, name = name_f)
    else:
        img_arr = []
        a = []
        for n in f:
            image = b64encode(n.photo).decode("utf-8")
            img_arr.append(image)
            a.append(str(n.name))
        return render_template('AdminControlPanel_PhotoAdd.html', image= img_arr, name = a)  

idart = None

@app.route('/userDefinitions/AdminControlPanel/upfiles', methods=['POST', "GET"])
def upfiles():
    if request.method == 'POST':
        file = request.files.getlist('upfile')
        print(file)
        for i in file:
            nFile = schooleGalery(name = i.filename, photo = i.read())
            db.session.add(nFile)
            db.session.commit()
        return redirect('/userDefinitions/AdminControlPanel/PhotoAdd')
    else:
        return render_template('Error upload file')

@app.route('/userDefinitions/AdminControlPanel/EditArticleID/<int:id>/', methods=['POST', "GET"])
def adminControlPanel_EditArticle(id):
    artic = Article.query.get(id)
    menusub = menuSub.query.get(id)
    if request.method == 'POST':
        artic.title = request.form.get('editTitle')
        artic.text = request.form.get('editText') 
        menusub.name = request.form.get('editTitle')
        try:
            db.session.commit()
            return redirect('/userDefinitions/AdminControlPanel/EditArticle')
        except:
            return 'Erorr'
    else:
        menuData = menu.query.all()
        menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
        return render_template('AdminConsolePanel_editArticID.html', menuData=menuData, menuData2=menuData2, artic=artic) 

@app.route('/userDefinitions/AdminControlPanel/EditArticle', methods=['POST', "GET"])
def adminControlPanel_EditArticle1():
    if request.method == 'POST':
        cMenu = request.form.get('cooseM')
        idart = cMenu

        try:
            menuData = menu.query.all()
            menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
            return redirect('/userDefinitions/AdminControlPanel/EditArticleID/%s'%(idart))  
        except:
            return '123'
    else:
        menuData = menu.query.all()
        menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
        return render_template('AdminControlPanel_EditArticle.html', menuData=menuData, menuData2=menuData2) 

@app.route('/userDefinitions/AdminControlPanel/DeletePub', methods=['POST', "GET"])
def adminControlPanel_DeletePub():
    if request.method == 'POST':
        menuData2 = menuSub.query.all()
        art =  Article.query.all()
        cMenu = request.form.get('list')
        r = cMenu.split(',')
        try:
            for i in r:
                menuData = menuSub.query.get(i)
                art = Article.query.get(i)
                db.session.delete(menuData)
                db.session.delete(art)
                db.session.commit()
            return redirect('/userDefinitions/AdminControlPanel/DeletePub') 
        except:
            return redirect('/userDefinitions/AdminControlPanel/DeletePub')
    else:
        menuData2 = menuSub.query.all()
        return render_template('DeletePub.html', menuData2=menuData2) 

@app.route('/userDefinitions/AdminControlPanel/DeletePicture', methods=['POST', "GET"])
def adminControlPanel_DeletePic():
    f = schooleGalery.query.all()
    img_arr = []
    name_f = []
    id = []
    a = []
    lastId = 0
    h = 0
    for n in f:
        image = b64encode(n.photo).decode("utf-8")
        img_arr.append(image)
        name_f.append(n.name)
        a.append(str(n.name)) 
        id.append(n.id)
        lastId = id[-1]
    if request.method == 'POST':
        menuData2 = schooleGalery.query.all()
        cMenu = request.form.get('list')
        r = cMenu.split(',')
        try:
            for i in r:
                menuData = schooleGalery.query.get(i)
                db.session.delete(menuData)
                db.session.commit()
            return redirect('/userDefinitions/AdminControlPanel/DeletePicture') 
        except:
            return redirect('/userDefinitions/AdminControlPanel/DeletePicture')
    else:
        menuData2 = schooleGalery.query.all()
        return render_template('DeletePicture.html', menuData2=menuData2, img = img_arr, name = a, stopV = lastId, idP = id) 

def imgBlock(id, startN, stopN):
    f = schooleGalery.query.all()
    img_arr = []
    name_f = []
    a = []
    res = ''
    if id == 1:
        res = '<div class="type1">'
        for n in f:
            image = b64encode(n.photo).decode("utf-8")
            img_arr.append(image)
            name_f.append(n.name)
            a.append(str(n.name))
        for i in range(startN,stopN-1):
            res += '<div class="clickBLock"><img src="data:;base64,%s" alt="140x140" srcset="" class="img4x4" id="%s"></div>'%(img_arr[i-1], i)
        res += '</div>'
    if id == 2:
        res = '<div class="type2">'
        for n in f:
            image = b64encode(n.photo).decode("utf-8")
            img_arr.append(image)
            name_f.append(n.name)
            a.append(str(n.name))
        for i in range(startN,stopN-1):
            res += '<div class="clickBLock"><img src="data:;base64,%s" alt="140x140" srcset="" class="img4x4" id="%s"></div>'%(img_arr[i-1], i)
        res += '</div>'

    return res

@app.route('/content/<int:id>/')
def content(id):    
    oneRes = False
    res2 = 0
    res3 = 0
    whereStartIMG = 0
    idNews = []
    news = News.query.all()
    for i in news: 
        idNews.append('/news/' + str(i.id) + '/')

    menuData = menu.query.all()
    menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
    artic = Article.query.get(id)
    f = schooleGalery.query.all()
    img_arr = []
    a = []
    blocks_form_DB = ''
    contents = artic.text

    o = contents
    w = o.split('|')
    b = []
    h = 1
    for i in range(0,len(w)):
        if i == h:
            b.append(w[i])
            h += 2
    v = []
    for i in range(0,len(b)):
        v.append(b[i].split('-', 1))

    for i in range(0,len(v)):
        #generator img blocks 
        if str(v[i][0]) == 'imgBlock':
            p1 = v[i][1].split(',')
            p2 = str(p1[0])
            p3 = str(p1[1])
            p4 = str(p1[2])
            res1 = 0
            u = ''
            u2 = ''
            u3 = ''
            for g in range(1,len(p2)):
                u += str(p2[g])
                res1 = int(u)
            for h in range(0,len(p3)):
                u2 += str(p3[h])
                res2 = int(u2)
                if oneRes == False:
                    whereStartIMG = res2
                oneRes = True
            for h in range(0,len(p4)-1):
                u3 += str(p4[h])
                res3 = int(u3)
            blocks_form_DB += str(imgBlock(res1, res2, res3))
            print(whereStartIMG,res3)
        #generator video from youtube 
        if str(v[i][0]) == 'includeYT':
            u = v[i][1].split('(')
            b = u[1]
            res = ''
            for h in range(0,len(b)-1):
                res += b[h]
            blocks_form_DB += str("""<center><div><iframe width="560" class="video1" height="315" src="%s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></center>"""%(res))
         #generator text block 
        if str(v[i][0]) == 'text':
            u = v[i][1].split('(')
            b = u[1]
            res = ''
            for h in range(0,len(b)-1):
                res += b[h]
            blocks_form_DB += str("""<p class="textFount">%s</p>"""%(res))
         #generator titel 
        if str(v[i][0]) == 'title':
            u = v[i][1].split('(')
            b = u[1]
            res = ''
            for h in range(0,len(b)-1):
                res += b[h]
            blocks_form_DB += str("""<center><h1 class="titleaArt">%s</h1></center>"""%(res))
        

    f = schooleGalery.query.all()
    img_arr = []
    name_f = []
    a = []
    for n in f:
        image = b64encode(n.photo).decode("utf-8")
        img_arr.append(image)
        name_f.append(n.name)
        a.append(str(n.name))
    

    return render_template('content.html',idN = idNews,image = img_arr, contents=contents ,artic = artic, menuData = menuData, menuData2 = menuData2, name = a, blocks = blocks_form_DB, stopV = res3,startv = whereStartIMG) 


@app.route('/news/<int:id>/')
def newsP(id):    
    oneRes = False
    res2 = 0
    res3 = 0
    whereStartIMG = 0
    idNews = []
    news = News.query.all()
    for i in news: 
        idNews.append('/news/' + str(i.id) + '/')

    menuData = menu.query.all()
    menuData2 = menuSub.query.order_by(menuSub.idMenu).all()
    artic = News.query.get(id)
    f = schooleGalery.query.all()
    img_arr = []
    a = []
    blocks_form_DB = ''
    contents = artic.text

    o = contents
    w = o.split('|')
    b = []
    h = 1
    for i in range(0,len(w)):
        if i == h:
            b.append(w[i])
            h += 2
    v = []
    for i in range(0,len(b)):
        v.append(b[i].split('-', 1))

    for i in range(0,len(v)):
        #generator img blocks 
        if str(v[i][0]) == 'imgBlock':
            p1 = v[i][1].split(',')
            p2 = str(p1[0])
            p3 = str(p1[1])
            p4 = str(p1[2])
            res1 = 0
            u = ''
            u2 = ''
            u3 = ''
            for g in range(1,len(p2)):
                u += str(p2[g])
                res1 = int(u)
            for h in range(0,len(p3)):
                u2 += str(p3[h])
                res2 = int(u2)
                if oneRes == False:
                    whereStartIMG = res2
                oneRes = True
            for h in range(0,len(p4)-1):
                u3 += str(p4[h])
                res3 = int(u3)
            blocks_form_DB += str(imgBlock(res1, res2, res3))
            print(whereStartIMG,res3)
        #generator video from youtube 
        if str(v[i][0]) == 'includeYT':
            u = v[i][1].split('(')
            b = u[1]
            res = ''
            for h in range(0,len(b)-1):
                res += b[h]
            blocks_form_DB += str("""<center><div><iframe width="560" class="video1" height="315" src="%s" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div></center>"""%(res))
         #generator text block 
        if str(v[i][0]) == 'text':
            u = v[i][1].split('(')
            b = u[1]
            res = ''
            for h in range(0,len(b)-1):
                res += b[h]
            blocks_form_DB += str("""<p class="textFount">%s</p>"""%(res))
         #generator titel 
        if str(v[i][0]) == 'title':
            u = v[i][1].split('(')
            b = u[1]
            res = ''
            for h in range(0,len(b)-1):
                res += b[h]
            blocks_form_DB += str("""<center><h1 class="titleaArt">%s</h1></center>"""%(res))
        

    f = schooleGalery.query.all()
    img_arr = []
    name_f = []
    a = []
    for n in f:
        image = b64encode(n.photo).decode("utf-8")
        img_arr.append(image)
        name_f.append(n.name)
        a.append(str(n.name))
    

    return render_template('content.html',image = img_arr, contents=contents ,artic = artic, menuData = menuData, menuData2 = menuData2, name = a, blocks = blocks_form_DB, stopV = res3,startv = whereStartIMG, idN = idNews)


@app.route('/regUSer')
def regUser():
    return render_template(123)



if __name__ == "__main__":
    app.run(debug=True)
