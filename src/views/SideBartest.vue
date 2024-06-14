<template>
    <div class="wrapper">
        <aside id="sidebar">
            <div class="d-flex">
                <button id="toggle-btn" type="button">
                    <i class="bi bi-grid-1x2-fill"></i>
                </button>
                <div class="sidebar-logo">
                    <a href="#">menu</a>
                </div>
            </div>
            <ul class="sidebar-nav">
                <li class="sidebar-item">
                    <a href="#" class="sidebar-link">
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
                            <a href="#" class="sidebar-link">displayer即時版本</a>
                        </li>
                        <li class="sidebar-item">
                            <a href="#" class="sidebar-link">Realtime錯誤查詢</a>
                        </li>
                        <li class="sidebar-item">
                            <a href="#" class="sidebar-link">MainDisplye查詢</a>
                        </li>
                    </ul>
                </li>
                <li class="sidebar-item">
                    <a href="#" class="sidebar-link has-dropdown collapsed" data-bs-toggle="collapse" data-bs-target="#auth" 
                        aria-expanded="false" aria-controls="auth">
                        <i class="bi bi-megaphone"></i>
                        <span>Notification查詢</span>
                    </a>
                </li>
            </ul>
        </aside>
        <div class="main p-3">
            <div class="text-center">
                <h1>
                    Database Searching
                </h1>
            </div>
        </div>
    </div>
</template>


<script setup>
import { onMounted } from 'vue';


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