import React, { Suspense, lazy } from 'react';

import { Route, Routes } from 'react-router-dom';
// import { PrivateRoute } from './PrivateRoute';

const MainPage = lazy(() => import('../pages/Main/Main'));
const LoginPage = lazy(() => import('../pages/Login/Login'));
const SignupPage = lazy(() => import('../pages/Signup/Signup'));
const IDSearchPage = lazy(() => import('../pages/Login/IDSearch'));
const PwdSearchPage = lazy(() => import('../pages/Login/PwdSearch'));
const PwdEditPage = lazy(() => import('../pages/Login/PwdEdit'));

const Router = () => {
  console.log('Router.jsx');
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <Routes>
        <Route path="/" element={<MainPage />} />
        <Route path="/user/login" element={<LoginPage />} />
        <Route path="/user/signup" element={<SignupPage />} />
        <Route path="/user/findId" element={<IDSearchPage />} />
        <Route path="/user/findPwd" element={<PwdSearchPage />} />
        <Route path="/user/editPwd" element={<PwdEditPage />} />
      </Routes>
    </Suspense>
  );
};

export default Router;

// const routes = [
//   {
//     path: '/main',
//     element: <MainPage />,
//   },
// ];
