from flask import Flask, render_template

from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

"""
candidates = load_candidates_from_json('candidates.json') загружает данные в каждом руте на случай внесения изменений в
файл json, пусть в данном случае изменений не происходит
"""


@app.route("/")
def page_candidates():
    candidates = load_candidates_from_json('candidates.json')
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:candidate_id>")
def page_candidate(candidate_id):
    candidates = load_candidates_from_json('candidates.json')
    candidate = get_candidate(candidates, candidate_id)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<candidate_name>")
def page_name_candidate(candidate_name):
    candidates = load_candidates_from_json('candidates.json')
    candidate = get_candidates_by_name(candidates, candidate_name)
    return render_template('search.html', candidates=candidate, count_candidates=len(candidate))


@app.route("/skill/<skill_name>")
def page_skill_candidate(skill_name):
    candidates = load_candidates_from_json('candidates.json')
    candidate = get_candidates_by_skill(candidates, skill_name)
    return render_template('skill.html', candidates=candidate, count_candidates=len(candidate))


if __name__ == '__main__':
    app.run()
