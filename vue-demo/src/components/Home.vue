<template>
  <v-container>

    <v-row justify="center">
      <v-col cols="12" sm="10" md="8" lg="6">
        <v-row justify="center">


          <v-card
            class="mx-auto"
          >
            <v-list>
              <v-list-item-group v-model="model">
                <v-list-item 
                  two-line
                  v-for="(v, i) in videolist"
                  :key="i"
                >
                  <v-list-item-content>
                    <v-list-item-title v-text="v.videoTitle" @click="playVideo(v.id)">
                    </v-list-item-title>
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
    name: 'Home',
    data() {
      return {
        info: null,
        videolist: null,
        error: undefined,
      }
    },
    methods:{
      getData(){
        this.$http.get('').then(response => {
          this.info = response.body;
          }, error => {
            console.log(error)
        });
        this.$http.get('videolist').then(response => {
          this.videolist = response.body;
          console.log(this.videolist)
          }, error => {
            console.log(error)
        });
      },
      playVideo(){
        this.$router.push({
          path: `/describe/${id}`,
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
