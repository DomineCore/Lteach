<template>
  <div class="login" style="width: 350px">
    <t-form
      :data="formData"
      ref="form"
      @reset="onReset"
      @submit="onSubmit"
      :colon="true"
      :labelWidth="0"
    >
      <t-form-item name='username'>
        <t-input clearable v-model="formData.username" placeholder="请输入账户名">
          <desktop-icon slot="prefix-icon"></desktop-icon>
        </t-input>
      </t-form-item>
      <t-form-item name='password'>
        <t-input type="password" clearable v-model="formData.password" placeholder="请输入密码">
          <lock-on-icon slot="prefix-icon"></lock-on-icon>
        </t-input>
      </t-form-item>
      <t-form-item style="padding-top: 8px">
        <t-button theme="primary" type="submit" block >登录</t-button>
      </t-form-item>
    </t-form>
  </div>
</template>
<script>
import { DesktopIcon, LockOnIcon } from 'tdesign-icons-vue';
import { mapActions } from 'vuex';
import http from '@/api/http.js'
const INITIAL_DATA = {
  username: '',
  password: '',
};

export default {
  components: {
    DesktopIcon, LockOnIcon,
  },
  data() {
    return {
      formData: { ...INITIAL_DATA },
    };
  },

  methods: {
    ...mapActions([
      'login'
    ]),
    onReset() {
      this.$message.success('重置成功');
    },
    async asyncLogin(){
      http.post("/login/", {
        username:this.formData.username,
        password:this.formData.password
      }).then(res=>{
        if(res.status == 200){
          localStorage.setItem("access_token", res.data.token)
          this.$router.push("/home/")
          this.$message.success('登录成功');
        }else{
          this.$message.error("登录失败")
        }
      }).catch(err=>{
        this.$message.error("登录失败")
      })
    },
    onSubmit({ validateResult, firstError }) {
      if (this.formData.username!='' && this.formData.password != '') {
        // 发起请求
        this.asyncLogin()
      } else {
        console.log('Errors: ', validateResult);
        this.$message.warning('请输入用户名或密码');
      }
    },
  },
};
</script>

<style scoped>
  .login{
    margin: 30vh auto;
    height: 20vh;
    width: auto;
  }
</style>
