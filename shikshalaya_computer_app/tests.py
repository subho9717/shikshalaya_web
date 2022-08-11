from django.test import TestCase

# Create your tests here.
import psycopg2
import pandas as pd
import datetime
# from  mysql.connector import connect


conn = psycopg2.connect(
        host="satao.db.elephantsql.com",
        database="bhkpnqch",
        user="bhkpnqch",
        password="u5N4eHFTnwxRj9XhlTMPhqy3kudxnqR0")
cursor = conn.cursor()
# df = pd.read_sql_query("select mf.month ,sum(mf.month_fees) as month_fees ,sum(cs.registration_fees) as registration_fees from shikshalaya_computer_app_computer_student_monthly_fees as mf inner join shikshalaya_computer_app_computer_student as cs on mf.month = cs.month group by mf.month, cs.month",conn)
#
# ce = pd.read_sql_query('select month,sum("Amount") as expenses_amount from shikshalaya_computer_app_computer_expenses group by month',conn)
# fnl = df.merge(ce,how = 'inner',on='month')
# fnl['registration_fees_share'] = fnl['registration_fees']/2
# fnl['expenses_share'] = fnl['expenses_amount']/2
# fnl['employee_share'] = (fnl['month_fees']*55)/100
# fnl['rupam_subhajit_share'] = (fnl['month_fees']*55)/100 + fnl['registration_fees_share'] - fnl['expenses_share']
# fnl = round(fnl,1)
# for ms in fnl.itertuples():
#         context = {
#                 'month': ms[1],
#                 'monthfees': str(ms[2]),
#                 'regestraionfees': str(ms[3]),
#                 'expenses': str(ms[4]),
#                 'regfeesshare': str(ms[5]),
#                 'expshare': str(ms[6]),
#                 'employee': str(ms[7]),
#                 'rupamsubhofinal': str(ms[8])}
# print(fnl)
mydate = datetime.datetime.now()
month = mydate.strftime("%B")
def exp():
        cursor.execute("select month,sum(month_fees) as month_fees from shikshalaya_computer_app_computer_student_monthly_fees where month = '"+month+"' group by month")

        for r in cursor.fetchall():
                return r[1]


print(exp())
