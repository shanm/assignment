//App.jsx
import React from 'react';
import { useState } from 'react'
import ChildComponent from './components/ChildComponent';

function App() {
  const [search, setSearch] = useState("");
  const [users, setUsers] = useState(
    [
    {"id": 1,"name": "Alice"},
    {"id": 2,"name": "Bob"},
    {"id": 3,"name": "Mike"}
    ]
  );

  const searchUsers = users.filter(
    (user) => user.name.toLowerCase().includes(search.toLowerCase())
  )

  //console.log(searchUsers);

  const deleteUser = (id) => {
    setUsers((prevUsers) => prevUsers.filter((user) => user.id !== id))
  }

  const greetFunc = () => {
    alert("Hi welcome to the site")
    console.log("Click on button")
  }


  return (
    <>
    <p>
    <input
    type="text"
    value={search}
    placeholder="Search Name..."
    onChange={(e) => setSearch(e.target.value)}
    />
    </p>
    {
      searchUsers.length > 0 ? (
        <ul>
        {
          searchUsers.map((user) => 
          <li key={user.id}>
          {user.name} - 
          <button onClick={() => deleteUser(user.id)}>Delete</button>

          </li>
          )
        }
        </ul>
      ) : (
        <p>
        Users not found
        </p>
      )
    }

    <ChildComponent name="shan" age={23} greet={greetFunc} />
    </>
  )
} 

export default App

///////////////////////////////////////

//ChildComponent.jsx
import react from 'react';

const ChildComponent = (props) => {
  return (
    <div>
    Name is {props.name} and age is {props.age}
    <p>
    <button onClick={props.greet}>Say Hello</button>
    </p>
    </div>
    
  )
}

export default ChildComponent