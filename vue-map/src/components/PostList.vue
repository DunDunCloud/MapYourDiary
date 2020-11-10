<template>
<div>
    <h1>User Info</h1>
</div>
</template>

<script>
import axios from "axios";
import { eventBus } from "../main.js"

export default {
    name: "PostList",
    methods: {
        getPost: function (){
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
        postPost: function (){
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
            eventBus.$emit("click");
        },
        deletePost: function (pageNum){
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