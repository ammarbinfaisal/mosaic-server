from sqlalchemy import Column, DateTime, Integer, Boolean, Text, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,scoped_session, relationship
from sqlalchemy.sql import func

DATABASE_URL = "mysql+pymysql://root:p@localhost:3306/cop"

engine = create_engine(
    DATABASE_URL,
)

session_factory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = scoped_session(session_factory)
session = Session()

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True,
                autoincrement=True, unique=True)
    username = Column(Text)
    email = Column(Text)
    password = Column(Text)
    display_pic = Column(Text)

    last_login = Column(DateTime, server_default=func.now())
    time_joined = Column(DateTime, server_default=func.now())

    # user_preference = Column(Integer)
    user_status = Column(Integer)


class Vote(Base):
    __tablename__ = "votes"
    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    upvote = Column(Boolean)
    user = relationship("User", foreign_keys="Vote.user_id")
    post = relationship("Post", foreign_keys="Vote.post_id")


class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    display_pic = Column(Text)
    downvotes = Column(Integer, default=0)
    is_deleted = Column(Boolean)
    post_id = Column(Integer)
    time_created = Column(DateTime, server_default=func.now())
    title = Column(Text)
    upvotes = Column(Integer, default=0)
    view_count = Column(Integer, default=0)
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    community_id = Column(ForeignKey(
        "communities.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="Post.user_id")
    community = relationship("Community", foreign_keys="Post.community_id")


class Moderator(Base):
    __tablename__ = "moderators"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    community_id = Column(ForeignKey(
        "communities.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="Moderator.user_id")
    community = relationship(
        "Community", foreign_keys="Moderator.community_id")


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="History.user_id")
    post = relationship("Post", foreign_keys="History.post_id")


class FollowUser(Base):
    __tablename__ = "follow_users"
    id = Column(Integer, primary_key=True, index=True)
    follower = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    following = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    time = Column(DateTime, server_default=func.now())


class Community(Base):
    __tablename__ = "communities"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True)
    description = Column(Text)
    display_pic = Column(Text)
    is_banned = Column(Boolean, default=0)
    is_deleted = Column(Boolean, default=0)
    time_created = Column(DateTime, server_default=func.now())
    sub_count = Column(Integer, default=1)
    admin_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    created_by_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    admin = relationship("User", foreign_keys="Community.admin_id")
    created_by = relationship("User", foreign_keys="Community.created_by_id")


class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    downvotes = Column(Integer, default=0)
    is_deleted = Column(Boolean)
    parent_comment = Column(ForeignKey(
        "comments.id", ondelete="CASCADE"), nullable=True)
    time_created = Column(DateTime, server_default=func.now())
    upvotes = Column(Integer, default=0)
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="Comment.user_id")
    post = relationship("Post", foreign_keys="Comment.post_id")


class SubscribedCommunity(Base):
    __tablename__ = "subscribed_communities"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    community_id = Column(ForeignKey(
        "communities.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="SubscribedCommunity.user_id")
    community = relationship(
        "Community", foreign_keys="SubscribedCommunity.community_id")


class SavedPost(Base):
    __tablename__ = "saved_posts"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="SavedPost.user_id")
    post = relationship("Post", foreign_keys="SavedPost.post_id")


class SavedComment(Base):
    __tablename__ = "saved_comments"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    comment_id = Column(ForeignKey(
        "comments.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="SavedComment.user_id")
    comment = relationship("Comment", foreign_keys="SavedComment.comment_id")


class CommentVote(Base):
    __tablename__ = "comment_votes"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    is_upvote = Column(Boolean)
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    comment_id = Column(ForeignKey(
        "comments.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="CommentVote.user_id")
    comment = relationship("Comment", foreign_keys="CommentVote.comment_id")


class BlockedUser(Base):
    __tablename__ = "blocked_users"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    blocker_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    blocked_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    blocker = relationship("User", foreign_keys="BlockedUser.blocker_id")
    blocked = relationship("User", foreign_keys="BlockedUser.blocked_id")


class View(Base):
    __tablename__ = "views"
    id = Column(Integer, primary_key=True, index=True)
    time = Column(DateTime, server_default=func.now())
    user_id = Column(ForeignKey(
        "users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(ForeignKey(
        "posts.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User", foreign_keys="View.user_id")
    post = relationship("Post", foreign_keys="View.post_id")


def migrate():
    tables = [
        User,
        Community,
        Post,
        Vote,
        Comment,
        SubscribedCommunity,
        SavedPost,
        SavedComment,
        Moderator,
        History,
        FollowUser,
        CommentVote,
        BlockedUser,
        View
    ]
    for table in tables:
        table.__table__.create(bind=engine, checkfirst=True)


migrate()
