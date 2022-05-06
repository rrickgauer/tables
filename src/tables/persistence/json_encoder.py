#************************************************************************************
# Name:     CustomJSONEncoder
#
# Purpose:  This class is used to encode date's in the correct format: YYYY-MM-DD. 
#
#           Before creating this, Flask was encoding all dates/datetimes/times as 'Mon, 15 Mar 2021 18:30:42 GMT'.
#           This was done to fields that were only dates.
#
#           The solution was found: https://www.javaer101.com/en/article/1732830.html
#************************************************************************************
import dataclasses
from enum import Enum
from uuid import UUID
from json import JSONEncoder
from datetime import date, datetime
from decimal import Decimal

class IDictable:
    pass

class CustomJSONEncoder(JSONEncoder):
    
    def default(self, obj):
        try:
            if isinstance(obj, IDictable) and hasattr(obj, "__dict__"):
                return obj.__dict__
            if isinstance(obj, (date, datetime)):
                return obj.isoformat()
            if isinstance(obj, UUID):
                return str(obj)
            if dataclasses.is_dataclass(obj):
                return dataclasses.asdict(obj)
            if isinstance(obj, Decimal):
                return float(obj)
            if isinstance(obj, Enum):
                return obj.value
        except:
            pass

        return super().default(obj)
            