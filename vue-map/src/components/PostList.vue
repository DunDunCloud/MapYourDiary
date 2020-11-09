<template>
<div>
    <h1>User Info</h1>
</div>
</template>

<script>
import axios from "axios";

export default {
    name: "PostList",
    methods: {
        getPost(){
            axios.get("http://127.0.0.1:8000/api/map", {auth: {
                username: "admin",
                password: "admin"
            }})
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error)
            });
        },
        postPost(){
            axios.post("http://127.0.0.1:8000/api/map", {auth: {
                username: "admin",
                password: "admin"
            }})
            .then(response => {
                console.log(response.data);
            })
            .catch(error => {
                console.log(error)
            });
        },
        deletePost(pageNum){
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
        }
    },
    created() {
        this.getPost();
    }
}
</script>