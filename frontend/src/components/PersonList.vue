<template>
  <b-list-group>
    <b-col lg="4" class="pb-2"><b-button size="lg" v-on:click="comparePictures">Compare images</b-button></b-col>
    <h2 v-bind:key="this.distance"> DISTANCE: {{this.distance.distance}} </h2>
    <b-form-group>
      <b-form-checkbox-group id="checkbox-group-2" v-model="selected" name="flavour-2">
        <b-list-group-item  v-for="(person, id) in this.$store.getters.PERSONS" v-bind:key="id" >
          {{ person['id'] }}
        <div class="line">
          <person-details :id="id" :uuid="person['id']"></person-details>
          <delete-person   :id="id" :uuid="person['id']"/>
          <b-form-checkbox  :value="person['id']"></b-form-checkbox>
        </div>
        </b-list-group-item>
      </b-form-checkbox-group>
    </b-form-group>
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
      errors: [],
      selected: [],
      distance: this.$store.getters.DISTANCE
    }
  },
  created () {
    this.$store.dispatch('GET_PERSONS')
  },
  methods: {
    comparePictures: function () {
      this.$store.dispatch('COMPARE_IMAGES', {id1: this.selected[0], id2: this.selected[1]})
      console.log(this.selected[0])
    }
  }
}
</script>

<style scoped>
  .pb-2 {
    align-self: center;
  }
  .line {
    display: flex;
    justify-content: center;
  }
</style>
