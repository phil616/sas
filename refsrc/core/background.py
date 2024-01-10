"""


"""
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.schedulers.background import BackgroundScheduler
from config import appcfg


def generate_background_scheduler() -> BackgroundScheduler:
    """
    通过配置文件生成一个后台任务调度器
    :return:
    """
    url = appcfg.MYSQL_JOB_STORE_URL
    aps_bg_scheduler = BackgroundScheduler()
    aps_bg_job_store = SQLAlchemyJobStore(url=url)
    # 这个Job Store曾经一度无法使用，无法从MYSQL中读取，但不知道为何又能使用了
    # 现在经过测试是能使用的，如果不能使用就用Navicat看一看Job库里面有没有记录
    aps_bg_scheduler.add_jobstore(aps_bg_job_store)
    return aps_bg_scheduler

def BGK_export_schedule_list():
    ...

def BGK_daily_summary():
    ...
