import React from "react";
import { useDispatch } from "react-redux";
import { Link } from "react-router-dom";
import { deleteToDo } from "../store";

function ToDo({ text, id }) {
  const dispatch = useDispatch();
  const onBtnClick = () => dispatch(deleteToDo(id));
  return (
    <li>
      <Link to={`/${id}`}>
        {text} 
      </Link>
      <button onClick={onBtnClick}>DEL</button>
    </li>
  );
}

export default ToDo;
