from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import json
import os
from toolz import memoize

app = FastAPI()

# TODO: Change origin to real domain to reject Ajax requests from elsewhere
app.add_middleware(CORSMiddleware, allow_origins=['*'])

@memoize
def data():
    with open(os.path.join(os.path.dirname(__file__), 'esv.json')) as f:
        return json.load(f)


@app.get('/api/verse/{book}/{chapter}/{verse}')
def load_text(book: str, chapter: int, verse: int):
    try:
        return {'text': data()[book][str(chapter)][str(verse)]}
    except KeyError as e:
        return {'error': str(e), 'type': 'KeyError'}

