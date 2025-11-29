from datetime import date, datetime

def calculate_task_score(task):
    """
    Compute a priority score for a task.
    Higher score = higher priority.
    Factors: Urgency, Importance, Effort, Dependencies
    """
    score = 0

    # Parse due_date if string
    if isinstance(task['due_date'], str):
        task_due_date = datetime.strptime(task['due_date'], "%Y-%m-%d").date()
    else:
        task_due_date = task['due_date']

    today = date.today()
    days_until_due = (task_due_date - today).days

    # Urgency
    if days_until_due < 0:
        score += 100  # overdue
    elif days_until_due <= 3:
        score += 50
    elif days_until_due <= 7:
        score += 20

    # Importance
    score += task.get('importance', 5) * 5

    # Effort (quick wins)
    estimated_hours = task.get('estimated_hours', 1)
    if estimated_hours < 2:
        score += 10
    elif estimated_hours > 8:
        score -= 5

    # Dependencies (tasks that block others are more important)
    deps = task.get('dependencies', [])
    score += len(deps) * 5

    return score
