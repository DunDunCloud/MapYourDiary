<template>
  <v-row>
    <v-col
      cols="12"
    >
      <v-card>
        <v-list>
<!--          <v-subheader inset>-->
<!--            Folders-->
<!--          </v-subheader>-->

          <v-list-item
            v-for="item in friends"
            :key="item.name"
            @click="test(item)"
          >
            <v-list-item-avatar>
              <img :src="item.avatar">
            </v-list-item-avatar>

            <v-list-item-content>
              <v-list-item-title>{{ item.name }}</v-list-item-title>

              <v-list-item-subtitle>{{ item.text }}</v-list-item-subtitle>
            </v-list-item-content>

            <v-list-item-action>
              <v-btn icon @click="set(item)">
                <v-icon>mdi-dots-vertical</v-icon>
              </v-btn>
            </v-list-item-action>
<!--              <v-btn icon>-->
<!--                <v-icon color="grey lighten-1">-->
<!--                  mdi-information-->
<!--                </v-icon>-->
<!--              </v-btn>-->
<!--            </v-list-item-action>-->
          </v-list-item>

        </v-list>
      </v-card>
    </v-col>
  </v-row>
</template>

<script>
  export default {
    data () {
      return {
        friends: [
          { avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', name: 'Photos', text: 'Jan 9, 2014' },
          { avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', name: 'Recipes', text: 'Jan 17, 2014' },
          { avatar: 'https://cdn.vuetifyjs.com/images/lists/1.jpg', name: 'Work', text: 'Jan 28, 2014' },
        ],
      }
    },
    methods: {
      test(item) {
        alert(item.name)
      },
      set(item) {
        console.log(item.name)
      }
    }
  }
</script>