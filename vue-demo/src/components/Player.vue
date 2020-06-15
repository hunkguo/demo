<template>

  <v-container>
    <v-row dense>
      <v-col cols="12">
        <v-card
          dark
          ref="form"
          >
          <v-card-title v-text="video.videoTitle"></v-card-title>
            <v-divider class="mx-4"></v-divider>
            <v-card-subtitle>
              <audio autoplay="autoplay" 
                    controls="controls"
                    preload="auto"
                    v-bind:src="'/api/static/media/' + video.videoFile"
                    >
              </audio>
            </v-card-subtitle>
          <v-card-text>
            <v-card-actions>
              <v-btn text color="primary" @click="1">后退</v-btn>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="1">快进</v-btn>
            </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>

  export default {
    name: 'Player',
    data() {
      return {
        video: null,
        error: undefined,
      }
    },
    methods:{
      getData(){
        this.$http.get('http://192.168.30.55:5000/api/getvideo/'+this.$route.params.id).then(response => {
        //this.$http.get('/api/getvideo/'+this.$route.params.id).then(response => {
            this.video = response.body;
          }, error => {
            console.log(error)
        })
      },
    },

    mounted () {
      this.getData()
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
