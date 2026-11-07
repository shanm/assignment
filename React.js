import React from 'react';
import { useState } from 'react';

function App() {
  const [count, setCount] = useState(0)

  const [firstName, SetFirstName] = useState("Bob")
  const [lastName, SetLastName] = useState("Rob")

  function handleFirstNameChange(e) {
    console.log(e.target.value);
    SetFirstName(e.target.value)
  }

  function handleLastNameChange(e) {
    console.log(e.target.value);
    SetLastName(e.target.value)
  }

  return (
    <>
    <label>
      <input value={firstName} onChange={handleFirstNameChange} />
    </label>
    <label>
      <input value={lastName} onChange={handleLastNameChange} />
    </label>
    <p>First Name: { firstName } Last Name: { lastName }</p>
    <button onClick={ () => setCount((count) => count + 1)}>+</button>
    <button onClick={ () => setCount((count) => count - 1)}>-</button>
    <p>{count}</p>
    </>
  )
}

export default App

//////////////////////////////////////

import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <>
    <h2>{count}</h2>
    <p>
   <button onClick={ () => setCount(count => count + 1)}>Increment</button> 
   </p>
   <p>
   <button onClick={ () => setCount(count => count - 1)}>Decrement</button> 
   </p>
   <p>
   <button onClick={ () => setCount(0)}>Reset</button> 
   </p>
   </>
  )
}

export default Counter

