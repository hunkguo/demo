<template>
  <v-container>
    <v-row dense>
      <v-col cols="12"
          v-model="model" 
          v-for="(v, i) in videolist"
          :key="i">
        <v-card
          dark
          @click="playVideo(v.id)"
          >
          <v-card-title v-text="v.videoTitle"></v-card-title>
                <v-divider class="mx-4"></v-divider>
                <v-card-subtitle>{{v.videoUploader}} - {{v.videoUploadDate}} - 时长{{v.videoDuration}}秒</v-card-subtitle>
          <v-card-text>
                <v-card-actions>
                  <v-btn small disabled>点赞</v-btn>
                  <v-btn small disabled>删除</v-btn>
                </v-card-actions>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>

  export default {
    name: 'VideoList',
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
        this.$http.get('http://192.168.30.55/api/videolist').then(response => {
        //this.$http.get('/api/videolist').then(response => {
          this.videolist = response.body;
          //console.log(this.videolist)
          }, error => {
            console.log(error)
        });
      },
      playVideo(id){
        //console.log(id)
        this.$router.push({
          path: `/Player/`+id,
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
