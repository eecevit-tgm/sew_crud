<template>
  <div class="User">
  <thead>
    <th>username</th>
    <th>email</th>
    <th>image</th>
  </thead>
  <tbody>
    <tr v-for="(user, index) in Users" :key="index">
      <td>{{user.username}}</td>
      <td>{{user.email}}</td>
      <td>{{user.picture}}</td>
    </tr>
  </tbody>
    </div>
</template>

<script>
import axios from "axios";

export default {
  data(){
    return{
        Users: []
    };
  },

  methods:{
  getUsers () {
      axios.get("http://127.0.0.1:5000/user").then(res =>{
        this.Users = res.data
      })
  }
  },
  created() {
    this.getUsers()
  }
};
</script>


<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
