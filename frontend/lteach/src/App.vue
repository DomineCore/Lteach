<template>
  <div id="app">
    <t-layout>
      <t-aside id="aside" v-if="!$route.meta.hiddenNav">
        <navigation v-if="!$route.meta.hiddenNav"></navigation>
      </t-aside>
      <t-layout id="layout">
        <!-- <t-header id="header" v-if="!$route.meta.showNav">Header</t-header> -->
        <t-content id="content"><router-view /></t-content>
        <t-footer id="footer">乐教 ©2022-03</t-footer>
      </t-layout>
    </t-layout>
  </div>
</template>

<script>
import navigation from "@/components/navigation.vue";
export default {
  name: "App",
  components: {
    navigation
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
#layout {
  height: 100vh;
  margin: 0;
}
#aside {
  height: 100vh;
  margin: 0;
}
#header {
  height: 5%;
  background-color: red;
}
</style>
