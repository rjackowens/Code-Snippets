from collections import namedtuple
from dataclasses import dataclass
import pandas as pd

past = ["1997", "1923", "1400"]
present = ["2019"]
future = ["2084"]


# Named Tuple
yearsTuple = namedtuple('Attributes', ['past', 'present', 'future'])
yt = yearsTuple(past, present, future)
# print(yt.past)
# print(yt._fields)


# Dictionary
yearsDict = {
    "Past": past,
    "Present": present,
    "Future": future
}
yd = yearsDict
# print(yd["Past"])
# print(yd.items())


# Class Object
class yearsObject(object):
    def __init__(self, past, present, future):
        self.past = past
        self.present = present
        self.future = future

    def __str__(self):
        return f" Past {self.past} Present {self.present} Future {self.future}"
yo = yearsObject(past, present, future)
print(yo.present)


# Dataclass Module
@dataclass
class yearsDataClass:
    past: list
    present: str
    future: str
ydc = yearsDataClass(past, present, future)
# print(ydc.past)


# Zip Object
z = zip(past, present, future)
z = set(z)
# print(z)


# Pandas Dataframe
df_past = pd.DataFrame(past, columns=["Past"])
df_present = pd.DataFrame(present, columns=["Present"])
df_future = pd.DataFrame(future, columns=["Future"])
df_combined = pd.concat([df_past, df_present, df_future], axis=1) # Works w/diff. length lists
print(df_combined)
