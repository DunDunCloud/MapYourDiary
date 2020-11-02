<template>
  <v-app style="margin: 0px">
    <v-content>
      <HelloWorld/>
    </v-content>
    <ListView/>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>