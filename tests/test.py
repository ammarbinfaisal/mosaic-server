import requests
from random import choice

alpha = "abcdefghijklmnopqrstuvwxyz"
nums = "0123456789"

API_URL = "http://localhost:5000"

auth_token = None

def set_auth_token(token):
    print("Setting auth token", token)
    global auth_token
    auth_token = token


def rand_text():
    return "".join(choice(alpha) for _ in range(10))


def register(username, password):
    return requests.post(f"{API_URL}/u/create", json={"username": username, "password": password}, headers={"Authorization": auth_token})


def login(username, password):
    return requests.post(f"{API_URL}/u/login", json={"username": username, "password": password}, headers={"Authorization": auth_token})


def create_community(name, description, display_pic):
    return requests.post(f"{API_URL}/c/create", json={"name": name, "description": description, "display_pic": display_pic}, headers={"Authorization": auth_token})


def get_communities():
    return requests.get(f"{API_URL}/c/get", headers={"Authorization": auth_token})


def create_post(title, content, community_id, display_pic):
    return requests.post(f"{API_URL}/p/create", json={"title": title, "content": content, "community_id": community_id, "display_pic": display_pic}, headers={"Authorization": auth_token})


def update_post(id, title, content, display_pic):
    return requests.post(f"{API_URL}/p/update", json={"id": id, "title": title, "content": content, "display_pic": display_pic}, headers={"Authorization": auth_token})


def create_comment(content, user_id, post_id):
    return requests.post(f"{API_URL}/cm/create", json={"content": content, "user_id": user_id, "post_id": post_id}, headers={"Authorization": auth_token})


def update_comment(id, content):
    return requests.post(f"{API_URL}/cm/update", json={"id": id, "content": content}, headers={"Authorization": auth_token})


if __name__ == "__main__":
    # register a user
    username = rand_text()
    password = rand_text()
    register(username, password)
    # login with the user
    u = login(username, password).text
    set_auth_token(u)
    # create a community
    name = rand_text()
    description = rand_text()
    display_pic = rand_text()
    create_community(name, description, display_pic)
    # get all communities
    print(get_communities().text)
    # create a post
    title = rand_text()
    content = rand_text()
    community_id = 1
    display_pic = rand_text()
    p = create_post(title, content, community_id, display_pic)
    print("post", p.text)
