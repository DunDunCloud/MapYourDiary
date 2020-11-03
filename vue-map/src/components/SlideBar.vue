<template>
    <sidebar-menu :menu="menu" />
</template>

<script>
// import { SlidebarMenu } from 'vue-sidebar-menu'

export default {
    components: {
        
    },
    data: () => ({
    menu: [
      {
        header: true,
        title: 'MENU',
        hiddenOnCollapse: true
      },
      {
        href: '/',
        title: 'Friends',
        icon: 'fa fa-user'
      },
      {
        href: '/',
        title: 'My Places',
        icon: 'fa fa-chart-area',
        child: [
          {
              href: '/',
              title: 'child'
          }
        ]
      }
    ]
  }),
}
</script>