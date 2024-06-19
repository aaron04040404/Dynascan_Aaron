<template>
    <div class="col-auto">
        <div  v-if="store.jsonArray.length > 0" class="table-container">
          <table class="styled-table">
            <thead>
              <tr>
                <th v-for="(value, key) in store.jsonArray[0]" :key="key">{{ key }}</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(item, index) in store.jsonArray" :key="index">
                <td v-for="(value, key) in item" :key="key">{{ value }}</td>
              </tr>
            </tbody>
          </table> 
        </div>       
        <p v-if="store.jsonArray.length > 0">共有 {{ store.jsonArray.length }} 筆資料</p>
        <h2> {{ store.err_message }}</h2>
      </div>
</template>

<script setup>
import {ref, computed} from 'vue'
import { useStore } from "@/stores/counter.js";
const store = useStore();
const jsonArray = computed(()=> store.jsonArray);

</script>