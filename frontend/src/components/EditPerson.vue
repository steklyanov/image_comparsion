<template>
  <b-button v-on:click="console.log('click')">Edit</b-button>
</template>

<script>
export default {
  name: 'EditPerson',
  props: ['id'],
  methods: {
    getPerson()
  }
}
</script>

<style scoped>

</style>
