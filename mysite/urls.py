# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.conf.urls import include, url
from django.contrib import admin

from drupalcamp.views import index
from drupalcamp.views import checkUpdates
from drupalcamp.views import getTypes
from drupalcamp.views import getLevels
from drupalcamp.views import getTracks
from drupalcamp.views import getSpeakers
from drupalcamp.views import getLocations
from drupalcamp.views import getSessions
from drupalcamp.views import getBofs
from drupalcamp.views import getSocialEvents
from drupalcamp.views import getPOI
from drupalcamp.views import getInfo
from drupalcamp.views import getFloorPlans
from drupalcamp.views import getSettings

urlpatterns = [
    url(r'^$', index),
    url(r'^checkUpdates$', checkUpdates),
    url(r'^getTypes$', getTypes),
    url(r'^getLevels$', getLevels),
    url(r'^getTracks$', getTracks),
    url(r'^getSpeakers$', getSpeakers),
    url(r'^getLocations$', getLocations),
    url(r'^getSessions$', getSessions),
    url(r'^getBofs$', getBofs),
    url(r'^getSocialEvents$', getSocialEvents),
    url(r'^getPOI$', getPOI),
    url(r'^getInfo$', getInfo),
    url(r'^getFloorPlans$', getFloorPlans),
    url(r'^getSettings$', getSettings),
    url(r'^admin/', include(admin.site.urls)),
]