<template>
<div>
    <!-- <PlaceList :posts="this.posts"></PlaceList> -->
    <p v-for="(post, index) in posts" :key="index">
        {{ post.id }} <br>
        {{ post.title }} <br>
        {{ post.description  }} <br><br>
    </p>
</div>
</template>

<script>
import axios from "axios";
// import PlaceList from "@/views/PlaceList";

export default {
    name: "PostList",

    data() {
        return {
            posts: []
        }
    },
    // components: {
    //     PlaceList
    // }, 

    methods: {
        getPost: function (){
            axios.get("http://127.0.0.1:8000/api/map", {auth: {
                username: "admin",
                password: "admin",
                
            }})
            .then(response => {
                console.log(response.data);
                // this.posts = JSON.stringify(response.data);
                this.posts = response.data;
                console.log(this.posts)
                // JSON.parse(JSON.stringify(this.posts))
                this.$EventBus.$emit("post-list", JSON.parse(JSON.stringify(this.posts)))
            })
            .catch(error => {
                console.log(error)
            })
            .finally(() => {
                
            })
        }
    },
    created() {
        this.getPost();
        this.$EventBus.$on('post-post', () => {
            const title = document.getElementById('title').value;
            const description = document.getElementById('description').value;
            
            axios.post("http://127.0.0.1:8000/api/map",
            {auth: {
                username: "admin",
                password: "admin"
            },
            params: {
                title: title,
                description: description
            }})
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error)
            });
        });
        
        this.$EventBus.$on('delete-post', (pageNum) => {
            axios.delete("http://127.0.0.1:8000/api/map"+pageNum, {auth: {
                username: "admin",
                password: "admin"
            }})
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error)
            });
        });
    }
}
</script>