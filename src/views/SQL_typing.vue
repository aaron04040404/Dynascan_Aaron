<template>
    <div>
        <RouterLink to="/">Home</RouterLink>
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
        </div>
    </div>
</template>


<script setup>
import { ref, computed } from 'vue';
import API from '../api.js';


const sql = ref("");

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