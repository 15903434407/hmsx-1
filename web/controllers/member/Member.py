from flask import Blueprint,request,redirect,jsonify
from common.libs.Helper import ops_render


router_member = Blueprint("member_page",__name__)

@router_member.route("/index")
def index():
    return ops_render("member/index.html")

@router_member.route("/info")
def info():
    return ops_render("member/info.html")

@router_member.route("/set")
def set():
    return ops_render("member/set.html")

@router_member.route("/comment")
def comment():
    return ops_render("member/comment.html")
