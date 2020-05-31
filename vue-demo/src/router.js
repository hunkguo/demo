export default new Router({
    routes: [
        {
          
          path: '/',
          name: 'HelloWorld',
          component: HelloWorld,
          children: [{path: '/h1', name: 'H1', component: H1},//子路由的<router-view>必须在HelloWorld.vue中出现
            {path: '/h2', name: 'H2', component: H2}
          ]
        }
      ]
  })

