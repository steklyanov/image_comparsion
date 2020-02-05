<template>
  <div>
    <b-button v-on:click="editPerson">Button</b-button>
    <b-button variant="danger">Button</b-button>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'ButtonGroup',
  props: ['id'],
  methods: {
    editPerson: function () {
      axios.get('http://127.0.0.1:8000/api/v1/person/details/{{id}}/')
        .then(response => {
          this.persons = response.data
        })
        .catch(e => {
          this.errors.push(e)
        })
    }
  }
}
</script>

<style scoped>

</style>
