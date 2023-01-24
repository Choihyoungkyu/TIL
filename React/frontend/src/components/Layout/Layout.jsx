import React, { useEffect } from 'react';
import PropTypes from 'prop-types';
import { useDispatch, useSelector } from 'react-redux';
import Navbar from '../Navbar/Navbar';
import { userAction } from '../../store/modules/userModule';

const Layout = ({ children }) => {
  const dispatch = useDispatch();
  // 로그인 확인 변수
  const { logInDone } = useSelector(state => state.user);
  useEffect(() => {
    if (!logInDone && sessionStorage.userToken) {
      dispatch({ type: userAction.LOG_IN_SUCCESS });
    }
  }, [dispatch, logInDone]);

  return (
    <div>
      <Navbar logInDone={logInDone} />
      <main>{children}</main>
    </div>
  );
};

Layout.propsTypes = {
  children: PropTypes.node.isRequired,
};

export default Layout;
