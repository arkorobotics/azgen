from fastapi import FastAPI, Response, status

from .models import AZRequest, AZResponse
from .azgen import get_bounds, get_cutoff_alt, get_az
from .verison import __version__


app = FastAPI()


@app.get("/")
def home():
    return f'AZAPI v{__version__}'


@app.post("/", status_code=status.HTTP_200_OK, response_model=AZResponse)
def azgen(item: AZRequest, response: Response):
    bounds = get_bounds(item)
    cutoff_alt = get_cutoff_alt(item)
    dem_data = get_az(item, bounds)

    print(f'Bounds: {bounds}')
    print(f'Cutoff Alt: {cutoff_alt}')
    print(f'DEM Data: {dem_data}')

    # final points would be put in this dict:
    az_resp = {}
    return az_resp
