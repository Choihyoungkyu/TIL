import axios from 'axios';
import { BASE_URL } from '../../utils/urls';

// 회원가입
export async function signUpAPI({
  name,
  age,
  si,
  gun,
  dong,
  email,
  id,
  pwd,
  nick,
  gender,
  weight,
  // bikeweight,
  // imagePath,
  open,
}) {
  const result = await axios.post(`${BASE_URL}user/signup`, {
    name,
    age,
    si,
    gun,
    dong,
    email,
    id,
    password: pwd,
    permission: 0,
    nickname: nick,
    gender,
    weight,
    // bikeweight,
    // image_path: imagePath,
    image_path: 'imagePath',
    open,
  });
  return result;
}

// 로그인
export async function logInAPI({ id, password }) {
  const result = await axios.post(`${BASE_URL}user/login`, {
    id,
    password,
  });
  // console.log(result);
  return result;
}

// 아이디찾기
export async function findIdAPI({ name, email }) {
  const result = await axios.post(`${BASE_URL}user/findId`, {
    name,
    email,
  });
  // console.log(result);
  return result;
}

// 비밀번호 찾기
export async function findPwdAPI({ name, id, email }) {
  const result = await axios.post(`${BASE_URL}user/findPassword`, {
    name,
    id,
    email,
  });
  // console.log(result);
  return result;
}

// 비밀번호 변경
export async function editPwdAPI({ nowPassword, newPassword }) {
  const result = await axios.post(`${BASE_URL}user/changePassword`, {
    nowPassword,
    newPassword,
  });
  // console.log(result);
  return result;
}

// Email 인증 보내기
export async function sendMailAPI(email) {
  const result = await axios.get(`${BASE_URL}user/registerMail`, {
    params: { email },
  });
  return result;
}

// Email 인증 확인
export async function checkCertiAPI(code) {
  const promise = await axios.get(`${BASE_URL}user/certMail`, {
    params: { code },
  });
  return promise.data;
}

// 아이디 중복 체크
export async function checkIdAPI(id) {
  const promise = await axios.get(`${BASE_URL}user/signup/id`, {
    params: { id },
  });
  // console.log(promise.data);
  return promise.data;
}

// 닉네임 중복 체크
export async function checkNickAPI(nick) {
  const promise = await axios.get(`${BASE_URL}user/signup/nickname`, {
    params: { nickname: nick },
  });
  return promise.data;
}

// 프로필사진 업로드
export async function imageAPI(formData) {
  const result = await axios.post(`${BASE_URL}user/image`, formData);
  return result;
}

// 로그인 상태 확인
export async function getMyInfoAPI(token, id) {
  const result = await axios.post(`${BASE_URL}user/getUserInfo`, {
    token,
    id,
  });
  return result;
}
