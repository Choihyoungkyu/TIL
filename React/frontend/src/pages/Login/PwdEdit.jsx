import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { userActions } from '../../store/modules/userModule';

const pwdEdit = () => {
  const dispatch = useDispatch();

  const [currentPassword, setCurrentPassword] = useState('');
  const [newPassword, setNewPassword] = useState('');
  const [confrimPassword, setConfirmPassword] = useState('');

  const inputCurrentPassword = e => {
    setCurrentPassword(e.target.value);
  };

  const inputNewPassword = e => {
    setNewPassword(e.target.value);
  };

  const inputConfrimPassword = e => {
    setConfirmPassword(e.target.value);
  };

  const passwordEdit = e => {
    e.preventDefault();
    dispatch({
      type: userActions.EDIT_PWD_REQUEST,
      data: {
        nowPassword: currentPassword,
        newPassword: confrimPassword,
      },
    });
  };

  return (
    <div>
      <h1>LOGO</h1>
      <div>
        <h3>비밀번호 변경</h3>
      </div>
      <form onSubmit={passwordEdit}>
        <div>
          <label htmlFor="currentPassword">현재 비밀번호</label>
          <br />
          <input
            required
            value={currentPassword}
            onChange={inputCurrentPassword}
            id="currentPassword"
            type="password"
          />
        </div>
        <div>
          <label htmlFor="newPassword">변경할 비밀번호</label>
          <br />
          <input
            required
            value={newPassword}
            onChange={inputNewPassword}
            id="newPassword"
            type="password"
          />
        </div>
        <div>
          <label htmlFor="confirmPassword">비밀번호 재확인</label>
          <br />
          <input
            required
            value={confrimPassword}
            onChange={inputConfrimPassword}
            id="confirmPassword"
            type="password"
          />
        </div>
        <div>
          <input type="submit" value="확인" />
          <button>취소</button>
        </div>
      </form>
    </div>
  );
};

export default pwdEdit;
