import { combineReducers } from 'redux';
// toDos.reducer가 자동으로 toDosReducer로 바뀜
import toDosReducer from './toDosSaga';

const rootReducer = combineReducers({
  toDos: toDosReducer,
});

export default rootReducer;