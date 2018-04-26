from datetime import datetime as dt
from dateutil import parser
import pandas as pd

class Statistical:

    def __index__(self):
        pass
    def stat(self):
        data = pd.read_csv('detector/deep_learn/daily-log.csv')
        dat = pd.read_csv('detector/deep_learn/stat-log.csv')
        with open('detector/deep_learn/stat-log.csv', 'a') as stat:
            counters = [0, 0, 0, 0, 0, 0]
            for i in range(len(data["time"])):
                last_day = dt.date(parser.parse(data["time"].iloc[-2]))
                counters[0] = last_day
                if (dt.date(parser.parse((data["time"][i]))) == last_day) \
                        & (dt.date(parser.parse((data["time"][i]))) != dt.date(dt.now())):
                    counters[1] += int(data.loc[i:i, "total"])
                    counters[2] += int(data.loc[i:i, "anger"])
                    counters[3] += int(data.loc[i:i, "disgust"])
                    counters[4] += int(data.loc[i:i, "joy"])
                    counters[5] += int(data.loc[i:i, "undefined"])
            days_list = []
            for j in range(len(dat["day"])):
                days_list.append(parser.parse(dat["day"][j]))
            if (dt.date(parser.parse(data["time"].iloc[-2])) not in days_list) \
                    & (dt.date(parser.parse((data["time"][i]))) != dt.date(dt.now())):
                stat.write(str(counters[0]) + ',' + str(counters[1]) + ',' + str(counters[2]) + ',' + str(counters[3])
                           + ',' + str(counters[4]) + ',' + str(counters[5]) + '\n')
        goals = dict()
        goals['counters'] = counters
        return goals

