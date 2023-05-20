from pydantic import BaseModel


class TDPInputs(BaseModel):
    pickup_longitude: str
    pickup_latitude: str
    tpep_pickup_datetime: str
