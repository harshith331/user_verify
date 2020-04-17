import schedule
from schedule import * 
from celery import Celery
from celery.schedules import crontab
from django.utils.timezone import datetime
from datetime import datetime,date

############################      using python scheduler   ################################


### sample format of start date and time ###
start_date="2020-02-16"
end_date="2020-08-16"
date_time=["2020-04-17 11:33:11",
            "2020-04-17 11:33:13",
            "2020-04-17 11:33:15",
            "2020-04-17 11:33:17",]


#############################################

#### main task 
def task():
    print("hello")


#### scheduler task 
def schdl():
    start_dt=datetime.strptime(start_date, "%Y-%m-%d").date()
    end_dt  =datetime.strptime(end_date, "%Y-%m-%d").date()
    if date.today()<= end_dt and date.today()>= start_dt:
        for dt_time in date_time: 
            dt_obj=datetime.strptime(dt_time, '%Y-%m-%d %H:%M:%S')
            if datetime.now()==dt_obj:
                task()
            # if datetime.now()==dt_timr
    

schedule.every(2).seconds.do(schdl)

while(True):
    schedule.run_pending()
    time.sleep(1)

####################################################################################################

######################################### in settings.py ###########################################

# INSTALLED_APPS = (
#     'django_crontab',
#     ...
# )


# CRONJOBS = [
#     ('*/5 * * * *', 'schdule_.schdl')
# ]


# # run command to add cron jobs # #
# $ python manage.py crontab add

####################################################################################################