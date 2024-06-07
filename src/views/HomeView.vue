<template>
  <div>
    <div class="row me-3 mt-2">
        <nav>
          <RouterLink to="/sql_typing"><button class="box me-3">SQL查詢</button></RouterLink>
          <RouterLink to="/about"><button class="box me-3">dynascan_main_notification查詢</button></RouterLink>
          <RouterLink to="/displayer_srch"><button class="box me-3">dynascan_main_displayer查詢</button></RouterLink>
          <RouterLink to="/dynascan_main_db"><button class="box me-3">dynascan_main_db</button></RouterLink>
        </nav>
    </div>
    <div class="offset-11">
      <button class="box" @click="sendSQLQuery">function1</button>
    </div>
    <div class="offset-11">
      <button class="box" @click="increment">{{ count }}</button>
      <button class="box" @click="getRandomFromBackend">{{ randomNumber }}</button>
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
          <td v-for="(value, key) in item" :key="key">{{ value }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import API from '../api.js'
import { useRouter } from 'vue-router';

const count = ref(0)
const randomNumber = ref(0)
const jsonArray = ref([])

const getRandomFromBackend = async () => {
  const path = 'http://localhost:5000/api/random'
  try {
    const response = await axios.get(path)
    randomNumber.value = response.data.randomNumber
    console.log("accept!")
  } catch (error) {
    console.log(error)
  }
}

const getRandom = () => {
  getRandomFromBackend()
}

const increment = () => {
  count.value++
}

const dbconnection = async() =>{
  const path = 'http://localhost:5000/db_connect'
  try{
    const response = await API.post(path)
    console.log(response)
  }catch(error){
    console.log(error)
  }

}

const sendSQLQuery = async () => {
  const path = 'http://localhost:5000/wrong_Bonding' // Your SQL query endpoint
  try {
    const response = await API.post(path, { sql: 'YOUR_SQL_QUERY_HERE' })

    jsonArray.value = response.data.data // assuming response.data.data is your JSON array
    console.log(response)
  } catch (error) {
    console.log(error)
  }
}

onMounted(() => {
  getRandom()
})

</script>

<style scoped>
.styled-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #f3f3f3;
  color: #000;
  font-size: 14px; /* 調整字體大小 */
}

.styled-table th,
.styled-table td {
  padding: 8px 10px; /* 調整padding */
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

.div {
  background-color: #fff;
  display: flex;
  padding-bottom: 80px;
  flex-direction: column;
  font-size: 40px;
  color: #000;
  font-weight: 700;
  text-align: center;
}

.box {
  justify-content: center;
  border-radius: 20px;
  background-color: #c5c7cc;
  align-self: end;
  white-space: nowrap;
  letter-spacing: 3px;
  padding: 5px 8px;
  font: 700 20px Inter, sans-serif;
  cursor: pointer; /* 添加鼠標指針 */
  border: none;
}

/* 添加hover時的樣式 */
.box:hover {
  background-color: #4caf50; /* 綠色 */
}
</style>

