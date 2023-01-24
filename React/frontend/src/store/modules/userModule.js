import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  // 회원가입
  signUpRequest: false,
  signUpDone: false,
  signUpError: null,
  // 로그인
  logInRequest: false,
  logInDone: false,
  logInError: null,
  // 아이디 찾기
  findIdRequest: false,
  findIdDone: false,
  findIdError: null,
  // 비밀번호 찾기
  findPwdRequest: false,
  findPwdDone: false,
  findPwdError: null,
  // 비밀번호 변경
  editPwdRequest: false,
  editPwdDone: false,
  editPwdError: null,
  // 로그인 상태 유지
  getMyInfoRequest: false,
  getMyInfoDone: false,
  getMyInfoError: null,
};

// 회원가입
export const SIGN_UP_REQUEST = 'SIGN_UP_REQUEST';
export const SIGN_UP_SUCCESS = 'SIGN_UP_SUCCESS';
export const SIGN_UP_FAILURE = 'SIGN_UP_FAILURE';
// 로그인
export const LOG_IN_REQUEST = 'LOG_IN_REQUEST';
export const LOG_IN_SUCCESS = 'LOG_IN_SUCCESS';
export const LOG_IN_FAILURE = 'LOG_IN_FAILURE';
// 아이디 찾기
export const FIND_ID_REQUEST = 'FIND_ID_REQUEST';
export const FIND_ID_SUCCESS = 'FIND_ID_SUCCESS';
export const FIND_ID_FAILURE = 'LOG_IN_FAILURE';
// 비밀번호 찾기
export const FIND_PWD_REQUEST = 'FIND_PWD_REQUEST';
export const FIND_PWD_SUCCESS = 'FIND_PWD_SUCCESS';
export const FIND_PWD_FAILURE = 'FIND_PWD_FAILURE';
// 비밀번호 변경
export const EDIT_PWD_REQUEST = 'EDIT_PWD_REQUEST';
export const EDIT_PWD_SUCCESS = 'EDIT_PWD_SUCCESS';
export const EDIT_PWD_FAILURE = 'EDIT_PWD_FAILURE';
// 자기 자신의 회원정보 불러오기
export const GET_MY_INFO_REQUEST = 'GET_MY_INFO_REQUEST';
export const GET_MY_INFO_SUCCESS = 'GET_MY_INFO_SUCCESS';
export const GET_MY_INFO_FAILURE = 'GET_MY_INFO_FAILURE';

const reducer = createSlice({
  name: 'userReducer',
  initialState,
  reducers: {
    SIGN_UP_REQUEST: state => {
      state.signUpRequest = true;
      state.signUpDone = false;
      state.signUpError = null;
      console.log(`회원가입 시도 ${state.signUpRequest}`);
    },
    SIGN_UP_SUCCESS: state => {
      state.signUpRequest = false;
      state.signUpDone = true;
    },
    SIGN_UP_FAILURE: (state, action) => {
      state.signUpRequest = false;
      state.signUpError = action.error;
    },
    LOG_IN_REQUEST: state => {
      state.logInRequest = true;
      state.logInDone = false;
      state.logInError = null;
    },
    LOG_IN_SUCCESS: state => {
      state.logInRequest = false;
      state.logInDone = true;
    },
    LOG_IN_FAILURE: (state, action) => {
      state.logInRequest = false;
      state.logInError = action.error;
    },
    FIND_ID_REQUEST: state => {
      state.findIdRequest = true;
      state.findIdDone = false;
      state.findIdError = null;
    },
    FIND_ID_SUCCESS: state => {
      state.findIdRequest = false;
      state.logInDone = true;
    },
    FIND_ID_FAILURE: (state, action) => {
      state.findIdRequest = false;
      state.findIdError = action.error;
    },
    FIND_PWD_REQUEST: state => {
      state.findPwdRequest = true;
      state.findPwdDone = false;
      state.findPwdError = null;
    },
    FIND_PWD_SUCCESS: state => {
      state.findPwdRequest = false;
      state.findPwdDone = true;
    },
    FIND_PWD_FAILURE: (state, action) => {
      state.findPwdRequest = false;
      state.findPwdDone = true;
      state.findPwdError = action.error;
    },
    EDIT_PWD_REQUEST: state => {
      state.editPwdRequest = true;
      state.editPwdDone = false;
      state.editPwdError = null;
    },
    EDIT_PWD_SUCCESS: state => {
      state.editPwdRequest = false;
      state.editPwdDone = true;
    },
    EDIT_PWD_FAILURE: (state, action) => {
      state.editPwdRequest = false;
      state.editPwdDone = true;
      state.editPwdError = action.error;
    },
    GET_MY_INFO_REQUEST: state => {
      state.getMyInfoRequest = true;
      state.getMyInfoDone = false;
      state.getMyInfoError = null;
    },
    GET_MY_INFO_SUCCESS: state => {
      state.getMyInfoRequest = false;
      state.getMyInfoDone = true;
    },
    GET_MY_INFO_FAILURE: (state, action) => {
      state.getMyInfoRequest = false;
      state.getMyInfoDone = false;
      state.getMyInfoError = action.error;
    },
  },
});

export const userAction = reducer.actions;
export default reducer.reducer;
