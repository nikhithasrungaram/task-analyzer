from django.test import TestCase
from .scoring import calculate_task_score, detect_circular_dependencies

class ScoringTests(TestCase):
    def test_basic_scoring(self):
        tasks = [
            {'id': 'a', 'title': 'Task A', 'due_date': '2025-12-01', 'importance': 8, 'estimated_hours': 2, 'dependencies': []},
            {'id': 'b', 'title': 'Task B', 'due_date': '2024-01-01', 'importance': 5, 'estimated_hours': 1, 'dependencies': []},
        ]
        id_map = {t['id']: t for t in tasks}
        score_a, _ = calculate_task_score(tasks[0], id_map, strategy='smart_balance')
        score_b, _ = calculate_task_score(tasks[1], id_map, strategy='smart_balance')
        # Task B is in the past (2024) -> high urgency -> should have higher score than A
        self.assertTrue(score_b > score_a)

    def test_cycle_detection(self):
        tasks = [
            {'id': 1, 'dependencies': [2]},
            {'id': 2, 'dependencies': [3]},
            {'id': 3, 'dependencies': [1]},
            {'id': 4, 'dependencies': []}
        ]
        cycles = detect_circular_dependencies(tasks)
        self.assertTrue(len(cycles) >= 1)
        cycle_nodes = set(sum(cycles, []))
        self.assertTrue({1,2,3}.issubset(cycle_nodes))
