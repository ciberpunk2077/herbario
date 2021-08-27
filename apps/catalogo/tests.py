from django.test import TestCase

# Create your tests here.
import datetime


def mes_list():
    st = "2021-06-01"
    ed = "2021-10-31"
    start_date = datetime.datetime.strptime(st.strip(), '%Y-%m-%d')
    end_date = datetime.datetime.strptime(ed.strip(), '%Y-%m-%d')

    months = [datetime.datetime.strptime('%2.2d-%2.2d' % (y, m), '%Y-%m').strftime('%b')
              for y in range(start_date.year, end_date.year + 1)
              for m in range(start_date.month if y == start_date.year else 1, end_date.month + 1 if y == end_date.year else 13)]

    print(months)
