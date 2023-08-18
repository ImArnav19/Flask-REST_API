from flask import Flask, abort
from flask_restful import Api, Resource, reqparse , fields, marshal_with
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VidModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    views = db.Column(db.Integer)
    likes = db.Column(db.Integer)

    def __repr__(self):
        return f"Video(name -> {name},)"



vid_args = reqparse.RequestParser()
vid_args.add_argument("name",type=str,help ="Name of the video")
vid_args.add_argument("views",type=int,help ="Views of the video")
vid_args.add_argument("likes",type=int,help ="Likes of the video")

res_fields = {
    'id' : fields.Integer(),
    'name' : fields.String(),
    'views' : fields.Integer(),
    'likes' : fields.Integer(),
    
}


class video(Resource):
    @marshal_with(res_fields)
    def get(self,vid_id):
        res = VidModel.query.filter_by(id=vid_id).first()
        if res:
            return res
        else:
            abort(400,"No video")


        
        
    @marshal_with(res_fields)
    def post(self,vid_id):
        args = vid_args.parse_args()
        
        res = VidModel.query.filter_by(id=vid_id).first()
        if res:
            abort(400," video Taken!!")
        else:
            save = VidModel(id=vid_id, name=args['name'],likes=args['likes'],views=args['views'])
            db.session.add(save)
            db.session.commit()
            return save , 201
            
        
        
    @marshal_with(res_fields)
    def delete(self,vid_id):
        res = VidModel.query.filter_by(id=vid_id).first()
        if res:
            
            
            
            obj = VidModel.query.filter_by(id=vid_id).one()
            db.session.delete(obj)
            db.session.commit()
            return obj , 201
        else:
            abort(401, "No video!")
    
api.add_resource(video,'/hw/<int:vid_id>')

if __name__ == "__main__":
    app.run(debug=True)