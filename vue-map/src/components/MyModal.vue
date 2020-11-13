<template>
  <v-row justify="center">
    <v-dialog
      v-model="dialog"
      persistent
      max-width="600px"
    >
      <v-card>
        <v-card-title>
          <span class="headline">Place Diary</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-text-field
                  id="diary_title" 
                  label="글 제목*"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="testdata"
                  id="diary_description" 
                  label="내용*"
                  required
                ></v-text-field>
              </v-col>
            </v-row>
          </v-container>
<!--          <small>*indicates required field</small>-->
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="blue darken-1"
            text
            @click="dialog = false"
          >
            취소
          </v-btn>
          <v-btn
            color="blue darken-1"
            text
            @click="saveDiary"
          >
            저장
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
</template>

<script>
import axios from "axios";

export default {
  // props: {
  //    show: {
  //      type: Boolean,
  //      required: true,
  //      twoWay: true
  //    }
  // },
  data: function(){
    return {
      dialog: false,
      testdata: ''
    }
  },
  created() {
    this.$EventBus.$on('open-modal', () => {
      this.dialog = true;
    });
  },
  methods: {
    async saveDiary() {
      this.dialog = false
      const title = document.getElementById('diary_title').value;
      const description = document.getElementById('diary_description').value;
      
      console.log(title, description)

      await axios.post("http://127.0.0.1:8000/api/map",{
        title: title,
        description: description
      },{
        auth:{
          username: "admin",
          password: "admin"
        }
      })
      .then(response => {
          console.log(response.data);
          this.$EventBus.$emit('get-post');
      })
      .catch(error => {
          console.log(error)
      });
      
    },
  }
}
</script>