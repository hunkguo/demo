<template>
  <v-container>
    <v-row dense>
      <v-col cols="12">
        <v-card
          dark
          ref="form"
          >
          <v-card-title>视频链接</v-card-title>
                <v-divider class="mx-4"></v-divider>
                <v-card-subtitle>
                  <v-text-field
                    ref="videoLink"
                    v-model="videoLink"
                    :rules="[() => !!videoLink || 'This field is required']"
                    :error-messages="errorMessages"
                    placeholder="地址"
                    required
                    autofocus='true'
                  ></v-text-field>
                </v-card-subtitle>
          <v-card-text>
            <v-card-actions>
              <v-btn  small   @click="resetForm">清除</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary"  small  @click="submit">保存</v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

  export default {
    name: 'AddVideo',
    data() {
      return {
        videoLink: null,
        errorMessages: '',
        formHasErrors: false,

        info: null,
        videolist: null,
        error: undefined,
      }
    },
    computed: {
      form () {
        return {
          videoLink: this.videoLink,
        }
      },
    },
    watch: {
      name () {
        this.errorMessages = ''
      },
    },
    methods:{
      resetForm () {
        this.errorMessages = []
        this.formHasErrors = false
        Object.keys(this.form).forEach(f => {
          this.$refs[f].reset()
        })
      },
      submit () {
        this.formHasErrors = false
        Object.keys(this.form).forEach(f => {
          if (!this.form[f]) this.formHasErrors = true
          this.$refs[f].validate(true)
        })

        //this.$http.post('http://10.8.0.6:5000/api/savevideolist',{link:this.videoLink}).then(response => {
        this.$http.post('/api/savevideolist',{link:this.videoLink}).then(response => {
          this.videolist = response.body;
          this.resetForm()
          }, error => {
            console.log(error)
        });
        
      },
    },
  }
    
</script>

<style>
  #input-usage .v-input__prepend-outer,
  #input-usage .v-input__append-outer,
  #input-usage .v-input__slot,
  #input-usage .v-messages {
    border: 1px dashed rgba(0,0,0, .4);
  }
</style>
