<template>
  <b-button id=id v-on:click="this.deletePerson" variant="danger">Delete</b-button>
</template>

<script>
export default {
  name: 'DeletePerson',
  props: ['uuid', 'id'],
  methods: {
    deletePerson: function () {
      this.$store.dispatch('DELETE_PERSON', {
        id: this.uuid,
        arr_id: this.id
      })
    }
  }
}
</script>

<style scoped>

</style>
