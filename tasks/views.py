from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .scoring import calculate_task_score

@csrf_exempt
def analyze_tasks(request):
    if request.method != 'POST':
        return JsonResponse({"error": "POST required"})
    
    try:
        data = json.loads(request.body)
        tasks = data.get('tasks', [])
    except Exception:
        return JsonResponse({"error": "Invalid JSON"})

    for task in tasks:
        task['score'] = calculate_task_score(task)

    tasks_sorted = sorted(tasks, key=lambda x: x['score'], reverse=True)
    return JsonResponse(tasks_sorted, safe=False)

@csrf_exempt
def suggest_tasks(request):
    if request.method != 'POST':
        return JsonResponse({"error": "Please POST JSON with \"tasks\" list to this endpoint or call via POST/with body"})

    try:
        data = json.loads(request.body)
        tasks = data.get('tasks', [])
    except Exception:
        return JsonResponse({"error": "Invalid JSON"})

    for task in tasks:
        task['score'] = calculate_task_score(task)

    tasks_sorted = sorted(tasks, key=lambda x: x['score'], reverse=True)
    top_tasks = tasks_sorted[:3]

    for t in top_tasks:
        t['reason'] = f"Score {t['score']} computed from urgency, importance, effort, dependencies"

    return JsonResponse(top_tasks, safe=False)
