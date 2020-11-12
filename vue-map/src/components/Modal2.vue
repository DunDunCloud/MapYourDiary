<template>
  <eModal v-model='modal' ref='modal' v-show="is_show"></eModal>
</template>

<script>
import {eModal} from 'vue-eagle-modal'

export default {
  components: {eModal},
  data(){
    return {
      is_show: false,
      modal:{
        title: 'Title',
        items: [
          {
            label: 'test',
            type:'text',
            name: 'e1',
            value: 'test'
          }
        ],
      },
    }
  }
}
</script>