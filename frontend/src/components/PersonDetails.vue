<template>
  <div>
    <b-button v-b-modal="'myModal' + id" v-on:click="getPerson">Details</b-button>

    <b-modal :id="'myModal' + id" title="BootstrapVue">
      <p class="my-4">Name: {{this.$store.getters.CURRENT_PERSON.name}}</p>
      <p class="my-4">Surname: {{this.$store.getters.CURRENT_PERSON.surname}}</p>
    </b-modal>
  </div>
</template>

<script>
export default {
  name: 'PersonDetails',
  props: ['uuid', 'id'],
  // created () {
  //   this.$store.dispatch('GET_PERSON_DATA')
  // },
  methods: {
    getPerson: function () {
      this.$store.dispatch('GET_PERSON_DATA', {
        id: this.uuid
      })
    }
  }
}
</script>

<style scoped>

</style>
