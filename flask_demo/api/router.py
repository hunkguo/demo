from flask import jsonify, request
from app import bp

from api.models import *
from app import db
from error import bad_request


@bp.route('/', methods=['GET'])
def get_users():
    limit = min(request.args.get('limit', 10, int), 100)
    offset = (request.args.get('page', 1, int) - 1) * request.args.get('limit', 10, int)
    return jsonify([user.to_dict() for user in User.query.limit(limit).offset(offset).all()])



@bp.route('/videolist', methods=['GET'])
def youtubeVideoList():
    limit = min(request.args.get('limit', 10, int), 100)
    offset = (request.args.get('page', 1, int) - 1) * request.args.get('limit', 10, int)
    return jsonify([yv.to_dict() for yv in YoutubeVideo.query.filter(YoutubeVideo.isDownload==True).limit(limit).offset(offset).all()])


@bp.route('/savevideolist', methods=['POST'])
def saveYoutubeVideo():

    link = request.json['link']

    yv = YoutubeVideo(link=link,isDownload=True)
    db.session.add_all([yv])
    db.session.commit()

    return jsonify({'success':True}), 200, {'ContentType':'application/json'} 