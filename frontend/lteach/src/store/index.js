import Vue from 'vue';
import Vuex from 'vuex';
// 引入模块
import token from './token';
import http from '../api/http.js'

Vue.use(Vuex);
//不是在生产环境debug为true
const debug = process.env.NODE_ENV !== 'production';
//创建Vuex实例对象
const store = new Vuex.Store({
    strict:debug,//在不是生产环境下都开启严格模式
    state:{
    },
    getters:{
    },
    mutations:{
    },
    actions:{
        // 登录
        login ({commit, data}) {
            return http.post("/login/", {data}).then(response=>response.data)
        }
    },
    modules: {
    }
})
export default store;

