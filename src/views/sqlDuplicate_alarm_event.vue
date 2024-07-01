<template>
    <Nav_Alarm />
    <div class="mt-3">
        <h1>mcb_alarm</h1>
    </div>
      <!-- 左側 -->
      <div>
        <div class="ms-3 mt-3">
          選擇alarm結束日期:
        </div>
        <div class="ms-3 mt-3">
          <VueDatePicker v-model="end_on_date" time-picker-inline class="custom-datepicker"></VueDatePicker>
        </div>
        <div class="ms-3 mt-3">
          end_on_Date: {{ end_on_Date }}
        </div>
        <div class="mt-3">
            <button type="button" class="btn btn-secondary" @click="sendSQLQuery">查詢</button>
        </div>
        <div class="mt-3">
            <button type="button" class="btn btn-secondary" @click="downloadData">Download CSV  <i class="bi bi-download"></i></button>
        </div>
        <sqlTable/>
      </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import axios from 'axios'
import API from '../api.js'
import { useStore } from "@/stores/counter.js";
import { format } from 'date-fns';
import Nav_Alarm from '@/views/Nav_Alarm.vue';
import sqlTable from '@/views/sqlTable.vue';
import '@vuepic/vue-datepicker/dist/main.css'
import VueDatePicker from '@vuepic/vue-datepicker';
import Swal from 'sweetalert2';


const store = useStore();
const end_on_date = ref(null);
const downloadData = store.downloadData;


const end_on_Date = computed(() => {
  if (!end_on_date.value) return '';
  return format(new Date(end_on_date.value), 'yyyy-MM-dd HH:mm:ss');
});

const sendSQLQuery = async() =>{
  const path = 'http://localhost:5000/duplicate_alarm_event'
  try{
    const response = await API.post(path, {
      end_on_date: end_on_Date.value,
      

    })

    if(response.data && response.data.data){
      store.jsonArray = response.data.data;
        if(response.data.data.length == 0){
          store.err_message = "沒有查詢到任何東西!!!"
          Swal.fire({
            title: 'Warning!',
            text: store.err_message,
            icon: 'warning',
            confirmButtonText: 'OK'
          })
        }
        else{
          store.err_message = "";
        }
    }
    else{
      store.jsonArray = [];
      store.err_message = response.data.message;
      Swal.fire({
            title: 'Error!',
            text: store.err_message,
            icon: 'error',
            confirmButtonText: 'OK'
          })
    }
  console.log(response)
  //console.log(store.jsonArray)
  console.log(store.err_message)
}catch(error){
console.log(error)
  store.jsonArray = [];
}
}



</script>

<style scoped>
.custom-datepicker {
  width: 200px;
  height: 40px; 
}
.box {
    justify-content: center;
    border-radius: 30px;
    background-color: #c5c7cc;
    align-self: end;
    white-space: nowrap;
    letter-spacing: 4px;
    padding: 10px 10px;
    font: 700 20px Inter, sans-serif;
    cursor: pointer; /* 添加鼠標指針 */
	border: none;
  }
  /* 添加hover時的樣式 */
  .box:hover {
    background-color: #4caf50; /* 綠色 */
  }
  @media (max-width: 991px) {
    .box {
      white-space: initial;
      margin: 40px 10px 0 0;
    }
  }
</style>