# Dynascan資料庫報表輸出

製作能夠符合查詢要求的一個前端介面來供公司內部的資料庫查詢  
並且下載成csv檔案儲存起來

## 環境

後端API:Python Flask  
前端:Vue.js  
資料庫:MySQL  
選擇用mysql-connector而不是用pymysql，能夠更好管理，套件也很多，缺點只有不能直接CALL Procedure


## 2024-05-12

建置flask開發環境

## 2024-05-13

製作按鈕回傳路由開啟新的頁面(都是醜醜的)  
製作文字輸入框

## 2024-05-14

把原本傳統的html轉換成Vue，並將flask跟Vue搭建起來傳輸要的response

## 2024-05-15

flask回傳給frontend的response設置為JSON格式，進行傳送資料時都先檢查response是否為要的格式  
開始做後台需要的SQL語法查詢:function, View, index

## 2024



## Recommended IDE Setup

[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Customize configuration

See [Vite Configuration Reference](https://vitejs.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```

### Lint with [ESLint](https://eslint.org/)

```sh
npm run lint
```
