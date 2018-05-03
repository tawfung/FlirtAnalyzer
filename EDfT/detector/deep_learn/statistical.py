from datetime import datetime as dt
from dateutil import parser
import pandas as pd

class Statistical:

    def __index__(self):
        pass
    def stat(self):
        data = pd.read_csv('detector/deep_learn/daily-log.csv')
        dat = pd.read_csv('static/stat-log.csv')
        with open('static/stat-log.csv', 'a') as stat:
            counters = [0, 0, 0, 0, 0, 0]
            now = dt.date(dt.now())

            list_day = []
            for j in range(len(data["time"])):
                if dt.date(parser.parse(data["time"][j])) != now:
                    list_day.append(dt.date(parser.parse(data["time"][j])))
            last_day = max(list_day)
            for i in range(len(data["time"])):
                counters[0] = last_day
                if dt.date(parser.parse((data["time"][i]))) == last_day:
                    counters[1] += int(data.loc[i:i, "total"])
                    counters[2] += int(data.loc[i:i, "anger"])
                    counters[3] += int(data.loc[i:i, "sadness"])
                    counters[4] += int(data.loc[i:i, "joy"])
                    counters[5] += int(data.loc[i:i, "undefined"])

            days_list = []
            for k in range(len(dat["day"])):
                days_list.append(dt.date(parser.parse(dat["day"][k])))
            if last_day not in days_list:
                stat.write(str(counters[0]) + ',' + str(counters[1]) + ',' + str(counters[2]) + ',' + str(counters[3])
                           + ',' + str(counters[4]) + ',' + str(counters[5]) + '\n')
        goals = dict()
        goals['counters'] = counters
        return goals

