from collectors.linkedin import fetch_linkedin_jobs
from filters.skills import has_mandatory_skills
from filters.experience import senior_role
from scoring.score import score_job
from db.database import save_job
from notify.email import send_email
from config import MIN_SCORE

def run():
    alerts = []
    jobs = fetch_linkedin_jobs()

    for job in jobs:
        if not has_mandatory_skills(job["description"]):
            continue
        if not senior_role(job["description"]):
            continue

        job["score"] = score_job(job["description"])

        if job["score"] >= MIN_SCORE:
            if save_job(job):
                alerts.append(job)

    send_email(alerts)

if _name_ == "_main_":
    run()
