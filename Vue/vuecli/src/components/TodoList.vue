<template>
    <div class="todo-list">
        <h2>{{category}}</h2>
        <input v-model="newTodo" type="text">
        <button v-on:click="addTodo">할일 추가</button>
        {{todos}}
        <!-- 할일 목록 나열 -->
        <li v-for="todo in todos" :key="todo.id">{{todo.content}} <button v-on:click="removeTodo(todo.id)">일 삭제</button>
        </li>
      </div>
</template>

<script>
export default {
    props: {
        category: {
          type: String,
          required: true
        },
      },// 하위컴퍼넌트로 데이터 전송
      data: function () {
        return {
          todos: [],
          newTodo: ''
        }
      },
      methods: {
        addTodo() {
          this.todos.push({
            id: Date.now(),
            content: this.newTodo
          })
          this.newTodo = ''
        },
        removeTodo(id) {
          this.todos = this.todos.filter(todo => {
            return !(todo.id === id)
          })
        },
      },
    
}
</script>

<style lang="">
/* li {
    color: blue;
} */
</style>