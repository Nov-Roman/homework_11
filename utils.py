import json


def load_candidates_from_json(file_name: json) -> list:
    """
    :return: список кандидатов
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        candidates = json.load(file)
    return candidates


def get_candidate(candidates: list, candidate_id: int) -> dict:
    """
    :return: кандидат по его id
    """
    for candidate in candidates:
        if candidate["id"] == candidate_id:
            return candidate


def get_candidates_by_name(candidates: list, candidate_name: str) -> list:
    """
    :return: список кандидатов по имени
    """
    candidates_name = []
    for candidate in candidates:
        if candidate_name.lower() in candidate["name"].lower():
            candidates_name.append(candidate)
    return candidates_name


def get_candidates_by_skill(candidates: list, skill_name: str) -> list:
    """
    :return: список кандидатов по навыкам
    """
    candidates_skill = []
    for candidate in candidates:
        if skill_name.lower() in candidate["skills"].lower().split(', '):
            candidates_skill.append(candidate)
    return candidates_skill
