from flask import Blueprint,render_template,request,jsonify,redirect,session
from exts import mail,db
from flask_mail import Message
import string
import random
from models import EmailCaptchaModel,UserModel
from .forms import RegisterForm,LoginForm
from werkzeug.security import generate_password_hash,check_password_hash


bp = Blueprint('auth',__name__,url_prefix = '/auth')

@bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                print("邮箱在数据库中不存在！")
                return redirect('auth/login')
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                return redirect('/')
            else:
                print("密码错误!")
                return redirect('/')
        else:
            print(form.errors)
            return redirect('/auth/login')

@bp.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username, password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            return redirect("/auth/login")
        else:
            print(form.errors)
            return redirect("/auth/register")

@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get("email")
    source = string.digits*6
    captcha = random.sample(source, 6)
    captcha = "".join(captcha)
    message = Message(subject="博客验证码",recipients=[email], body=f'这是一条超级无敌巨帅的博客网站注册验证码:\n{captcha}')
    mail.send(message)

    email_captcha = EmailCaptchaModel(email = email,captcha = captcha)
    db.session.add(email_captcha)
    db.session.commit()
 
    return jsonify({"code": 200,"message":"","data":None})


@bp.route('logout')
def logout():
    session.clear()
    return redirect('/')