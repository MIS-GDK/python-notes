import datetime
import trafaret as t

date = t.Dict(year=t.Int, month=t.Int, day=t.Int) & (lambda d: datetime.datetime(**d))


def validate_date(data):
    try:
        return date.check(data), False
    except t.DataError as e:
        return False, e.as_dict()


print(validate_date({"year": 2012, "month": 1}))
# (False, {'day': 'is required'})

print(validate_date({"year": 2012, "month": 1, "day": 12}))
# (datetime.datetime(2012, 1, 12, 0, 0), False)

print(t.Email.check("someone"))
