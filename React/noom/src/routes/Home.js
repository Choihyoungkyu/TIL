import React, { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import ToDo from "../components/ToDo";
import { addToDo } from "../toDosSaga";

function Home() {
  const [text, setText] = useState("");
  const toDoList = useSelector((state) => state.toDos);
  const dispatch = useDispatch();
  function onChange(e) {
    setText(e.target.value);
  }
  function onSubmit(e) {
    e.preventDefault();
    console.log(text);
    dispatch(addToDo(text));
    setText("");
  }
  return (
    <>
      <h1>To Do</h1>
      <form onSubmit={onSubmit}>
        <input type="text" value={text} onChange={onChange} />
        <button>Add</button>
      </form>
      <ul>
        {toDoList.map((toDo) => (
          <ToDo {...toDo} key={toDo.id} />
        ))}
      </ul>
    </>
  );
}

export default Home;
