<template>
  <div id="app">
    <person-create/>
    <person-list/>
    <img src="./assets/logo.png">
    <router-view/>
  </div>
</template>

<script>
import PersonList from "./components/PersonList";
import PersonCreate from "./components/PersonCreate";
export default {
  name: 'App',
  components: {PersonCreate, PersonList}
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
