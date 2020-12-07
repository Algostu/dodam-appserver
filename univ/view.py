import json, time
import pandas as pd

from flask import send_file
from flask import escape, Blueprint, request, session, current_app as app
from sqlalchemy import text, desc

from main.extensions import *
from main.model import *

univ_api = Blueprint('univ', __name__, url_prefix='/univ')

@univ_api.route('/viewUniv', methods=['GET'])
@login_required
def get_viewUniv():
    univ_id = int(request.args.get('univID'))
    univ = UnivInfo.query.filter_by(univID=univ_id).first()
    if not univ:
        return response_with_code("<fail>:2:no university")
    if not univ.viewNumber:
        univ.viewNumber = 0
    univ.viewNumber += 1
    db.session.commit()
    return response_with_code("<success>")

@univ_api.route('/viewMajor', methods=['GET'])
@login_required
def get_viewMajor():
    major_id = int(request.args.get('majorID'))
    major = MajorInfo.query.filter_by(majorID=major_id).first()
    if not major:
        return response_with_code("<fail>:2:no university")

    if not major.viewNumber:
        major.viewNumber = 0
    major.viewNumber += 1
    db.session.commit()
    return response_with_code("<success>")

@univ_api.route('/ranking', methods=['GET'])
@login_required
def get_ranking():
    # this is server-side query.
    univs = UnivInfo.query.order_by(desc(UnivInfo.viewNumber)).limit(5).all()
    majors = MajorInfo.query.order_by(desc(MajorInfo.viewNumber)).limit(5).all()
    univs = [convert_to_dict(univ) for univ in univs]
    majors = [convert_to_dict(major) for major in majors]
    if not majors or not univs:
        return response_with_code("<fail>:2:server got problem")

    return response_with_code("<success>", {"univList":univs,"majorList":majors})

@univ_api.route('/logoImage', methods=['GET'])
@login_required
def get_logImage():
    # this is server-side query.
    # trim 고,등,학,교 off
    univ_id = int(request.args.get('univID'))
    print(univ_id)
    univ = UnivInfo.query.filter_by(univID=univ_id).first()
    if not univ.logoPossible:
        return response_with_code("<fail>:2:no logo are prepared")

    signiture_path = 'crawler/data/signiture/' + univ.univName + ".png" # point to your image location
    signiture_img = get_response_image(signiture_path)
    symbol_path = 'crawler/data/symbol/' + univ.univName + ".png" # point to your image location
    symbol_img = get_response_image(symbol_path)

    return response_with_code("<success>", {'symbol': symbol_img, 'signiture': signiture_img})

@univ_api.route('/liveShowList', methods=['GET'])
@login_required
def get_live_show_list():
    writtenAfter = request.args.get('writtenAfter')

    if writtenAfter == 'latest':
        rows = LiveShow.query.order_by(desc(LiveShow.writtenTime)).limit(15).all()
    else:
        rows = LiveShow.query.filter(LiveShow.writtenTime<writtenAfter).\
        order_by(desc(LiveShow.writtenTime)).limit(15).all()
    live_shows = []
    for row in rows:
        dict_row = convert_to_dict(row)
        dict_row.pop('userID')
        live_shows.append(dict_row)

    return response_with_code("<success>", live_shows)
