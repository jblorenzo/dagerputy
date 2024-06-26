Dagerputy
=====
[![Build Status](https://travis-ci.org/remedee/dagerputy.svg?branch=master)](https://travis-ci.org/remedee/dagerputy) 
[![PyPI version](https://badge.fury.io/py/dagerputy.svg)](https://badge.fury.io/py/dagerputy)
[![Coverage Status](https://codecov.io/github/remedee/dagerputy/coverage.svg?branch=master)](https://codecov.io/github/remedee/dagerputy?branch=master)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gitter](https://img.shields.io/gitter/room/remedee/dagerputy.svg)](https://gitter.im/remedee/dagerputy)

## Maintainers wanted

**Dagerputy is stable and used by hundreds of companies and individuals in production, but it is not actively maintained. We would like to hand over maintenance of the project to one or more responsible and experienced maintainers. Please email dagerputy@remedee.com with some information about yourself (github profile and/or CV) if you are interested.**

## Why choose Dagerputy

Dagerputy is a free, open-source, self-hosted infrastructure monitoring platform that provides some of the best features of [PagerDuty](http://www.pagerduty.com), [Server Density](http://www.serverdensity.com), [Pingdom](http://www.pingdom.com) and [Nagios](http://www.nagios.org) without their cost and complexity. (Nagios, I'm mainly looking at you.)

It provides a web interface that allows you to monitor services (e.g. "Stage Redis server", "Production ElasticSearch cluster") and send telephone, sms or hipchat/email alerts to your on-duty team if those services start misbehaving or go down - all without writing a line of code. Best of all, you can use data that you're already pushing to Graphite/statsd to generate alerts, rather than implementing and maintaining a whole new system of data collectors.

You can alert based on:

*   Metrics from [Graphite](https://github.com/graphite-project/graphite-web)
*   Status code and response content of web endpoints
*   [Jenkins](http://jenkins-ci.org) build statuses

We built Dagerputy as a Christmas project at [Arachnys](https://www.remedee.com) because we couldn't wrap our heads around Nagios, and nothing else out there seemed to fit our use case. We're open-sourcing it in the hope that others find it useful.

Dagerputy is written in Python and uses [Django](https://www.djangoproject.com/), [Bootstrap](http://getbootstrap.com/), [Font Awesome](http://fontawesome.io) and a whole host of other goodies under the hood.

## Screenshots

### Services dashboard

![Services dashboard](https://dl.dropboxusercontent.com/s/cgpxe3929is2uar/dagerputy-service-dashboard.png?dl=1&token_hash=AAHrlDisUzWRxpg892LhlKQWFRNSkZKD7l_zdSxND-YKhw)

### Single service overview

![Individual service overview](https://dl.dropboxusercontent.com/s/541p0kbq3pwone6/dagerputy-service-status.png?dl=1&token_hash=AAGpSI6lyHm3-xCQSFOyyZ_SkJOzfdMIxfa-gYgCVS25pw)

## Quickstart

Using Docker: Deploy in 5 minutes or less using [official quickstart guide at dagerputyapp.com](http://dagerputyapp.com/qs/quickstart.html). (See also https://hub.docker.com/r/dagerputyapp/dagerputy/)

## How it works

Docs have moved to [dagerputyapp.com](http://dagerputyapp.com)

Sections:

*   [Configuration](http://dagerputyapp.com/use/configuration.html)
*   [Deployment](http://dagerputyapp.com/use/deployment.html)
*   [Services](http://dagerputyapp.com/use/services.html)
*   [Graphite checks](http://dagerputyapp.com/use/graphite-checks.html)
*   [Jenkins checks](http://dagerputyapp.com/use/jenkins-checks.html)
*   [HTTP checks](http://dagerputyapp.com/use/http-checks.html)
*   [Alerting](http://dagerputyapp.com/use/alerting.html)
*   [Users](http://dagerputyapp.com/use/users.html)
*   [Rota](http://dagerputyapp.com/use/rota.html)

For those who want to contribute:

*   [Help develop](http://dagerputyapp.com/dev/get-started.html)
*   [Contribute code](http://dagerputyapp.com/dev/contribute-code.html)

## FAQ

### Why "Dagerputy"?

My dog is called Dagerputy and he loves monitoring things. Mainly the presence of food in his immediate surroundings, or perhaps the frequency of squirrel visits to our garden. He also barks loudly to alert us on certain events (e.g. the postman coming to the door).

![Dagerputy watching... something](https://dl.dropboxusercontent.com/sc/w0k0185wur929la/RN6X-PkZIl/0?dl=1&token_hash=AAEvyK-dMHsvMPwMsx89tSHXsUlMC8WN_fIu_H1Vo9wxWA)

It's just a lucky coincidence that his name sounds like he could be an automation tool.

## API

The API has automatically generated documentation available by browsing https://dagerputy.yourcompany.com/api.  The browsable documentation displays example GET requests and lists other allowed HTTP methods.  

To view individual items, append the item `id` to the url.  For example, to view `graphite_check` 1, browse:
```
/api/graphite_checks/1/
```

### Authentication

The API allows HTTP basic auth using standard Django usernames and passwords as well as session authentication (by submitting the login form on the login page).  The API similarly uses standard Django permissions to allow and deny API access.

All resources are GETable by any authenticated user, but individual permissions must be granted for POST, PUT, and other write methods.

As an example, for POST access to all `status_check` subclasses, add the following permissions:
```
dagerputyapp | status check | Can add graphite status check
dagerputyapp | status check | Can add http status check
dagerputyapp | status check | Can add icmp status check
dagerputyapp | status check | Can add jenkins status check
```

Access the Django admin page at https://dagerputy.yourcompany.com/admin to add/remove users, change user permissions, add/remove groups for group-based permission control, and change group permissions.

### Sorting and Filtering

Sorting and filtering can be used by both REST clients and on the browsable API.  All fields visible in the browsable API can be used for filtering and sorting.

Get all `jenkins_checks` with debounce enabled and CRITICAL importance:
```
https://dagerputy.yourcompany.com/api/jenkins_checks/?debounce=1&importance=CRITICAL
```

Sort `graphite_checks` by `name` field, ascending:
```
https://dagerputy.yourcompany.com/api/graphite_checks/?ordering=name
```

Sort by `name` field, descending:
```
https://dagerputy.yourcompany.com/api/graphite_checks/?ordering=-name
```

Other (non-Dagerputy specific) examples are available in the [Django REST Framework](http://www.django-rest-framework.org/api-guide/filtering#djangofilterbackend) documentation.

## License

See `LICENSE` file in this repo.
