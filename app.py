from flask import Flask,session,g
import config
from exts import db,mail
from models import UserModel
from BluePrints.qa import bp as qa_bp
from BluePrints.auth import bp as auth_bp
from flask_migrate import Migrate

app = Flask(__name__)
#绑定配置文件
app.config.from_object(config)

#绑定数据库
db.init_app(app)
#绑定邮箱
mail.init_app(app)

migrate = Migrate(app, db)
# flask db init
# flask db migrate
# flask db upgrade

#绑定蓝图
app.register_blueprint(qa_bp)
app.register_blueprint(auth_bp)

#hook
@app.before_request
def my_before_request():
    user_id = session.get("user_id")
    if user_id:
        user = UserModel.query.get(user_id)
        setattr(g,"user",user)
    else:
        setattr(g,"user",None)


@app.context_processor
def my_context_processor():
    return {"user": g.user}


if __name__ == '__main__':
    app.run(debug=True)