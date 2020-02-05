<template>
  <div>
    <b-form @submit="onSubmit" @reset="onReset">
      <b-form-group
        id="input-group-1"
        label="Surname:"
        label-for="input-1"
      >
        <b-form-input
          id="input-1"
          v-model="form.surname"
          required
          placeholder="Enter surname"
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-2" label="Your Name:" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.name"
          required
          placeholder="Enter name"
        ></b-form-input>
      </b-form-group>
      <b-button type="submit" variant="primary">Submit</b-button>
      <b-button type="reset" variant="danger">Reset</b-button>
    </b-form>
  </div>
</template>

<script>
// import {HTTP} from '../http-common'
export default {
  name: 'PersonCreate',
  data () {
    return {
      form: {
        surname: '',
        name: ''
      },
      errors: []
    }
  },
  methods: {
    onSubmit (evt) {
      this.$store.dispatch('CREATE_PERSON', {name: this.form.name, surname: this.form.surname})
    },
    onReset (evt) {
      evt.preventDefault()
      // Reset our form values
      this.form.surname = ''
      this.form.name = ''
    }
  }
}
</script>

<style scoped>

</style>
