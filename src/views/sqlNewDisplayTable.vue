<template>
    <DisplayerNav />
      <div class="row mt-2">
        <div class="col-auto mt-3">
          <div class="col-auto mt-3">
            <h1>
                New Display表格查詢
            </h1>
          </div>
          <div class="col-auto mt-3">
              <button type="button" class="btn btn-secondary" @click="sendSQLQuery('new_display_tab')">產生表格</button>
          </div>
          <div class="col-auto mt-3">
              <button type="button" class="btn btn-secondary" @click="downloadData">Download CSV  <i class="bi bi-download"></i></button>
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