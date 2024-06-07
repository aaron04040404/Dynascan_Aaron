<template>
    <div class="row">
        <div class='col-1'>
            <nav>
                <button class = 'box' @click="sendSQLQuery">displayer</button>
                <button class = 'box' @click="test_connect">test</button>
            </nav>
        </div>
    </div>
    <div> 
        <table v-if="jsonArray.length > 0" class = "styled-table">
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

const jsonArray = ref([])

const sendSQLQuery = async () => {
  const path = 'http://localhost:5000/sql_searching' // Your SQL query endpoint
  try {
    const response = await API.post(path, { sql: 'YOUR_SQL_QUERY_HERE' })

    //view.value = JSON.stringify(response.data.data, null, 2)
    jsonArray.value = response.data.data // assuming response.data.data is your JSON array
    // Handle response if needed
    console.log(response)
  } catch (error) {
    console.log(error)
  }
}

const test_connect = async () => {
  const path = 'http://localhost:5000/test' // Your SQL query endpoint
  try {
    const response = await API.post(path)
    jsonArray.value = response.data.data
    //view.value = JSON.stringify(response.data.data, null, 2)
    // assuming response.data.data is your JSON array
    // Handle response if needed
    console.log(response)
  } catch (error) {
    console.log(error)
  }
}

</script>