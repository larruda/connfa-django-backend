from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings

import json
import pprint
import pytz

from .models import Type
from .models import Level
from .models import Track
from .models import Speaker
from .models import Location
from .models import POI
from .models import Session
from .models import BoF
from .models import SocialEvent
from .models import Page
from .models import FloorPlan

from constance import config


def index(request):
    return JsonResponse({})


def checkUpdates(request):
    response_data = {
        "idsForUpdate": [ int(x) for x in config.CHECK_UPDATES ],
    }
    return JsonResponse(response_data)


def getTypes(request):
    response_data = {}
    response_data['types'] = []
    types = Type.objects.all()

    # Another database query to start fetching the rows in batches.
    for type in types.iterator():
        response_data['types'].append({
            "typeId" : type.id,
            "typeName" : type.name,
            "typeIconURL" : type.iconURL,
            "order" : type.order,
            "deleted" : type.deleted
            })

    return JsonResponse(response_data)


def getLevels(request):
    response_data = {}
    response_data['levels'] = []
    levels = Level.objects.all()

    # Another database query to start fetching the rows in batches.
    for level in levels.iterator():
        response_data['levels'].append({
            "levelId" : level.id,
            "levelName" : level.name,
            "order" : level.order,
            "deleted" : level.deleted
            })

    return JsonResponse(response_data)


def getTracks(request):
    response_data = {}
    response_data['tracks'] = []
    tracks = Track.objects.all()

    # Another database query to start fetching the rows in batches.
    for track in tracks.iterator():
        response_data['tracks'].append({
            "trackId" : track.id,
            "trackName" : track.name,
            "order" : track.order,
            "deleted" : track.deleted
            })

    return JsonResponse(response_data)


def getSpeakers(request):
    response_data = {}
    response_data['speakers'] = []
    speakers = Speaker.objects.all()

    # Another database query to start fetching the rows in batches.
    for speaker in speakers.iterator():
        response_data['speakers'].append({
            "speakerId" : speaker.id,
            "firstName" : speaker.firstName,
            "lastName" : speaker.lastName,
            "characteristic" : speaker.characteristic,
            "jobTitle" : speaker.jobTitle,
            "organizationName" : speaker.organizationName,
            "twitterName" : speaker.twitterName,
            "webSite" : speaker.webSite,
            "avatarImageURL" : speaker.avatarImageURL,
            "order" : speaker.order,
            "deleted" : speaker.deleted
            })

    return JsonResponse(response_data)


def getLocations(request):
    response_data = {}
    response_data['locations'] = []
    locations = Location.objects.all()

    # Another database query to start fetching the rows in batches.
    for location in locations.iterator():
        response_data['locations'].append({
            "locationId" : location.id,
            "longitude" : location.longitude,
            "latitude" : location.latitude,
            "locationName" : location.name,
            "address" : location.address,
            "order" : location.order,
            "deleted" : location.deleted
            })

    return JsonResponse(response_data)


def getSessions(request):
    return parseEvents(model=Session)


def parseEvents(model):
    response_data = {}
    response_data['days'] = []
    days = model.objects.values_list('start', flat=True).distinct()
    sp_timezone = pytz.timezone('America/Sao_Paulo')

    for day in days.iterator():
        sessions = model.objects.filter(start=day)
        events = []
        for session in sessions.iterator():
            events.append({
                "eventId": session.id,
                "text": session.text,
                "name": session.name,
                "place": session.place,
                "version": session.version,
                "experienceLevel": session.experienceLevel and session.experienceLevel.id or None,
                "type": session.type and session.type.id or None,
                "from": session.start.astimezone(pytz.timezone(settings.TIME_ZONE)).isoformat(),
                "to": session.end.astimezone(pytz.timezone(settings.TIME_ZONE)).isoformat(),
                "speakers": [ speaker.id for speaker in session.speakers.all().iterator() ],
                "track": session.track and session.track.id or None,
                "order": session.order,
                "link": session.link,
                "deleted": session.deleted
                })

        response_data['days'].append({
            "date": day.strftime('%d-%m-%Y'),
            "events": events
            })

    return JsonResponse(response_data)


def getBofs(request):
    return parseEvents(model=BoF)


def getSocialEvents(request):
    return parseEvents(model=SocialEvent)


def getPOI(request):
    response_data = {}
    response_data['poi'] = []
    pois = POI.objects.all()

    # Another database query to start fetching the rows in batches.
    for poi in pois.iterator():
        response_data['poi'].append({
            "poiId" : poi.id,
            "poiName" : poi.name,
            "poiDescription" : poi.description,
            "poiImageURL" : poi.imageURL,
            "poiDetailURL" : poi.detailURL,
            "order" : poi.order,
            "deleted" : poi.deleted
            })

    return JsonResponse(response_data)


def getInfo(request):
    response_data = {
        "title": {
            "titleMajor": config.TITLE_MAJOR,
            "titleMinor": config.TITLE_MINOR,
        }
    }
    response_data['info'] = []
    pages = Page.objects.all()

    # Another database query to start fetching the rows in batches.
    for page in pages.iterator():
        response_data['info'].append({
            "infoId" : page.id,
            "infoTitle" : page.title,
            "html" : page.html,
            "order" : page.order,
            "deleted" : page.deleted
            })

    return JsonResponse(response_data)


def getFloorPlans(request):
    response_data = {}
    response_data['floorPlans'] = []
    floorPlans = FloorPlan.objects.all()

    # Another database query to start fetching the rows in batches.
    for floorPlan in floorPlans.iterator():
        response_data['floorPlans'].append({
            "floorPlanId" : floorPlan.id,
            "floorPlanName" : floorPlan.name,
            "floorPlanImageURL" : floorPlan.imageURL,
            "order" : floorPlan.order,
            "deleted" : floorPlan.deleted
            })

    return JsonResponse(response_data)


def getSettings(request):
    response = {
        "settings": {
            "titleMajor": config.TITLE_MAJOR,
            "titleMinor": config.TITLE_MINOR,
            "twitterWidget": config.TWITTER_WIDGET,
            "timezone": config.TIMEZONE
        }
    }
    return JsonResponse(response)
