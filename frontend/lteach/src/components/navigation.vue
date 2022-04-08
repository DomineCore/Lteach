<template>
  <div class="box">
    <t-menu theme="dark" id="nav" defaultValue="dashboard" >
      <!-- <img slot="logo" width="136"  src="https://www.tencent.com/img/index/menu_logo.png" alt="logo"> -->
      <span id="logotitle" slot="logo">Lteach | 乐教</span>
      <t-menu-item value="dashboard">
        <template #icon>
          <icon name="dashboard"/>
        </template>
        工作台
      </t-menu-item>
      <t-menu-item value="resource">
        <template #icon>
          <icon name="server"/>
        </template>
        学员列表
      </t-menu-item>
      <t-menu-item value="root">
        <template #icon>
          <icon name="root-list"/>
        </template>
        课程设置
      </t-menu-item>
      <t-menu-item value="control-platform">
        <template #icon>
          <icon name="control-platform"/>
        </template>
        通知系统
      </t-menu-item>
    </t-menu>
  </div>

</template>

<script>
import { Icon } from 'tdesign-icons-vue';

export default {
  components: {
    Icon,
  },
  methods: {
    changeHandler(active) {
      console.log('change', active);
    },
  },
};
</script>

<style scoped>
.box{
  height: 100vh;
  background-color: black;
}
#nav{
  height: 100%;
}
#logotitle{
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: large;
}
</style>
