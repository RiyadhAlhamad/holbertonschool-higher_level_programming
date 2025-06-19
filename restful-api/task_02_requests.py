#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    responed = requests.get(url)
    print(f"Status Code: {responed.status_code}")

    if responed.status_code == 200:
        posts = responed.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    responed = requests.get(url)

    if responed.status_code == 200:
        all_posts = responed.json()
        list_posts = [{'id' : post['id'], 'title' : post['title'], 'body' : post['body']} for post in all_posts]

    with open('posts.csv', mode='w', newline='', encoding='utf-8') as csvfile:
            my_field = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=my_field)

            writer.writeheader()
            writer.writerows(list_posts)
