<template>
  
    <DisplayerNav />
      <div class="row mt-2">
        <div class="col-auto mt-3">
          <div class="col-auto mt-3">
            <h1>
              正式機Realtime不一致
            </h1>
          </div>
          <div class="col-auto mt-3">
              <button type="button" class="btn btn-secondary" @click="sendSQLQuery('displayer_realtime')">產生表格</button>
          </div>
          <div class="col-auto mt-3">
              <button type="button" class="btn btn-secondary" @click="downloadData">下載CSV檔</button>
          </div>
        </div>
        <div class="col-auto">
          <div class="table-container">
            <table v-if="jsonArray.length > 0" class="styled-table">
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
        </div>
      </div>
      
</template>
  
  <script setup>
      import {ref} from 'vue'
      import axios from 'axios'
      import API from '../api.js'
      import { useCounterStore } from "@/stores/counter.js";
      import DisplayerNav from '@/views/DisplayerNav.vue'
      const counterStore = useCounterStore();
      const jsonArray = ref([])
  
  
      const sendSQLQuery = async(route) =>{
          const path = `http://localhost:5000/${route}`
          try {
          const response = await API.post(path, { sql: 'YOUR_SQL_QUERY_HERE' })
  
          jsonArray.value = response.data.data // assuming response.data.data is your JSON array
          console.log(response)
          } catch (error) {
              console.log(error)
          }
      }
      //下載csv檔
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