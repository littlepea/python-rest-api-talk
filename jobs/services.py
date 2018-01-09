from functools import lru_cache

from jobs.dataatwork import DataAtWorkAPIAdapter as skills_service


@lru_cache()
def get_top_skills_for_job_title(title):
    skills = skills_service.related_skills_by_title(title)
    top_skills = [skill for skill in reversed(sorted(skills, key=lambda x: x.score))][:10]
    return top_skills
