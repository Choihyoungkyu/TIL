import { createSlice } from "@reduxjs/toolkit";
  
const toDos = createSlice({
  name: "toDos",
  initialState: [],
  reducers: {
    addToDo: (state, action) => {
      state.push({ text: action.payload, id: Date.now() });
    },
    deleteToDo: (state, action) =>
      state.filter((toDo) => toDo.id !== action.payload),
  },
});

export const { addToDo, deleteToDo } = toDos.actions;

export default toDos.reducer;   // 이렇게 export 하면 toDosReducer로 됨