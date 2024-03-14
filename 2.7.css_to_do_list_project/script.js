document.addEventListener('DOMContentLoaded', function () {
    const addButton = document.getElementById('add-button');
    const inputField = document.getElementById('todo-input');
    const todoList = document.getElementById('todo-list');  
  
    addButton.addEventListener('click', function () {
      const todoText = inputField.value;
      if (todoText.trim() !== '') {
        const todoItem = document.createElement('li');
        todoItem.innerHTML = `
          <span>${todoText}</span>
          <button class="delete-btn">Delete</button>
        `;
        todoList.appendChild(todoItem);
        inputField.value = '';
  
        const deleteButton = todoItem.querySelector('.delete-btn');
        deleteButton.addEventListener('click', function () {
          todoItem.remove();
        });
      } else {
        alert('Please enter a valid task.');
      }
    });
  });