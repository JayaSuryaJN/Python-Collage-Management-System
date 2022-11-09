from flask import Flask,render_template,request,redirect
import pymysql

x=Flask(__name__)

@x.route('/')

def index():
    
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo 1")
        cu=db.cursor()
        sql="select * from task "
        cu.execute(sql)
        data=cu.fetchall()
        return render_template('dashboard.html',d=data)

    except Exception as e:
        print("Error:",e)


@x.route('/form')

def create():

    return render_template('form.html')


@x.route('/store',methods=['POST'])

def store():

    s=request.form['name']
    r=request.form['rollno']
    c=request.form['class']
    m=request.form['mark']  
    try:
       db=pymysql.connect(host="localhost",user="root",password="",database="todo 1")
       cu=db.cursor()
       sql="insert into task(name,rollno,class,mark)values('{}','{}','{}','{}')".format(s,r,c,m)
       cu.execute(sql)
       db.commit()
       return redirect('/')

    except Exception as e:
       print("Error:",e)


@x.route('/delete/<rid>')

def delete(rid):

    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo 1")
        cu=db.cursor()
        sql="delete from task where id='{}'".format(rid)
        cu.execute(sql)
        db.commit()
        return redirect('/')

    except Exception as e:
        print("Error:",e)

@x.route('/edit/<rid>')

def edit(rid):
    
    try:
        db=pymysql.connect(host="localhost",user="root",password="",database="todo 1")
        cu=db.cursor()
        sql="select * from task where id='{}'".format(rid)
        cu.execute(sql)
        data=cu.fetchone()
        return render_template('edit.html',d=data)

    except Exception as e:
        print("Error:",e)

@x.route('/update/<rid>',methods=['POST'])

def update(rid):

    s=request.form['name']
    r=request.form['rollno']
    c=request.form['class']
    m=request.form['mark']
    try:
         db=pymysql.connect(host="localhost",user="root",password="",database="todo 1")
         cu=db.cursor()
         sql="update task SET name='{}',rollno='{}',class='{}',mark='{}' where id='{}'".format(s,r,c,m,rid)
         cu.execute(sql)
         db.commit()
         return redirect('/')

    except Exception as e:
         print("Error:",e)


x.run(debug=True)
