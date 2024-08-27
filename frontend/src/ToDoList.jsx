import { useState, useEffect } from 'react';

const ToDoList = () => {

    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState("");

    const handleTextChange = (ev) => {
        setNewTask(ev.target.value);
    };
    const addTask = () => {
        fetch('http://localhost:5000/list', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({text: newTask}),
        });
        fetch('http://localhost:5000/list', {
            method: 'GET',
        }).then(resp => resp.json())
            .then(data => setTasks(data));
    };
    const deleteTask = (idx) => {
        setTasks(tasks.filter((it, _) => it[0] !== idx));
        fetch('http://localhost:5000/list', {
            method: 'DELETE',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({id: idx})
        });
    };

    useEffect(() => {
        fetch('http://localhost:5000/list', {
            method: 'GET',
        }).then(resp => resp.json())
            .then(data => setTasks(data));
    }, []);

    return (
        <div className="to-do-list">
          <h1>ToDo List</h1>

          <div>
            <input
              type="text"
              placeholder="Enter text here..."
              value={newTask}
              onChange={handleTextChange}/>

            <button className="add-button" onClick={addTask}>Add</button>
          </div>

          <ol>
            {tasks.map((task, idx) =>
                <li key={idx}>
                  <span className="text">{task[1]}</span>
                  <button className="delete-button" onClick={() => deleteTask(task[0])}>Delete</button>
                </li>
            )}
          </ol>
          
        </div>
    );
};

export default ToDoList;
