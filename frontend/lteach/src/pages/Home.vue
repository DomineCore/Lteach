<template>
  <div class="home" style="width: 350px">
    主页
  </div>
</template>
<script>
import { DesktopIcon, LockOnIcon } from 'tdesign-icons-vue';
import { mapActions } from 'vuex';
import http from '@/api/http.js'

export default {
  components: {
    DesktopIcon, LockOnIcon,
  },
  mounted() {
    http.get("/test/")
  }
  
};
</script>

<style scoped>
  .login{
    margin: 30vh auto;
    height: 20vh;
    width: auto;
  }
</style>
