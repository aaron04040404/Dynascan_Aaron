<template>

  
</template>

<style>


</style>

<script setup>
/*import { ref, onMounted } from 'vue'
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
})*/

</script>

<style>


</style>

