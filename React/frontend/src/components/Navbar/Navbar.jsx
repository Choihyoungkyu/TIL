import React from 'react';
import { useDispatch } from 'react-redux';
import { Link } from 'react-router-dom';
import { LOG_OUT_REQUEST } from '../../store/modules/userModule';

const Navbar = ({ logInDone }) => {
  const dispatch = useDispatch();
  const logOutBtn = () => {
    dispatch({ type: LOG_OUT_REQUEST });
  };
  return (
    <>
      <Link to="/">Logo </Link>
      {logInDone ? (
        <button onClick={logOutBtn}>로그아웃</button>
      ) : (
        <Link to="/user/login">Login</Link>
      )}
    </>
  );
};

export default Navbar;
