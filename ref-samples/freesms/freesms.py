#!/usr/bin/python3
import requests
requests.post('https://textbelt.com/text', {
  'phone': '+919766925741',
  'message': 'Hello world',
  'key': 'textbelt',
})
