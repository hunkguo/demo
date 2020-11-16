from flask import jsonify, request
from main import db
from error import bad_request


@bp.route('/', methods=['GET'])
def get_users():
    limit = min(request.args.get('limit', 10, int), 100)
    offset = (request.args.get('page', 1, int) - 1) * request.args.get('limit', 10, int)
    return jsonify([user.to_dict() for user in User.query.limit(limit).offset(offset).all()])



@bp.route('/videolist', methods=['GET'])
def youtubeVideoList():
    #limit = min(request.args.get('limit', 10, int), 100)
    #offset = (request.args.get('page', 1, int) - 1) * request.args.get('limit', 10, int)
    #return jsonify([yv.to_dict() for yv in YoutubeVideo.query.filter(YoutubeVideo.isDownload==True).limit(limit).offset(offset).all()])
    return jsonify([yv.to_dict() for yv in YoutubeVideo.query.filter(YoutubeVideo.isDownload==True).all()])


@bp.route('/savevideolist', methods=['POST'])
def saveYoutubeVideo():

    link = request.json['link']
    if (YoutubeVideo.query.filter(YoutubeVideo.link==link).first()):
        return jsonify({'error': 'duplicate'}), 200, {'ContentType':'application/json'}
    else:
        yv = YoutubeVideo(link=link,isDownload=False)        
        db.session.add(yv)
        db.session.commit()

        return jsonify({'success':True}), 200, {'ContentType':'application/json'} 


@bp.route('/nodownloadvideolist', methods=['GET'])
def nodownloadvideolist():
    limit = min(request.args.get('limit', 10, int), 100)
    offset = (request.args.get('page', 1, int) - 1) * request.args.get('limit', 10, int)
    return jsonify([yv.to_dict() for yv in YoutubeVideo.query.filter(YoutubeVideo.isDownload==False).limit(limit).offset(offset).all()])


@bp.route('/savedownloadvideo', methods=['POST'])
def savedownloadvideo():
    
    yv = YoutubeVideo.query.get(request.json['id'])
    yv.isDownload=True
    yv.videoTitle = request.json['title']
    yv.downloadFile = request.json['file']

    
    yv.videoUploader = request.json['uploader']
    yv.videoChannelUrl =request.json['channel_url']
    yv.videoUploadDate = request.json['upload_date']
    yv.videoThumbnail = request.json['thumbnail']
    yv.videoDescription = request.json['desc'].replace('\n', '').replace('\r', '')
    yv.videoDuration = request.json['duration']
    yv.videoViewCount = request.json['view_count']
    yv.videoLikeCount = request.json['like_count']
    yv.videoDislikeCount = request.json['dislike_count']
    yv.videoAverageRating =request.json['average_rating']
    db.session.commit()

    return jsonify({'success':True}), 200, {'ContentType':'application/json'} 


@bp.route('/getvideo/<id>', methods=['GET'])
def getvideo(id):
    
    yv = YoutubeVideo.query.get(id)

    return jsonify(yv.to_dict())
