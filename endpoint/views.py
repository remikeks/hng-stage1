from django.shortcuts import render
from django.http import JsonResponse
from datetime import datetime

def index(request):
    slack_name = request.GET.get("slack_name")
    track = request.GET.get("track")

    data = {
        "slack_name": slack_name,
        "current day": datetime.utcnow().strftime('%A'),
        "utc_time": datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": track,
        "github_file_url": "https://github.com/remikeks/hng-stage1/blob/main/endpoint/views.py",
        "github_repo_url": "https://github.com/remikeks/hng-stage1",
        "status_code": 200
    }
    

    return JsonResponse(data)

