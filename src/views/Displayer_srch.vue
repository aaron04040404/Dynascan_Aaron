<template>
    <div class="row mt-2">
        <div class="col-md-auto">
            <button class="box" @click="sendSQLQuery('version')">displayer即時版本查詢</button>
        </div>
        <div class="col-md-auto">
            <button class="box" @click="sendSQLQuery('wrong_Bonding')">realtime錯誤查詢</button>
        </div>
        <div class="col-md-auto">
            <button class="box" @click="sendSQLQuery('maindisplayer')">MainDisplayer查詢</button>
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
  <div class="row mt-2">
    <button class="offset-8" style="justify-content: space-between; width: 150px;" @click="downloadData">下載CSV檔</button>
  </div>
    
</template>

<script setup>
    import {ref} from 'vue'
    import axios from 'axios'
    import API from '../api.js'

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