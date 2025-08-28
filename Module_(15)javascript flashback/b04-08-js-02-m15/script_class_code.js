const todoForm = document.getElementById('todo-form');
const todoList = document.getElementById('todo-list');

// Event Handler Function
const formSubmitHandler = (event) => {
    event.preventDefault(); // Prevent the default form submission behavior

    console.log(event); // Log the event object to the console
    console.log(event.target); // Log the form element to the console
    console.log(event.target.ghorardim); // Log the specific form element to the console
    console.log(event.target.ghorardim.value); // Log the form elements to the console

    const todoText = event.target.ghorardim.value;
    todoList.innerHTML = `<li class="task-item p-4 bg-gray-50 rounded-xl flex items-center shadow-sm">
                    <label class="cursor-pointer">
                        <div class="relative flex items-center mr-3">
                            <input type="checkbox" class="peer sr-only">
                            <div
                                class="h-5 w-5 flex items-center justify-center rounded border-2 border-purple-500 transition-colors peer-checked:bg-purple-500 peer-checked:border-purple-500 cursor-pointer">
                                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
                                    stroke="currentColor" stroke-width="3" stroke-linecap="round"
                                    stroke-linejoin="round"
                                    class="h-3 w-3 text-white opacity-0 peer-checked:opacity-100 transition-opacity">
                                    <path d="M5 12l5 5 9-9"></path>
                                </svg>
                            </div>
                        </div>
                    </label>
                    <span class="flex-1 text-gray-700 font-medium">
                        ${todoText}
                    </span>
                    <button class="text-gray-400 hover:text-red-500 transition-colors">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24"
                            stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2"
                                d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                    </button>
                </li>` + todoList.innerHTML;

    event.target.ghorardim.value = ""; // Clear the input field after submission
};

todoForm.addEventListener("submit", formSubmitHandler);
