<template>
  <b-list-group>
    <b-list-group-item  v-for="person in this.$store.getters.PERSONS" v-bind:key="person['id']" >
      {{ person['id'] }}

    </b-list-group-item>
  </b-list-group>
</template>

<script>
export default {
  name: 'PersonList',
  data () {
    return {
      persons: [],
      errors: []
    }
  },
  created () {
    this.$store.dispatch('GET_PERSONS')
  }
}
</script>

<style scoped>

</style>
