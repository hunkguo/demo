import Vue from 'vue';
import App from './App.vue';
import vuetify from './plugins/vuetify';
import VueRouter from 'vue-router';

Vue.config.productionTip = false



//安装插件
Vue.use(VueRouter); //挂载属性

//创建路由对象并配置路由规则
let router = new VueRouter({
    routes: [
        //一个个对象
        { path: '/home', component: Home }
    ]
});

//new Vue 启动
new Vue({
  vuetify,
  //让vue知道我们的路由规则
  router: router, //可以简写router
  render: h => h(App)
}).$mount('#app')
