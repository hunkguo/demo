<template>
  <v-container>
    
    <v-row justify="center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-row justify="center">
          <v-card
            class="mx-auto"
            max-width="300"
          >

            <v-list>
              <v-list-item-group >
                <v-list-item 
                  two-line
                  
                >
                  <v-list-item-content>
                    <v-list-item-title class="wrap-text" v-text="video.videoTitle">
                    </v-list-item-title>
                    <v-list-item-subtitle>
                      <audio autoplay="autoplay" 
                            controls="controls"
                            preload="auto"
                            v-bind:src="'/static/media/' + video.videoFile"
                            >
                      </audio>
                    </v-list-item-subtitle>

                  </v-list-item-content>
                </v-list-item>
              </v-list-item-group>
            </v-list>

          </v-card>
        </v-row>
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
        //this.$http.get('http://106.55.33.30:5000/api/getvideo/'+this.$route.params.id).then(response => {
        this.$http.get('/api/getvideo/'+this.$route.params.id).then(response => {
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
