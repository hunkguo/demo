import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router';
import Home from './components/Home.vue'
import Dashboard from './components/Dashboard.vue'
import Settings from './components/Settings.vue'
import HelloWorld from './components/HelloWorld.vue'
import vuetify from './plugins/vuetify';

import VueResource from 'vue-resource';


Vue.config.productionTip = false
Vue.use(VueResource);

//安装插件
Vue.use(VueRouter); //挂载属性

//创建路由对象并配置路由规则
let router = new VueRouter({
    routes: [
        //一个个对象
        { name: 'Home', path: '/Home', component: Home },
        { name: 'HelloWorld', path: '/', component: HelloWorld },
        { name: 'Dashboard', path: '/Dashboard', component: Dashboard },
        { name: 'Settings', path: '/Settings', component: Settings }
    ]
});

Vue.http.options.root = 'http://106.55.33.30:5000/api/';

new Vue({
    //让vue知道我们的路由规则
    //可以简写router
    router: router,

    vuetify,
    render: h => h(App)
}).$mount('#app')
