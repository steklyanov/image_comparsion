<template>
  <div class="container">
    <div class="large-12 medium-12 small-12 cell">
      <label>File
        <input type="file" id="file" ref="file" v-on:change="handleFileUpload()"/>
      </label>
      <button v-on:click="submitFile()">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'UploadImage',
  props: ['uuid', 'id'],
  data () {
    return {
      file: null
    }
  },
  methods: {
    submitFile: function (file) {
      let formData = new FormData()
      formData.append('file', this.file)
      console.log(this.file)
      this.$store.dispatch('UPLOAD_IMAGE', {image: formData, id: this.uuid})
    },
    handleFileUpload: function () {
      this.file = this.$refs.file.files[0]
    }
  }
}
</script>

<style scoped>

</style>
