import requests

from .entities import Skill


def skill_score(skill):
    importance = skill['importance'] * 2
    level = skill['level']
    score = importance * 0.4 + level * 0.6
    return score


class DataAtWorkAPIAdapter:
    API_ROOT = 'http://api.dataatwork.org/v1/'

    @classmethod
    def _build_url(cls, collection=None, id=None, related=None):
        detail_path = f'/{id}' if id else ''
        related_path = f'/{related}' if related else ''
        return f'{cls.API_ROOT}{collection}{detail_path}{related_path}'

    @classmethod
    def _request(cls, collection=None, id=None, related=None, data=None):
        url = cls._build_url(collection, id, related)
        return requests.get(url, data).json()

    @classmethod
    def jobs(cls, title):
        return cls._request('jobs/autocomplete', data={'begins_with': title})

    @classmethod
    def job(cls, job_id):
        return cls._request('jobs', job_id)

    @classmethod
    def job_by_title(cls, title):
        jobs = cls.jobs(title)
        return jobs[0]

    @classmethod
    def related_skills(cls, job_id):
        return cls._request('jobs', job_id, 'related_skills')['skills']

    @classmethod
    def related_skills_by_title(cls, title):
        job_id = cls.job_by_title(title)['uuid']
        related_skills = cls.related_skills(job_id)
        return [Skill(s['skill_name'], skill_score(s)) for s in related_skills]
