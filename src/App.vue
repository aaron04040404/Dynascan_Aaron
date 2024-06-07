<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
    <div class="div div-2">
    database searching
    <br />
    </div>
  
  <RouterView/>
</template>

<style>
.styled-table {
  width: 100%;
  border-collapse: collapse;
  background-color: #f3f3f3;
  color: #000;
}

.styled-table th,
.styled-table td {
  padding: 12px 15px;
  text-align: left;
}

.styled-table th {
  background-color: #666;
  color: #fff;
}

.styled-table tbody tr:nth-of-type(even) {
  background-color: #ddd;
}

.div {
    background-color: #fff;
    display: flex;
    padding-bottom: 80px;
    flex-direction: column;
    font-size: 40px;
    color: #000;
    font-weight: 700;
    text-align: center;
  }
  .div-2 {
    background: linear-gradient(180deg, #5e6df5 0%, #e3e5f1 50.5%);
    width: 100%;
    align-items: center;
    justify-content: center;
    padding: 38px 60px;
    font: 800 64px Jost, sans-serif;
  }
  @media (max-width: 991px) {
    .div-2 {
      max-width: 100%;
      font-size: 40px;
      padding: 0 20px;
    }
  }
  .div-3 {
    font-family: Inter, sans-serif;
    justify-content: center;
    border-radius: 30px;
    background-color: #c5c7cc;
    align-self: start;
    white-space: nowrap;
    letter-spacing: 4px;
    margin: 18px 0 0 38px;
    padding: 1px 20px;
  }
  @media (max-width: 991px) {
    .div-3 {
      margin-left: 10px;
      white-space: initial;
    }
  }
  .div-4 {
    font-family: Inter, sans-serif;
    justify-content: center;
    border-radius: 30px;
    background-color: #c5c7cc;
    align-self: end;
    white-space: nowrap;
    letter-spacing: 4px;
    margin: 88px 42px 0 0;
    padding: 10px 20px;
  }
  @media (max-width: 991px) {
    .div-4 {
      white-space: initial;
      margin: 40px 10px 0 0;
    }
  }
  .box {
    justify-content: center;
    border-radius: 30px;
    background-color: #c5c7cc;
    align-self: end;
    white-space: nowrap;
    letter-spacing: 4px;
    padding: 10px 10px;
    font: 700 20px Inter, sans-serif;
    cursor: pointer; /* 添加鼠標指針 */
	border: none;
  }
  /* 添加hover時的樣式 */
  .box:hover {
    background-color: #4caf50; /* 綠色 */
  }
  @media (max-width: 991px) {
    .box {
      white-space: initial;
      margin: 40px 10px 0 0;
    }
  }
</style>
