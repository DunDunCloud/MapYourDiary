<template>
  <v-app style="margin: 0px">
    <v-content>
      <v-container id="container">
        <HelloWorld/>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
// import ListView from './components/ListView';

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