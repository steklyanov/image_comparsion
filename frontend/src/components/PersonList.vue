<template>
  <b-list-group>
    <b-list-group-item  v-for="(person, id) in this.$store.getters.PERSONS" v-bind:key="person['id']" >
      {{ person['id'] }}<person-details :id="id" :uuid="person['id']"></person-details>

    </b-list-group-item>
  </b-list-group>
</template>

<script>
import PersonDetails from './PersonDetails'

export default {
  name: 'PersonList',
  components: {PersonDetails},
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
