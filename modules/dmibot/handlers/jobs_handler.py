import telegram, yaml, logging

from modules.dmibot.handlers.jobs.dummy import dummy_job

def schedule_jobs(job_queue):
    job_queue.run_repeating(dummy_job, interval=5*60)