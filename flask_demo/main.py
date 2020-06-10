from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__
            )
CORS(app)
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://demo:ghlhj2891@localhost/demo'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


from flask import Blueprint
bp = Blueprint('api', __name__)
from api.router import *

app.register_blueprint(bp, url_prefix='/api')


from api.models import *

@app.route('/', methods=['GET'])
def home():
    return jsonify('It''s work.')


if __name__ == '__main__':
    
    #db.drop_all()
    db.create_all()

    #us1 = User(name='zhangsan')
    #us2 = User(name='lisi')

    #yv1 = YoutubeVideo(link='https://www.youtube.com/watch?v=itUoWLU3EWU',isDownload=False)
    #yv2 = YoutubeVideo(link='https://www.youtube.com/watch?v=CWxuTYEt0pc',isDownload=False)
    #yv3 = YoutubeVideo(link='https://www.youtube.com/watch?v=pLMMKwikHK4',isDownload=False)
    #yv4 = YoutubeVideo(link='https://www.youtube.com/watch?v=Xs1wVkkxpoI',isDownload=False)
    #yv5 = YoutubeVideo(link='https://www.youtube.com/watch?v=QFDyzfSG80o',isDownload=False)
    #db.session.add_all([us1, us2, yv1, yv2, yv3, yv4, yv5])
    #db.session.commit()





    app.run(host='0.0.0.0', port='5000', debug=True)
