<template>
  <NotificationNav />
      <!-- 左側 -->
      <div>
        <div class="ms-3 mt-3">
          輸入mcb_id:
        </div>
        <div class="ms-3 mt-3">
          <input v-model="mcb_id" placeholder="edit me" />
        </div>
        <div class="ms-3 mt-3">
          <VueDatePicker v-model="startdate" time-picker-inline class="custom-datepicker"></VueDatePicker>
        </div>
        <div class="ms-3 mt-3">
          起始日期: {{ startDate }}
        </div>
        <div class="ms-3 mt-3">
          <VueDatePicker v-model="enddate" time-picker-inline class="custom-datepicker"></VueDatePicker>
        </div>
        <div class="ms-3 mt-3">
          結束日期: {{ endDate }}
        </div>
        <div class="ms-3 mt-3" style="display: flex; justify-content: space-between; width: 200px;">
          <button type="button" class="btn btn-secondary" @click="sendSQLQuery">查詢</button>
          <button type="button" class="btn btn-secondary" @click="downloadData">下載csv檔</button>
        </div>
        <sqlTable/>
      </div>

        
</template>

<script setup>
import { ref, computed } from 'vue';
import axios from 'axios'
import API from '../api.js'
import { format } from 'date-fns';
import NotificationNav from './NotificationNav.vue'
import sqlTable from '@/views/sqlTable.vue'
import VueDatePicker from '@vuepic/vue-datepicker'
import '@vuepic/vue-datepicker/dist/main.css'

const mcb_id = ref("");
const startdate = ref(null);
const enddate = ref(null);
const jsonArray = ref([])

const startDate = computed(() => {
  if (!startdate.value) return '';
  return format(new Date(startdate.value), 'yyyy-MM-dd HH:mm:ss');
});

const endDate = computed(() => {
  if (!enddate.value) return '';
  return format(new Date(enddate.value), 'yyyy-MM-dd HH:mm:ss');
});

const sendSQLQuery = async() =>{
  const path = 'http://localhost:5000/Notification_between_date'
  try{
    const response = await API.post(path, {
      mcb_id: mcb_id.value,
      startDate: startDate.value,
      endDate: endDate.value

    })
    jsonArray.value = response.data.data
    console.log(response)
  }catch(error){
    console.log(error)
  }
}

const downloadData = async() =>{
        const path = 'http://localhost:5000/download'
        try{
            const response = await axios.post(path, {
              data: jsonArray.value,
              fileType: 'csv'
            })
            const csv = response.data;
            const link =document.createElement("a");
            link.target = "_blank";
            link.href = "data:text/csv;charset=utf-8," + encodeURIComponent(csv);
            link.download = "data.csv";
            link.click();
            console.log(response)
        }catch(error){
        console.log(error)
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
