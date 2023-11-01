import os

from rest_framework.decorators import api_view
from rest_framework.response import Response

from drf_spectacular.utils import OpenApiParameter, extend_schema

import googlemaps


gmaps = googlemaps.Client(key=os.getenv("GOOGLEMAPS_API_KEY"))


def execute_nearby_places_query(*args, **kwargs):
    acc = []

    resp = gmaps.places_nearby(*args, **kwargs)
    acc += resp["results"]
    while "next_page_token" in resp:
        resp = gmaps.places_nearby(*args, **kwargs, page_token=resp["next_page_token"])
        acc += resp["results"]

    return acc


@extend_schema(
    parameters=[
        OpenApiParameter(name='lat', description='<description>',  required=True, type=float),
        OpenApiParameter(name='long', description='<description>',  required=True, type=float),
    ]
)
@api_view(['GET'])
def get_nearby_restrooms(request) -> Response:
    lat = request.GET.get("lat")
    long = request.GET.get("long")

    acc = []

    for type_code in ["library", "university", "cafe", "gas_station"]:
        acc += execute_nearby_places_query(
            location=(float(lat), float(long)),
            open_now=True,
            radius=1000,
            type=type_code
        )

    acc += execute_nearby_places_query(
        location=(float(lat), float(long)),
        open_now=True,
        rank_by="distance",
        keyword="restroom"
    )

    return Response(acc)