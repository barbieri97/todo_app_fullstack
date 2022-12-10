<template>
    <main>
        <section class="listndone">
            <h1>Tarefas: </h1>
            <div v-for="(todo, index) in todos" :key="index" v-show="!todo.done" class="list-group-item-check" @click="done(index)">
                <label class="list-group-item rounded-3 py-3" for="listGroupCheckableRadios1">
                    {{todo.name}}
                </label>
            </div>
        </section>
    </main>
</template>


<script>
import api from '@/services/api.js'

export default {
    name: 'UserComponents',
    props: {
        todos: []
    },
    methods: {
            done(index) {
                this.todos[index].done = true
            },
            created () {
                this.makeReq()
            }
        }
    }
</script>

<style scoped>
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
</style>