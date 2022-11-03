<template>
  <div id="app">
    <h1>버튼 박스 제작</h1>
    <div id="page">
      <h2>예약 페이지</h2>
      <h3>시간 선택</h3>
      <div style="display: inline-block; max-width: 400px;">
        <button v-for="(time, index) in times" :key="index" @click="check(index, $event)" class="btn" :id=index>{{time}}</button>
      </div>
      <hr style="width: 400px">
      <h3>선택 시간 : <div v-for="(time, index) in checks" :key="index" style="display: inline-block; width: auto; margin: 0; padding: 0.2rem;">{{time}}</div></h3>
    </div>
  </div>
</template>

<script>

export default {
  name: 'App',
  data: function () {
    return {
      times: [
        "09:00","09:30","10:00","10:30","11:00","11:30","12:00","12:30","13:00","13:30",
        "14:00","14:30","15:00","15:30","16:00","16:30","17:00","17:30","18:00","18:30",
        "19:00","19:30","20:00","20:30","21:00","21:30","22:00","22:30","23:00","23:30",
      ],
      checks: []
    }
  },
  methods: {
    check: function (index, event) {
      if (this.checks.includes(this.times[index])) {
        // 체크 됐으면 삭제
        this.checks.splice(this.checks.indexOf(this.times[index]), 1)
        event.target.classList.remove('checkedBtn')
      } else {
        // 체크 안됐으면 추가
        if ( this.checks.length < 5 ) {
          this.checks.push(this.times[index])
          this.checks.sort()
          event.target.classList.add('checkedBtn')
        } else {
          alert('5타임까지만 신청할 수 있습니다.')
        }
      }
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #424242;
  margin-top: 60px;
}

#page {
  width: 500px;
  height: 330px;
  margin: auto;
  -webkit-box-shadow: 0px 3px 10px -3px rgba(0,0,0,0.35);
  -moz-box-shadow: 0px 3px 10px -3px rgba(0,0,0,0.35);
  box-shadow: 0px 3px 10px -3px rgba(0,0,0,0.35);
}

.btn {
  background: None;
  color: #84898C;
  
  margin: 0;
  padding: 0.3rem 0.8rem;
  
  font-family: 'Noto Sans Korean';
  font-size: 1rem;
  font-weight: 400;
  text-align: center;
  text-decoration: none;
  
  border: none;
  
  display: inline-block;
  width: auto;
  
  cursor: pointer;
}

.btn:hover {
  background: #658dc63d;
  color: #0F4C81;
}

.checkedBtn {
  background: #658dc63d;
  color: #0F4C81;
}
</style>
