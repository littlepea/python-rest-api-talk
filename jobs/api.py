"""API to get skills by job title"""
import hug

from jobs.services import get_top_skills_for_job_title


@hug.get()
def top_skills(title: hug.types.text):
    """Get skills by a job title"""
    skills = get_top_skills_for_job_title(title)
    return {'skills': [
        {'name': s.name,
         'score': s.score} for s in skills
    ]}


if __name__ == '__main__':
    top_skills.interface.cli()
