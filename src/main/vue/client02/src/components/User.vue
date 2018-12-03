<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Users</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.book-modal>Add User</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
            <th scope="col">Username</th>
              <th scope="col">Email</th>
              <th scope="col">Image</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{user.username}}</td>
              <td>{{user.email}}</td>
              <td>{{user.picture}}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm">Update</button>
                <button type="button" class="btn btn-danger btn-sm">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addUserModal"
             id="book-modal"
             title="Add a new User"
             hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group"
                    label="User:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addUserForm.username"
                        required
                        placeholder="Enter user">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group"
                      label="Email:"
                      label-for="form-author-input">
            <b-form-input id="form-author-input"
                          type="text"
                          v-model="addUserForm.email"
                          required
                          placeholder="Enter mail">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-title-group"
                    label="Image:"
                    label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addUserForm.picture"
                        required
                        placeholder="Enter image">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      users: [],
      addUserForm: {
        username: '',
        email: '',
        picture: '',
      },
    };
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:5000/user';
      axios.get(path)
        .then((res) => {
          this.users = res.data.user;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUser(info) {
      const path = 'http://localhost:5000/user';
      axios.post(path, info)
        .then(() => {
          this.getUsers();
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUsers();
        });
    },
    initForm() {
      this.addUserForm.username = '';
      this.addUserForm.email = '';
      this.addUserForm.picture = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();

      const info = {
        username: this.addUserForm.username,
        email: this.addUserForm.email,
        picture: this.addUserForm.picture
      };
      this.addUser(info);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
  },
  created() {
    this.getUsers();
  },
};
</script>
