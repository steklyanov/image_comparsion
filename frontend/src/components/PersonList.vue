<template>
  <b-list-group>
    <b-list-group-item  v-for="person in persons" >{{ person['id'] }}</b-list-group-item>
  </b-list-group>
</template>

<script>
  import axios from 'axios';
    export default {
        name: "PersonList",

        data() {
          return {
            persons: [],
            errors: []
          };
        },
        created() {
          axios.get('http://127.0.0.1:8000/api/v1/person/list/')
          .then(response => {
            this.persons = response.data
          })
          .catch(e => {
            this.errors.push(e)
          })
        }
    }
</script>

<style scoped>

</style>
