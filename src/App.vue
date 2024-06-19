<template>
    <div class="wrapper">
        <aside id="sidebar">
            <div class="d-flex">
                <button id="toggle-btn" >
                    <i class="bi bi-grid-1x2-fill"></i>
                </button>
                <div class="sidebar-logo">
                    <a href="#">menu</a>
                </div>
                <div class="sidebar-logo ms-3">
                    <a href="/"><i class="bi bi-house"></i></a>
                </div>
                
            </div>
            <ul class="sidebar-nav">
                <li class="sidebar-item">
                    <a href="/sql_typing" class="sidebar-link">
                        <i class="bi bi-filetype-sql"></i>
                        <span>SQL查詢</span>
                    </a>
                </li>
                <li class="sidebar-item">
                    <a href="#" class="sidebar-link has-dropdown collapsed" data-bs-toggle="collapse" data-bs-target="#displayer" 
                        aria-expanded="false" aria-controls="displayer">
                        <i class="bi bi-display"></i>
                        <span>Displayer查詢</span>
                    </a>
                    <ul id="displayer" class="sidebar-dropdown list-unstyle collapse" data-bs-parent="#sidebar">
                        <li class="sidebar-item">
                            <a href="/displayer_srch" class="sidebar-link">displayer即時版本</a>
                        </li>
                        <li class="sidebar-item">
                            <a href="/sqlwrongrealtime_srch" class="sidebar-link">Realtime錯誤查詢 <i class="bi bi-bug-fill"></i></a>
                        </li>
                        <li class="sidebar-item">
                            <a href="/sqlMaindisplayer" class="sidebar-link">MainDisplye查詢</a>
                        </li>
                        <li class="sidebar-item">
                            <a href="/sqlDisplayerRun" class="sidebar-link">有多少機台在運作</a>
                        </li>
                        <li class="sidebar-item">
                            <a href="/sqlDisplayer_inconsistent" class="sidebar-link">正式機Realtime不一致<i class="bi bi-bug-fill"></i></a>
                        </li>
                        <li class="sidebar-item">
                            <a href="/sqlNewDisplayTable" class="sidebar-link">New Display表格查詢</a>
                        </li>
                    </ul>
                </li>
                <li class="sidebar-item">
                    <a href="#" class="sidebar-link has-dropdown collapsed" data-bs-toggle="collapse" data-bs-target="#notification" 
                        aria-expanded="false" aria-controls="notification">
                        <i class="bi bi-megaphone"></i>
                        <span>Notification查詢</span>
                    </a>
                    <ul id="notification" class="sidebar-dropdown list-unstyle collapse" data-bs-parent="#sidebar">
                        <li class="sidebar-item">
                            <a href="/about" class="sidebar-link">mcb某時間內通知</a>
                        </li>
                    </ul>
                </li>
                <li class="sidebar-item">
                    <a href="#" class="sidebar-link has-dropdown collapsed" data-bs-toggle="collapse" data-bs-target="#mcb_alarm" 
                        aria-expanded="false" aria-controls="mcb_alarm">
                        <i class="bi bi-alarm"></i>
                        <span>mcb_alarm查詢</span>
                    </a>
                    <ul id="mcb_alarm" class="sidebar-dropdown list-unstyle collapse" data-bs-parent="#sidebar">
                        <li class="sidebar-item">
                            <a href="#" class="sidebar-link">mcb_alarm</a>
                        </li>
                    </ul>
                </li>
                <li class="sidebar-item">
                    <a href="#" class="sidebar-link has-dropdown collapsed" data-bs-toggle="collapse" data-bs-target="#model" 
                        aria-expanded="false" aria-controls="model">
                        <i class="bi bi-android"></i>
                        <span>Model查詢</span>
                    </a>
                    <ul id="model" class="sidebar-dropdown list-unstyle collapse" data-bs-parent="#sidebar">
                        <li class="sidebar-item">
                            <a href="/sqlModelDifferent" class="sidebar-link">註冊Model不一樣 <i class="bi bi-bug-fill"></i></a>
                        </li>
                    </ul>
                </li>
            </ul>
        </aside>
        <div class="main p-3">
            <div class="text-center">
                <h1>
                    Database Searching
                </h1>
            </div>
            
            <RouterView/>
        </div>
    </div>
    
  
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import HelloWorld from './components/HelloWorld.vue'
import { ref,onMounted } from 'vue';
import '@vuepic/vue-datepicker/dist/main.css'

    
    const toggleSidebar = () => {
      document.querySelector("#sidebar").classList.toggle("expand");
    };

    onMounted(() => {
      const hamBurger = document.querySelector("#toggle-btn");
      hamBurger.addEventListener("click", toggleSidebar);
    });


</script>

<style>

</style>
