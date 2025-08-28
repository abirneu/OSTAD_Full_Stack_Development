// Wait for the DOM to load
document.addEventListener('DOMContentLoaded', function () {
    // Get DOM elements
    const todoForm = document.getElementById('todo-form');
    const todoInput = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');
    const taskCount = document.getElementById('task-count');
    const clearCompletedBtn = document.getElementById('clear-completed');

    // Add event listener to form submission
    todoForm.addEventListener('submit', function (event) {
        // Prevent the default form submission
        event.preventDefault();

        // Get the task text and trim whitespace
        const taskText = todoInput.value.trim();

        // Only proceed if the input is not empty
        if (taskText !== '') {
            // Add the new task
            addTask(taskText);

            // Clear the input field
            todoInput.value = '';

            // Update the task count
            updateTaskCount();
        }
    });

    // Add event listener to clear completed button
    clearCompletedBtn.addEventListener('click', function () {
        // Get all completed tasks
        const completedTasks = document.querySelectorAll('.task-item.completed');

        // Remove each completed task
        completedTasks.forEach(task => task.remove());

        // Update the task count
        updateTaskCount();
    });

    // Function to add a new task
    function addTask(text) {
        // Create list item
        const listItem = document.createElement('li');
        listItem.className = 'task-item p-4 bg-gray-50 rounded-xl flex items-center shadow-sm';

        // Create the label with checkbox using HTML directly
        const labelHTML = `
            <label class="cursor-pointer">
                <div class="relative flex items-center mr-3">
                    <input type="checkbox" class="peer sr-only">
                    <div class="h-5 w-5 flex items-center justify-center rounded border-2 border-purple-500 transition-colors peer-checked:bg-purple-500 peer-checked:border-purple-500 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" 
                            stroke-width="3" stroke-linecap="round" stroke-linejoin="round" class="h-3 w-3 text-white opacity-0 transition-opacity">
                            <path d="M5 12l5 5 9-9"></path>
                        </svg>
                    </div>
                </div>
            </label>
        `;

        // Create task text
        const taskText = document.createElement('span');
        taskText.textContent = text;
        taskText.className = 'flex-1 text-gray-700 font-medium';

        // Create delete button using HTML directly
        const deleteBtnHTML = `
            <button class="text-gray-400 hover:text-red-500 transition-colors">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                </svg>
            </button>
        `;

        // Set the inner HTML of the list item
        listItem.innerHTML = labelHTML;
        listItem.appendChild(taskText);
        listItem.insertAdjacentHTML('beforeend', deleteBtnHTML);

        // Get the checkbox and add event listener
        const checkbox = listItem.querySelector('input[type="checkbox"]');
        const checkIcon = listItem.querySelector('svg');

        checkbox.addEventListener('change', function () {
            if (this.checked) {
                listItem.classList.add('completed');
                taskText.classList.add('line-through', 'text-gray-400');
                checkIcon.classList.add('opacity-100');
                checkIcon.classList.remove('opacity-0');
            } else {
                listItem.classList.remove('completed');
                taskText.classList.remove('line-through', 'text-gray-400');
                checkIcon.classList.remove('opacity-100');
                checkIcon.classList.add('opacity-0');
            }
        });

        // Add event listener to delete button
        const deleteBtn = listItem.querySelector('button');
        deleteBtn.addEventListener('click', function () {
            // Add a fade-out effect
            listItem.classList.add('opacity-0');

            // Remove the task after animation completes
            setTimeout(() => {
                listItem.remove();
                updateTaskCount();
            }, 300);
        });

        // Add the list item to the todo list with animation
        listItem.style.opacity = '0';
        todoList.appendChild(listItem);

        // Trigger reflow for animation
        setTimeout(() => {
            listItem.style.opacity = '1';
        }, 10);
    }

    // Function to update the task count
    function updateTaskCount() {
        const count = todoList.children.length;
        taskCount.textContent = count;
    }
});