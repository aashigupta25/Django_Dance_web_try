from django.shortcuts import render
import mysql.connector as sql
fn = ''
ln = ''
jd = ''
dd = ''
id = ''

# Create your views here.

def registerAction(request):
    global fn, ln, jd, dd, id
    if request.method == "POST":
        m=sql.connect(host="localhost",user= "root", password="Aashi@25111997",database ="DanceWebsite")
        cursor = m.cursor()
        d = request.POST
        for key,value in d.items():
            if key=="f_name":
                fn = value
            if key == "l_name":
                ln = value
            if key == "joining_date":
                jd = value
            if key == "learn_month":
                dd = value
            if key == "i_d":
                id = value
        c= "insert into users('{}','{}','{}','{}','{}')".format(fn,ln,jd,dd,id)
        cursor.execute(c)
        m.commit()

    return  render(request,'registration.html')

