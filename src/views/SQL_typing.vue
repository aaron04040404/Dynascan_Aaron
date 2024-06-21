<template>
  <div class="container">
      <div>
          <h1>輸入SQL語法:</h1>
          <p style="white-space: pre-line;"></p>
          <textarea v-model="sql" placeholder="" style="width: 100%; height: 200px;"></textarea>
      </div>
      <div class="mt-3">
          <div style="display: flex; justify-content: space-between; width: 400px;">
              <button type="button" class="btn btn-secondary" @click="sendSQLQuery_main">use_main</button>
              <button type="button" class="btn btn-secondary" @click="sendSQLQuery_client">use_client</button>
              <button type="button" class="btn btn-secondary" @click="downloadData">Download CSV  <i class="bi bi-download"></i></button>
          </div>
      </div>
    <div class="col-auto">
      <div class="table-container">
      <table v-if="store.jsonArray.length > 0" class="styled-table ">
      <thead>
          <tr>
              <th v-for="(value, key) in store.jsonArray[0]" :key="key">{{ key }}</th>
          </tr>
      </thead>
      <tbody>
          <tr v-for="(item, index) in store.jsonArray" :key="index">
              <td v-for="(value, key) in item" :key="key" style="white-space: nowrap;">{{ value }}</td>
          </tr>
      </tbody>
      </table>
      </div>
      <p v-if="store.jsonArray.length > 0">共有 {{ store.jsonArray.length }} 筆資料</p>
      <p> {{ store.err_message }}</p>
    </div>
  </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import axios from 'axios'
import API from '../api.js';
import { useStore } from "@/stores/counter.js";
import App from '@/App.vue';
import Swal from 'sweetalert2';

const store = useStore();
const sql = ref("");
const err_message = ref("");

const sendSQLQuery_main = async() =>{
const path = 'http://localhost:5000/sql_typing'

try{
    const response = await API.post(path,{
        sql: sql.value,
        database: 'dynascan365_main'
    })
    if(response.data && response.data.data){
      store.jsonArray = response.data.data;
        if(response.data.data.length == 0){
          store.err_message = "沒有查詢到任何東西!!!"
          //Code Copilot說:Pinia 中定義的 state 變量已經被 Pinia 自動包裝，使其成為 reactive 的對象，而不需要顯式地使用 .value。
          //測試下來是沒有被Pinia所包裝的都要用到.value
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

const sendSQLQuery_client = async() =>{
const path = 'http://localhost:5000/sql_typing'

try{
    const response = await API.post(path,{
        sql: sql.value,
        database: 'dynascan365_client'
    })
    if(response.data && response.data.data){
        store.jsonArray = response.data.data;
        err_message.value = "";
    }
    else{
      store.jsonArray = [];
      err_message.value = response.data.message;
    }
  console.log(response)
}catch(error){
console.log(error)
  store.jsonArray = [];
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

<style>
.styled-table {
width: 100%;
border-collapse: collapse;
background-color: #f3f3f3;
color: #000;
font-size: 14px;/* 調整字體大小 */
}

.styled-table th,
.styled-table td {
padding: 8px 10px;
text-align: left;
}

.styled-table th {
background-color: #666;
color: #fff;
}

.styled-table tbody tr:nth-of-type(even) {
background-color: #ddd;
}
.table-container {
max-width: 80%;
max-height: 500px; /* 設置表格容器的最大高度 */
overflow: auto; /* 啟用滾動條 */
margin-top: 20px;
border: 1px solid #ccc;
}
</style>

