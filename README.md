# status-service
Service status web service with RESTful API

## Design requirements
1. Get list of services for which status is available
2. Get current status of requested service
3. (Roadmap) Get historical service status data for date range
4. (Roadmap) Plugins for new services
5. Structure code as per
http://docs.python-guide.org/en/latest/writing/structure/ and the repo
structure as per kenneth reitz (next time I'll have to fork it first, but do it
manually this time for the learning experience)
6. Tests, tests write some tests. Plan to use pytest.

### Iteration 1 Plan
1. Initial service is the status-service itself
2. Simple GET only service status (ie reqs 1 and 2)
3. No fancy stuff like authentication/authorisation, let's just get it working
4. Deploy to AWS

### Service Status API
1. GET /services
    * returns JSON:
    
```
        {
            "services": ["status-service","ip-service","time-service"]
        }
```

2. GET /services/service-name
    * return JSON

```
        {
            "service" : "service-name",
            "status": "up" | "down",
            "datetime": "datetime-string"
        }
```

Error condition, if <service-name> doesn't exist, return a 404 error.
