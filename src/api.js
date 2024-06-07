//初始化整個API物件
import axios from 'axios'

const API = axios.create({
  baseURL: 'http://localhost:5000',
  headers: {
    'Content-Type': 'application/json; charset=utf-8',
    'Cache-Control': 'no-cache',//都做cache
    Pragma: 'no-cache',
    Expires: '0',
    Accept: 'application/json',
    'X-Requested-With': 'XMLHttpRequest'
  },
  withCredentials: true
}) 

export default API;
