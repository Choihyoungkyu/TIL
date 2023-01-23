import { configureStore } from "@reduxjs/toolkit";
import rootReducer from "./storeindex";

const store = configureStore({
  reducer: rootReducer,
});

export default store;
