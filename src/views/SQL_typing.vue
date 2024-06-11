<template>
        <div class="container">
            <div>
                <span>輸入SQL語法:</span>
                <p style="white-space: pre-line;"></p>
                <textarea v-model="sql" placeholder="" style="width: 100%; height: 200px;"></textarea>
            </div>
            <div class="mt-3">
                <div style="display: flex; justify-content: space-between; width: 200px;">
                    <button @click="sendSQLQuery_main">use_main</button>
                    <button @click="sendSQLQuery_client">use_client</button>
                </div>
            </div>
            <div class="table-container">
            <table v-if="jsonArray.length > 0" class="styled-table ">
            <thead>
                <tr>
                    <th v-for="(value, key) in jsonArray[0]" :key="key">{{ key }}</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(item, index) in jsonArray" :key="index">
                    <td v-for="(value, key) in item" :key="key" style="white-space: nowrap;">{{ value }}</td>
                </tr>
            </tbody>
            </table>
            </div>
        
        </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import API from '../api.js';


const sql = ref("");
const jsonArray = ref([])
const sendSQLQuery_main = async() =>{
    const path = 'http://localhost:5000/sql_typing'

    try{
        const response = await API.post(path,{
            sql: sql.value,
            database: 'dynascan365_main'
        })
        jsonArray.value = response.data.data
        console.log(response)
    }catch(error){
    console.log(error)
  }
}

const sendSQLQuery_client = async() =>{
    const path = 'http://localhost:5000/sql_typing'

    try{
        const response = await API.post(path,{
            sql: sql.value,
            database: 'dynascan365_client'
        })
        jsonArray.value = response.data.data
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