<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container-fluid">
        <a class="navbar-brand" href="#">Displayer相關</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDarkDropdown" aria-controls="navbarNavDarkDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDarkDropdown">
          <ul class="navbar-nav">
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" id="navbarDarkDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </a>              
              <ul class="dropdown-menu dropdown-menu-dark" aria-labelledby="navbarDarkDropdownMenuLink">                
                <li>
                  <a class="sidebar-link" href="/displayer_srch">displayer即時版本</a>
                </li>
                <li>
                  <a class="sidebar-link" aria-current="page" href="/sqlwrongrealtime_srch">Realtime錯誤查詢</a>
                </li>
                <li>
                  <a class="sidebar-link" aria-current="page" href="/sqlMaindisplayer">Maindisplayer查詢</a>
                </li>
                <li>
                  <a class="sidebar-link" aria-current="page" href="/sqlDisplayerRun">有多少機台在運作</a>
                </li>
                <li>
                  <a class="sidebar-link" aria-current="page" href="/sqlDisplayerRealtime">正式機Realtime不一致</a>
                </li>
                <li>
                  <a class="sidebar-link" aria-current="page" href="/sqlNewDisplayTable">New Display表格查詢</a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
</template>

<script>

</script>