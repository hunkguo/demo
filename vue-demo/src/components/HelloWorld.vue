<template>
  <v-container>
    <v-row class="text-center">

      <v-col
        class="mb-5"
        cols="12"
      >
      
        <h2 class="headline font-weight-bold mb-3">
          Important Links
        </h2>

        
        <v-row justify="center">
        <span>{{ info }}</span>
        <span
            v-for="(user, i) in info"
            :key="i"
            :href="user.id"
          >
            {{ user.name }}
          </span>
          <a
            v-for="(link, i) in importantLinks"
            :key="i"
            :href="link.href"
            class="subheading mx-3"
            target="_blank"
          >
            {{ link.text }}
          </a>
        </v-row>
      </v-col>

    </v-row>
  </v-container>
</template>

<script>

  import Vue from 'vue'
  export default {
    name: 'HelloWorld',

    data() {
      return {
        info: [],

      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
    },

    mounted: {  
      Vue.axios.get('http://106.55.33.30:5000/api/').then((response) => {
        //console.log(response.data);
        this.info = response.data;
})
    },
  }
</script>
