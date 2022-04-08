import http from '../../api/http.js'
const token = {
//多个模块,需要设置命名空间,它的所有 getter、action 及mutation 都会自动根据模块注册的路径调整命名
    namespaced: true, 
    state:{},
    mutations:{},
    actions:{
        // 登录
        login ({commit, data}) {
            return http.post("/login/", {data}).then(response=>response.data)
        }
    }
}
export default{
    token:token
}