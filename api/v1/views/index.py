#!/usr/bin/python3
"""Status of your API"""

from api.v1.views import app_views
from flask import jsonify
from models import storage
from flask import Flask

@app_views.route('/status', strict_slashes=False)
def status():
	"""
    Returns a JSON status
    """
    return jsonify({'status': 'OK'})


@app_views.route('/stats', strict_slashes=False)
def get_stats():
""" Retrieves the number of each objects by type """
    counts = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }

    return jsonify(counts)
