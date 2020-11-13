<script>
import axios from "axios";

export default {
    name: "PostList",

    data() {
        return {
            posts: []
        }
    },

    methods: {
        getPost: async function (){
            await axios.get("http://127.0.0.1:8000/api/map", {auth: {
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