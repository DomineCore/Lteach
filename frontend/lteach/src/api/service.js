import axios from 'axios'

const AJAX_URL = "http://127.0.0.1:8000/"

// 1-创建service（axios实例）
console.log(AJAX_URL)
const service = axios.create({
    baseURL: AJAX_URL,
    // api默认超时时间：3s
    withCredentials: true, // 解决服务器设置token到cookies中，浏览器Application的cookies中没有存入token
    timeout: 3*1000
})

// 2-请求拦截处理
service.interceptors.request.use(config => {
    // 从cookies注入token
    const token = localStorage.getItem('access_token')
    if (token) {
        config.headers.Authorization = 'JWT ' + token
    }
    console.log(config)
    return config
}, error => {
    Promise.reject(error)
})

// 3-响应拦截处理
service.interceptors.response.use(response => {
    return response
},error => {
    // 收到异常响应
    if (error && error.response) {
        switch (error.response.status) {
            case 400:
              error.message = '错误请求'
              break;
            case 401:
              error.message = '登录过期，请重新登录'
              // window.location.href=window.location.protocol+'//'+window.location.hostname + '/login'
              window.location.href = "/#/login"
              break;
            case 403:
              error.message = '权限不足，拒绝访问'
              break;
            case 404:
              error.message = '请求错误,未找到该资源'
              window.location.href = "/NotFound"
              break;
            case 405:
              error.message = '请求方法未允许'
              break;
            case 408:
              error.message = '请求超时'
              break;
            case 500:
              error.message = '服务器端出错'
              break;
            case 501:
              error.message = '网络未实现'
              break;
            case 502:
              error.message = '网络错误'
              break;
            case 503:
              error.message = '服务不可用'
              break;
            case 504:
              error.message = '网络超时'
              break;
            case 505:
              error.message = 'http版本不支持该请求'
              break;
            default:
              error.message = `连接错误${error.response.status}`
          }
    } else {
        // 响应超时
        if (JSON.stringify(error).includes('timeout')) {
            // 超时提醒
        }
        error.message = '网络异常'
    }
    // 展示异常信息
    return error.response.data
})


// 4-暴露service实例
export default service
