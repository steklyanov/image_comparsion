<template>
  <div>
    <b-button v-b-modal="'myModal' + id" v-on:click="getPerson">Details</b-button>

    <b-modal :id="'myModal' + id" title="BootstrapVue">
      <p class="my-4">Name: {{this.$store.getters.CURRENT_PERSON.name}}</p>
      <p class="my-4">Surname: {{this.$store.getters.CURRENT_PERSON.surname}}</p>
      <p class="my-4">Vector: {{ getVectorStatus() }}</p>
      <upload-image :id="id" :uuid="uuid" />
    </b-modal>
  </div>
</template>

<script>
import UploadImage from './UploadImage'
export default {
  name: 'PersonDetails',
  components: {UploadImage},
  props: ['uuid', 'id'],
  methods: {
    getPerson: function () {
      this.$store.dispatch('GET_PERSON_DATA', {
        id: this.uuid
      })
    },
    getVectorStatus: function () {
      if (this.$store.getters.CURRENT_PERSON.vector) {
        return ('Yes')
      } else {
        return ('No')
      }
    }
  }
}
</script>

<style scoped>

</style>
