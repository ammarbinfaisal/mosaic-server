# from flask import Flask, jsonify, request
# from bcrypt import hashpw, gensalt, checkpw
# from . import app, db, schema

# # ----------------------------
# # USERS
# # ----------------------------

# @app.route("/u/create", methods=["POST"])
# def register():
#     b = request.get_json()
#     try:
#         schema.login_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     if db.User.query.filter_by(name=b["username"]).first():
#         return "Username already exists", 400
#     hashed = hashpw(b["password"].encode("utf-8"), gensalt())
#     user = db.User(name=b["username"], password=hashed)
#     db.session.add(user)
#     db.session.commit()
#     return "OK", 200

# @app.route("/u/login", methods=["POST"])
# def login():
#     b = request.get_json()
#     try:
#         schema.login_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     user = db.User.query.filter_by(name=b["username"]).first()
#     if checkpw(b["password"].encode("utf-8"), user.password):
#         return "OK", 200
#     return "Incorrect password", 401

# @app.route("/u/<int:user_id>/posts", methods=["GET"])
# def get_user_posts(user_id):
#     posts = db.Post.query.filter_by(user_id=user_id).all()
#     return jsonify([post.to_dict() for post in posts]), 200

# @app.route("/u/<int:user_id>/comments", methods=["GET"])
# def get_user_comments(user_id):
#     comments = db.Comment.query.filter_by(user_id=user_id).all()
#     return jsonify([comment.to_dict() for comment in comments]), 200

# # ----------------------------
# # POSTS
# # ----------------------------

# @app.route("/p/create", methods=["POST"])
# def create_post():
#     b = request.get_json()
#     try:
#         schema.create_post_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     post = db.Post(
#         title=b["title"],
#         content=b["content"],
#         user_id=b["user_id"],
#         community_id=b["community_id"],
#         display_pic=b["display_pic"],
#     )
#     db.session.add(post)
#     db.session.commit()
#     return "OK", 200

# @app.route("/p/<int:post_id>/comments", methods=["GET"])
# def get_post_comments(post_id):
#     comments = db.Comment.query.filter_by(post_id=post_id).all()
#     return jsonify([comment.to_dict() for comment in comments]), 200

# @app.route("/p/update", methods=["POST"])
# def update_post():
#     b = request.get_json()
#     try:
#         schema.update_post_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     post = db.Post.query.get(b["id"])
#     post.title = b["title"]
#     post.content = b["content"]
#     post.display_pic = b["display_pic"]
#     db.session.commit()
#     return "OK", 200

# # ----------------------------
# # COMMUNITIES
# # ----------------------------

# @app.route("/c/create", methods=["POST"])
# def create_community():
#     b = request.get_json()
#     try:
#         schema.create_community_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     community = db.Community(
#         name=b["name"], description=b["description"], display_pic=b["display_pic"]
#     )
#     db.session.add(community)
#     db.session.commit()
#     return "OK", 200

# @app.route("/c/get", methods=["GET"])
# def get_communities():
#     communities = db.Community.query.all()
#     return jsonify([community.to_dict() for community in communities]), 200

# @app.route("/c/update", methods=["POST"])
# def update_community():
#     b = request.get_json()
#     try:
#         schema.update_community_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     community = db.Community.query.filter_by(id=b["id"]).first()
#     if b["name"]:
#         community.name = b["name"]
#     if b["description"]:
#         community.description = b["description"]
#     if b["display_pic"]:
#         community.display_pic = b["display_pic"]
#     db.session.commit()
#     return "OK", 200

# # ----------------------------
# # COMMENTS
# # ----------------------------


# @app.route("/cm/create", methods=["POST"])
# def create_comment():
#     b = request.get_json()
#     try:
#         schema.create_comment_schema.load(b)
#     except schema.ValidationError as err:
#         return err.messages, 400
#     comment = db.Comment(
#         content=b["content"],
#         user_id=b["user_id"],
#         post_id=b["post_id"],
#         parent_id=b["parent_id"],
#     )
#     db.session.add(comment)
#     db.session.commit()
#     return "OK", 200

