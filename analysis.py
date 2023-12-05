import json
import nltk
from imdb import Cinemagoer
from nltk.sentiment import SentimentIntensityAnalyzer
import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


np.random.seed(0)


def calculate_happiness_vader(text):
    nltk.download('vader_lexicon')
    analyzer = SentimentIntensityAnalyzer()
    sentiment_scores = analyzer.polarity_scores(text)
    happiness_score = sentiment_scores['compound']
    return happiness_score


def has_duplicates(json_list, key, value):
    for json_obj in json_list:
        if json_obj.get(key) == value:
            return True  # Duplicate found
    return False  # No duplicates found


def get_movie_description(title):
    ia = Cinemagoer()
    description = ""
    movie = ia.get_movie(ia.search_movie(title)[0].movieID)
    plots = movie.get('plot')
    for plot in plots:
        description = description + plot + " "
    for genre in movie.get('genre'):
        description = description + genre + " "
        description = description + genre + " "
    return description


# modify this to return a dictionary
def get_movie_objs(movie_list, kodi_id_list):
    ia = Cinemagoer()
    # add check somewhere in here to make sure the list of movie titles and kodi id's are the same length
    movie_jsons = []
    for index, title in enumerate(movie_list):

        description = get_movie_description(title)

        happy_value = sad_value = 0
        happy_sad = calculate_happiness_vader(description)
        # happiness and sadness are inverses, so if a movie has a negative result, we make happiness 0, and sadness
        # the absolute value
        if happy_sad < 0:
            sad_value = abs(happy_sad)
        else:
            happy_value = happy_sad


        obj = {"title": title,
               "path": kodi_id_list[index],
               "imdb_id": ia.search_movie(title)[0].movieID,
               "happy": happy_value,
               "sad": sad_value,
               "scary": calculate_similarity(scary_terms(), description),
               "relaxed": calculate_similarity(relaxing_terms(), description),
               "romantic": calculate_similarity(romantic_terms(), description),
               "platonic": calculate_similarity(platonic_terms(), description),
               "mindless": calculate_similarity(mindless_terms(), description),
               "thought-provoking": calculate_similarity(thought_provoking_terms(), description),
               "slow-paced": calculate_similarity(slow_paced_terms(), description),
               "action-packed": calculate_similarity(action_packed_terms(), description)
               }

        movie_jsons.append(obj)

    return movie_jsons


def calculate_similarity(term, document):
    nlp = spacy.load("en_core_web_md")
    if document == "":
        return 0
    # Preprocess the term and document
    term_vector = nlp(term).vector.reshape(1, -1)
    document_vector = nlp(document).vector.reshape(1, -1)
    # Calculate cosine similarity between the term and the document
    similarity = float(cosine_similarity(term_vector, document_vector)[0][0])

    return similarity

def scary_terms():
    return "scary frightening sinister spine-tingling phantasm ghostly spooky desolation strange creepy dread ghostly haunting phantom unearthly horror"

def relaxing_terms():
    return "soothing calm gentle tranquil serene cozy peaceful blissful comforting hugs mellow harmony pleasant easygoing"

def romantic_terms():
    return "romantic sweet tender passionate intimate gentle romantic heartfelt affectionate everlasting"

def platonic_terms():
    return "platonic friendly companionship cooperative collaborative respectful empathetic encouraging caring considerate warm-hearted genuine sincere kind-hearted cooperative amicable harmonious affable companionable comradeship camaraderie loyal comrades mutual companions"

def mindless_terms():
    return "mindless slapstick quirky wacky goofy mundane"

def thought_provoking_terms():
    return "thought-provoking philosophical dilemma existential reflections moral quandaries intellectual puzzles ethical deep introspection profound revelation complex moralities multilayered narratives ambiguous resolutions symbolic imagery emotional depth toughtful dialogues inner conflicts cognitive ambivalent"

def slow_paced_terms():
    return "slow-paced soothing gentle leisurely reflective solitude tranquil settings calm contemplation unhurried moments serene atmospheres meandering narratives slow"

def action_packed_terms():
    return "action-packed fast-paced sequences intense fights explosive showdowns daring stunts high-speed chases dramatic escapes epic battles adrenaline-pumping moments non-stop action heart-pounding thrills relentless pursuit high-octane energy dynamic cinematography thrilling encounters exhilarating escapades breathtaking stunts over-the-top sequences "

