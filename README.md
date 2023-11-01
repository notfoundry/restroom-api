# Installation

Start by cloning this repository.

To install Django and the other project dependencies, execute the following command:
`python3 -m pip install -U -r requirements.txt`

You will also need to set a `GOOGLEMAPS_API_KEY` environment variable to your Google Maps API key, used for querying local business information.

# Running

1. Start by running `python3 manage.py migrate`, to set up the Django database.
2. Then, run `python3 manage.py runserver` to start the backend server. This should expose the development server to http://127.0.0.1:8000/.
3. To explore the available APIs and experiment with them, navigate to http://127.0.0.1:8000/api-docs/.


The important endpoint is http://127.0.0.1:8000/api/v1/restrooms/nearby/, which can be used by passing a `lat` and `long` parameter to the query.

For example, making a GET request to http://127.0.0.1:8000/api/v1/restrooms/nearby/?lat=45.256420&long=-75.918472 will identify a list of restrooms in the area of (45.256420, -75.918472). An example list entry is:
```json
[
    {
        "business_status": "OPERATIONAL",
        "geometry": {
            "location": {
                "lat": 45.2542529,
                "lng": -75.9152888
            },
            "viewport": {
                "northeast": {
                    "lat": 45.2555265802915,
                    "lng": -75.91381236970848
                },
                "southwest": {
                    "lat": 45.2528286197085,
                    "lng": -75.9165103302915
                }
            }
        },
        "icon": "https://maps.gstatic.com/mapfiles/place_api/icons/v1/png_71/civic_building-71.png",
        "icon_background_color": "#7B9EB0",
        "icon_mask_base_uri": "https://maps.gstatic.com/mapfiles/place_api/icons/v2/civic-bldg_pinlet",
        "name": "Ottawa Public Library - Stittsville",
        "opening_hours": {
            "open_now": true
        },
        "photos": [
            {
                "height": 1080,
                "html_attributions": [
                    "<a href=\"https://maps.google.com/maps/contrib/115014721311659682284\">Tarek Belghith</a>"
                ],
                "photo_reference": "AcJnMuE0zGnberLDiaf5r1Rl42BJ4pLX0P_G9L5QPmuy0aq1KaZasxRHvPug_VYPjAjpYSXQ6QpncCdO8j5IyaK7mm5zWFo-tLEdvL4haDnABfstmnAOXwcDfxUvBxyAiJqYcoqi2q4ncF0vW8CCbXGeVWVdFMbMqt5dDOcvrzd3Qo6t0USw",
                "width": 1920
            }
        ],
        "place_id": "ChIJbcul-LP4zUwRxDeNHqWZUwM",
        "plus_code": {
            "compound_code": "733M+PV Stittsville, Ottawa, ON, Canada",
            "global_code": "87Q6733M+PV"
        },
        "rating": 4.7,
        "reference": "ChIJbcul-LP4zUwRxDeNHqWZUwM",
        "scope": "GOOGLE",
        "types": [
            "library",
            "point_of_interest",
            "establishment"
        ],
        "user_ratings_total": 68,
        "vicinity": "1637 Stittsville Main Street, Ottawa"
    }
```