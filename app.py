from flask import Flask, request, jsonify
from analysis import get_movie_objs

app = Flask(__name__)

output = {}


@app.route('/', methods=['GET'])
def mood_analysis():
    movie_list = request.args.getlist('movie_list')
    kodi_ids = request.args.getlist('kodi_ids')

    sent = get_movie_objs(movie_list, kodi_ids)
    return jsonify(sent)


if __name__ == '__main__':
    app.run()