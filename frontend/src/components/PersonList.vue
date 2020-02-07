<template>
  <b-list-group>
    <b-list-group-item  v-for="(person, id) in this.$store.getters.PERSONS" v-bind:key="id" >
      {{ person['id'] }}<person-details :id="id" :uuid="person['id']"></person-details>
      <delete-person :id="id" :uuid="person['id']"/>
    </b-list-group-item>
  </b-list-group>
</template>

<script>
import PersonDetails from './PersonDetails'
import DeletePerson from './DeletePerson'

export default {
  name: 'PersonList',
  components: {PersonDetails, DeletePerson},
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
