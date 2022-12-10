<template>
    <main>
        <!-- <section class="tododone"></section> -->
    <section class="todolist" v-show="show">
        <h1>Tarefas: </h1>
        <div v-for="(todo, index) in todos" :key="index" v-show="!todo.done" class="list-group-item-check" @click="done(index)">
        <label class="list-group-item rounded-3 py-3">
          {{todo.name}}
        </label>
        </div>
    </section>
        <section class="tododone" v-show="!show">
            <h1>Tarefas Feitas:</h1>
            <div v-for="(todo, index) in todos" :key="index" v-show="todo.done" class="list-group-item-check" @click="done(index)">
            <label class="list-group-item rounded-3 py-3">
              {{todo.name}}
            </label>
            </div>
        </section>
        <div @click="showDone()">click heare to see the done todos</div>
    </main>
    
</template>

<script>
import api from '@/services/api.js'

export default {
    name: 'UserComponents',
    data () {
        return {
            todos: [],
            show: false 
        }
    },
    methods: {
        done(index) {
            this.todos[index].done = true
            console.log('click')
        },
        makeReq() {
            const token = localStorage.getItem('access_token')
            if (!token) {
                this.$router.push('/login')
            } else {
                const config = {
                    headers: {
                        "Authorization": `Bearer ${token}` 
                    },
                }
            api.get('/user/me', config).then(res => {
                this.todos = res.data.todos
        })

            }

        },
        showDone() {
            this.show ? this.show = false : this.show = true
        }
    },
    created () {
        this.makeReq()
    },
}
</script>

<style scoped>

main{
    flex-direction: column;
    justify-content: space-around;
}
label {
    margin-bottom: 5px;
    background-color: antiquewhite;
    box-shadow: 3px 3px 10px black;
}

label:hover {
    background-color: #0d6efd;
    color: whitesmoke;
    cursor: pointer;
}

/* .tododone {
    background-color: rgba(0, 0, 0);
    width: 100%;
    height: 100%;
    position: absolute;
} */
</style>