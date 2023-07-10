from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Truyền mỗi truyền cho hệ thống hoạt động
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class VideoModel(db.Model):
    # Tạo các kiểu dữ liệu cho hệ cơ sở dữ liệu
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'video(name={self.name},views={self.views})'


video_put_args = reqparse.RequestParser()
video_put_args.add_argument(
    'name', type=str, help='name of the video', required=True)
video_put_args.add_argument(
    'views', type=int, help='views of the video', required=True)
video_put_args.add_argument(
    'likes', type=int, help='likes of the video', required=True)

video_update_put_args = reqparse.RequestParser()
video_update_put_args.add_argument(
    'name', type=str, help='name of the video')
video_update_put_args.add_argument(
    'views', type=int, help='views of the video')
video_update_put_args.add_argument(
    'likes', type=int, help='likes of the video')
resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='coul not find video with that id')
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        # thuc hien ktra xem co so du lieu da co ton tai trong he thong hay khong
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message='video id taken...')
        video = VideoModel(name=args['name'],
                           views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201
    # thưc hiện cập nhật cơ sở dữ liệu

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="video doesn't exist,cannot update")
        if 'name' in args:
            result.name = args['name']
        if 'views' in args:
            result.views = args['views']
        if 'likes' in args:
            result.likes = args['likes']
        # db.session.add(result)
        db.session.commit()
        return result


api.add_resource(Video, '/video/<int:video_id>')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
