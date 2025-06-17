#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    req = requests.get(url)
    print(f"Status Code: {req.status_code}")

    if response.status_code == 200:
		posts = response.json()
		for post in posts:
			print(post['title'])







def fetch_and_save_posts():