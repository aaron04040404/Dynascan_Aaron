<template>
  <DisplayerNav />
    <div class="row">
      <div class="col-auto mt-3">
        <div class="mt-3">
          <h1>
            displayer即時版本查詢
          </h1>
        </div>
        <div class="mt-3">
            <button type="button" class="btn btn-secondary" @click="sendSQLQuery('immediate_version')">產生表格</button>
        </div>
        <div class="mt-3">
            <button type="button" class="btn btn-secondary" @click="downloadData">下載CSV檔</button>
        </div>
      </div>
    </div>
    <sqlTable />
    
</template>

<script setup>
    import {ref, computed} from 'vue'
    import axios from 'axios'
    import API from '../api.js'
    import DisplayerNav from '@/views/DisplayerNav.vue'
    import sqlTable from '@/views/sqlTable.vue'

    import { useStore } from "@/stores/counter.js";
    const store = useStore();
    const jsonArray = computed(()=> store.jsonArray);
    const sendSQLQuery = store.sendSQLQuery;

    /*const sendSQLQuery = async(route) =>{
        const path = `http://localhost:5000/${route}`
        try {
        const response = await API.post(path, { sql: 'YOUR_SQL_QUERY_HERE' })

        jsonArray.value = response.data.data // assuming response.data.data is your JSON array
        console.log(response)
        } catch (error) {
            console.log(error)
        }
    }*/
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

<style>

</style>