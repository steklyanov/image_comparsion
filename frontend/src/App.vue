<template>
  <div id="app">
    <person-list/>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
import PersonList from "./components/PersonList";
export default {
  name: 'App',
  components: {PersonList}
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
