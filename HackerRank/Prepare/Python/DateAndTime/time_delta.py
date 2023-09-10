import calendar
from datetime import datetime

def get_datetime_object(timestamp):
    ts = timestamp.split()
    day = int(ts[1])
    month_str = ts[2]
    month_hdrs = calendar.month_name[1:]
    month_hdr = list(map(lambda x:x[0:3], month_hdrs))
    month = month_hdr.index(month_str)+1
    year = int(ts[3])
    hour, min, sec = list(map(int,ts[4].split(':')))
    
    #datetime(year, month, day[, hour[, minute[, second[, microsecond[,tzinfo]]]]])
    return datetime(year, month, day, hour, min, sec, tzinfo=datetime.strptime(ts[-1], '%z').tzinfo)


# Complete the time_delta function below.
def time_delta(t1, t2):
    pass

if __name__ == '__main__':
    
    
    t1 = 'Wed 12 May 2269 23:22:15 -0500'
    t2 = 'Tue 05 Oct 2269 02:12:07 -0200'

    t1_dt, t2_dt = get_datetime_object(t1), get_datetime_object(t2)
    dt = t1_dt-t2_dt
    delta_t = int(dt.total_seconds())
    print(abs(delta_t))
    print('12527392')
