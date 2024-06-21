# Dynascan資料庫報表輸出

製作能夠符合查詢要求的一個前端介面來供公司內部的資料庫查詢  
並且下載成csv檔案儲存起來

## 環境

後端API:Python Flask  
前端:Vue.js  
資料庫:MySQL  
選擇用mysql-connector而不是用pymysql，能夠更好管理，套件也很多，缺點只有不能直接CALL Procedure
其他:Bootstrap5, Pinia


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

## 2024-05-20~2024-05-24

不同的Function執行不同的SQL語法  
SyntaxKisok.py裡的Class SyntaxKisok裡面有最常用到的SQL搜尋Function sqlBondingMainId()….等

## 2024-05-27~2024-05-31

拿到公司的部分資料庫資料，理解每個Table,欄位是什麼功用  
整合一些以前常用的查詢

## 2024-06-03~2024-06-07

把目前用到的SQL查詢都先擺進python function裡面  
每個function在前端都是一顆按鈕連接到flask的API來執行flask指定的function

## 2024-06-10~2024-06-14

確定好各個功能可以使用後開始雕前端:製作Sidebar更簡易的切換頁面


## 2024-06-17

網頁上方也加Navbar能夠在各種查詢頁面中跳轉到想要的地方  
確認輸出好表格後能夠下載csv檔

## 2024-06-18

把一些抽換頁後會繼續保留的地方製作成一個獨立的vue檔在各個會出現的vue中import  
研究Pinia能夠將變數在各個vue中傳送

## 2024-06-19

變數的部分:回傳的錯誤訊息, 回傳查詢成功的data, 已經寫好的查詢直接用同一個function
以上變數都利用Pinia實現

## 2024-06-20

refactor python程式 原本分好處理data的python檔有DownloadData, ReturnData, sqlConvertData, sqlsearchMethod  
將這幾個處理data的Class全部集中進DataProcess裡面



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
