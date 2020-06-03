<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-row justify="center">
          <v-card ref="form">
            <v-card-text>
              <h2 class="headline font-weight-bold ">
                请输入喜欢的视频地址
              </h2>
              <v-text-field
                ref="videoLink"
                v-model="videoLink"
                :rules="[() => !!videoLink || 'This field is required']"
                :error-messages="errorMessages"
                label="链接"
                placeholder="支持youtube地址"
                required
                autofocus='true'
              ></v-text-field>

            </v-card-text>
            <v-divider class="mt-12"></v-divider>
            <v-card-actions>
              <v-btn text  @click="resetForm">清除</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="submit">保存</v-btn>
            </v-card-actions>
          </v-card>
        </v-row>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>

  export default {
    name: 'HelloWorld',
    data() {
      return {
        videoLink: null,
        errorMessages: '',
        formHasErrors: false,

        info: [],
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
    mounted () {
        this.$http.get('').then(response => {
        this.info = response.body;
        }, error => {
          console.log(error)
      });
    },
    methods:{
      resetForm () {
        console.log('重置...')
        this.errorMessages = []
        this.formHasErrors = false
        console.log(this.name)
        Object.keys(this.form).forEach(f => {
          this.$refs[f].reset()
        })
      },
      submit () {
        this.formHasErrors = false
        console.log('提交...')
        Object.keys(this.form).forEach(f => {
          if (!this.form[f]) this.formHasErrors = true
          this.$refs[f].validate(true)
        })
      },
    }
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
