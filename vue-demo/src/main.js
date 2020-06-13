import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import VideoList from './components/VideoList.vue'
import AddVideo from './components/AddVideo.vue'
import Player from './components/Player.vue'
import vuetify from './plugins/vuetify';

import VueResource from 'vue-resource';


Vue.config.productionTip = false
Vue.use(VueResource);

//安装插件
Vue.use(VueRouter); //挂载属性

//创建路由对象并配置路由规则
let router = new VueRouter({
    mode: 'history',
    base:"/demo",
    routes: [
        //一个个对象
        { name: 'VideoList', path: '/', component: VideoList },
        { name: 'AddVideo', path: '/AddVideo', component: AddVideo },
        { name: 'Player', path: '/Player/:id', component: Player },
    ]
});
Vue.http.options.root = 'http://10.8.0.6:5000/api/';

new Vue({
    //让vue知道我们的路由规则
    //可以简写router
    router: router,

    vuetify,
    render: h => h(App)
}).$mount('#app')
