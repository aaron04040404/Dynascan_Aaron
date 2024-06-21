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
      jsonArray.value = response.data.data;
      
      //Code Copilot說:要確認組數是否為空，要檢查數組的length而不是用 data == []來檢查
      if(response.data.data.length == 0){
          err_message.value = "沒有查詢到任何東西!!!"
          //Code Copilot說:如果直接用alert(err_message)的話會回傳一個包括value的ref對象，而不是value本身
          Swal.fire({
            title: 'Warning!',
            text: err_message.value,
            icon: 'warning',
            confirmButtonText: 'OK'
          })
      }
      else{
          err_message.value = "";
      }
  }
    else{
      jsonArray.value = [];
      err_message.value = response.data.message;
      Swal.fire({
        title: 'Error!',
        text: err_message.value,
        icon: 'error',
        confirmButtonText: 'OK'
      })
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
