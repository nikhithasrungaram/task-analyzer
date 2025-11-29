async function analyzeTasks() {
    const input = document.getElementById('taskInput').value;
    try {
        const response = await fetch('http://127.0.0.1:8000/api/tasks/analyze/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ tasks: JSON.parse(input) })
        });
        const data = await response.json();
        displayTasks(data);
    } catch (err) {
        alert("Error: Invalid JSON or server error");
    }
}

async function suggestTasks() {
    const input = document.getElementById('taskInput').value;
    try {
        const response = await fetch('http://127.0.0.1:8000/api/tasks/suggest/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ tasks: JSON.parse(input) })
        });
        const data = await response.json();
        displayTasks(data);
    } catch (err) {
        alert("Error: Invalid JSON or server error");
    }
}

function displayTasks(tasks) {
    const output = document.getElementById('output');
    output.innerHTML = '';
    tasks.forEach(task => {
        const card = document.createElement('div');
        card.className = 'task-card';
        if (task.score >= 80) card.classList.add('high');
        else if (task.score >= 50) card.classList.add('medium');
        else card.classList.add('low');
        card.innerHTML = `<b>${task.title}</b> - Score: ${task.score}<br>
                          Due: ${task.due_date}, Importance: ${task.importance}, Effort: ${task.estimated_hours}<br>
                          ${task.reason ? "Reason: " + task.reason : ""}`;
        output.appendChild(card);
    });
}
