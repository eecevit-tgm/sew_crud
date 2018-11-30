<template>
	<div class="hello">
		  <tbody>
            <tr v-for="student in studens" :key="student">
              <td>{{ student.username }}</td>
            </tr>
		  </tbody>
	</div>
</template>  
  
<script>  
import axios from 'axios'
export default {
	name: 'HelloWorld',
	data () {
		return {
			students: none,
		}
	},
	methods:{ 
		getStudents() {
			const path = 'http://localhost:5000/user';
			axios.get(path).then((res) => {
				this.students = res.data;
			}).catch((error) => {
				console.error(error);
			});
    }
  },
	created(){
			this.getStudents()
	}
	
}
</script>