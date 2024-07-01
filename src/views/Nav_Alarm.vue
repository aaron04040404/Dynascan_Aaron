<template>
    <nav class="navbar navbar-expand-sm navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Alarm相關</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                dropdown
              </a>
              <ul class="dropdown-menu dropdown-menu-dark dropdown-menu-end" aria-labelledby="navbarDarkDropdownMenuLink">
                <li>
                  <a class="sidebar-link" href="/sqlDuplicate_alarm_event">mcb_alarm</a>
                </li>
              </ul>
            </li>
          </ul>
          <form class="d-flex" @submit.prevent="sendSQLQuery2('displayer_realtime')">
            <input v-model="bonding" class="form-control me-2" placeholder="輸入Bonding或sn" aria-label="Search">
            <button class="btn btn-outline-success" type="submit">Search</button>
          </form>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  import API from '../api.js';
  import { useStore } from "@/stores/counter.js";
  import Swal from 'sweetalert2';
  
  const store = useStore();
  //const jsonArray = computed(()=> store.jsonArray);
  
  
  const bonding = ref("")
  const sendSQLQuery2 = async (route) => {
    const path = `http://localhost:5000/${route}`;
    
    try {
      const response = await API.post(path, { 
        bonding: bonding.value 
      })
      if(response.data && response.data.data){
        store.jsonArray = response.data.data;
        if(response.data.data.length == 0){
            store.err_message = "沒有查詢到任何東西!!!"
            Swal.fire({
              title: 'Warning!',
              text: store.err_message,
              icon: 'warning',
              confirmButtonText: 'OK'
            })
        }
        else{
            store.err_message = "";
        }
    }
      else{
        store.jsonArray = [];
        store.err_message = response.data.message;
        Swal.fire({
              title: 'Error!',
              text: store.err_message,
              icon: 'error',
              confirmButtonText: 'OK'
            })
    }
  console.log(response)
  //console.log(store.jsonArray)
  console.log(store.err_message)
    } catch (error) {
      console.log(error);
    }
  };
  
  </script>