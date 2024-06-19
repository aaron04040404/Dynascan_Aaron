import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import API from '../api.js'


export const useStore = defineStore('store', () =>{
  const jsonArray = ref([]);
  const err_message = ref("");

  const sendSQLQuery = async(route) =>{
    const path = `http://localhost:5000/${route}`
    try {
    const response = await API.post(path, { 
      sql: 'YOUR_SQL_QUERY_HERE'

    })
    
    if(response.data && response.data.data){
      if(response.data.data == []){//在pinia裡面要用 ==
          err_message.value = "沒有查詢到任何東西!!!"
      }
      else{
          jsonArray.value = response.data.data;
          err_message.value = "";
      }
  }
    else{
      jsonArray.value = [];
      err_message.value = response.data.message;
  }
console.log(response)
//console.log(store.jsonArray)
console.log(err_message)
    } catch (error) {
        console.log(error)
    }
  }

  return {jsonArray, sendSQLQuery, err_message}

})
