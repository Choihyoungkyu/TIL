import { all, call, fork, put, takeLatest } from '@redux-saga/core/effects';
// import { Route } from 'react-router';
import Swal from 'sweetalert2';
import { CONTEXT_URL } from '../../utils/urls';
import {
  signUpAPI,
  logInAPI,
  findIdAPI,
  findPwdAPI,
  editPwdAPI,
  getMyInfoAPI,
} from '../apis/userApi';
import {
  SIGN_UP_REQUEST,
  LOG_IN_REQUEST,
  FIND_ID_REQUEST,
  FIND_PWD_REQUEST,
  EDIT_PWD_REQUEST,
  GET_MY_INFO_REQUEST,
  LOG_OUT_REQUEST,
} from '../modules/userModule';
/* eslint-disable */
// 회원가입
function* singUp(action) {
  try {
    const result = yield call(signUpAPI, action.data);
    yield put({ type: 'SIGN_UP_SUCCESS', data: result.data });
    Swal.fire({
      title: '회원가입 성공',
      text: '',
      icon: 'success',
    }).then(() => {
      location.href = `${CONTEXT_URL}user/login`;
    });
  } catch (err) {
    yield put({
      type: 'SIGN_UP_FAILURE',
      data: err,
    });
    Swal.fire({
      title: '회원가입 실패',
      text: '',
      icon: 'error',
    });
  }
}

function* watchSignup() {
  yield takeLatest(SIGN_UP_REQUEST, singUp);
}

// 로그인
function* logIn(action) {
  try {
    const result = yield call(logInAPI, action.data);
    console.log(`${result} 로그인 성공`);
    yield put({ type: 'LOG_IN_SUCCESS', data: result.data });
    console.log(`${result.data} 토큰 반환 성공`);
    sessionStorage.setItem('userToken', result.data);
    location.href = `${CONTEXT_URL}`;
  } catch (err) {
    Swal.fire({
      title: '로그인 실패',
      text: '아이디와 비밀번호를 확인해주세요',
      icon: 'error',
    });
    yield put({ type: 'LOG_IN_FAILURE', data: err });
    // console.log(err);
  }
}

function* watchLogin() {
  yield takeLatest(LOG_IN_REQUEST, logIn);
}

// 로그아웃
function* logOut(action) {
  try {
    const result = yield call(logOutAPI, action.data);
    yield put({ type: LOG_OUT_SUCCESS, data: result.data });
    sessionStorage.clear();
    document.location.href = '/';
  } catch (err) {
    yield put({ type: 'LOG_OUT_FAILURE' });
  }
}

function* watchLogOut() {
  yield takeLatest(LOG_OUT_REQUEST, logOut);
}

// 아이디 찾기
function* findId(action) {
  try {
    const result = yield call(findIdAPI, action.data);
    yield put({ type: 'FIND_ID_SUCCESS', data: result.data });
    Swal.fire({
      title: '아이디 찾기 완료',
      text: 'ID : ' + result.data,
      icon: 'success',
    }).then(() => {
      location.href = `${CONTEXT_URL}user/login`;
    });
  } catch (err) {
    Swal.fire({
      title: '아이디 찾기 실패',
      text: '아이디와 이메일을 확인해주세요',
      icon: 'error',
    });
    yield put({ type: 'FIND_ID_FAILURE', data: err });
    // console.log(err);
  }
}

function* watchFindId() {
  yield takeLatest(FIND_ID_REQUEST, findId);
}

// 비밀번호 찾기
function* findPwd(action) {
  try {
    const result = yield call(findPwdAPI, action.data);
    console.log(result);
    yield put({ type: 'FIND_PWD_SUCCESS', data: result.data });
    Swal.fire({
      title: ' 비밀번호 찾기',
      text: '등록하신 이메일로 새로운 임시 비밀번호를 전송하였습니다.',
      icon: 'success',
      confirmButtonText: '로그인',
      confirmButtonColor: 'success',
    }).then(() => {
      location.href = `${CONTEXT_URL}user/login`;
    });
  } catch (err) {
    Swal.fire({
      title: '비밀번호 찾기 실패',
      text: '성명, 아이디, 이메일을 확인해주세요',
      icon: 'error',
    });
    yield put({ type: 'FIND_PWD_FAILURE', data: err });
    // console.log(err);
  }
}

function* watchFindPwd() {
  yield takeLatest(FIND_PWD_REQUEST, findPwd);
}

// 비밀번호 변경
function* editPwd(action) {
  try {
    const result = yield call(editPwdAPI, action.data);
    console.log(result);
    yield put({ type: 'EDIT_PWD_SUCCESS', data: result.data });
    Swal.fire({
      title: ' 비밀번호 변경',
      text: '새로운 비밀번호로 변경되었습니다.',
      icon: 'success',
    });

    // .then(() => {
    //   location.href = `${CONTEXT_URL}`;
    // });
  } catch (err) {
    Swal.fire({
      title: '비밀번호 변경 실패',
      text: '비밀번호를 다시 작성해주세요',
      icon: 'error',
    });
    yield put({ type: 'EDIT_PWD_FAILURE', data: err });
    // console.log(err);
  }
}

function* watchEditPwd() {
  yield takeLatest(EDIT_PWD_REQUEST, editPwd);
}

// 로그인 상태 확인
function* getMyInfo(action) {
  try {
    const result = yield call(getMyInfoAPI, action.data);
    console.log(result);
    yield put({ type: 'GET_MY_INFO_REQUEST', data: result.data });
  } catch (err) {
    yield put({ type: 'GET_MY_INFO_FAILURE', data: err });
  }
}

function* watchGetMyInfo() {
  yield takeLatest(GET_MY_INFO_REQUEST, getMyInfo);
}

export default function* userSaga() {
  yield all([
    fork(watchSignup),
    fork(watchLogin),
    fork(watchLogOut),
    fork(watchFindId),
    fork(watchFindPwd),
    fork(watchEditPwd),
    fork(watchGetMyInfo),
  ]);
}
