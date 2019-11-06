<template>
    <div>
        <h1>이게 싱글파일 컴포넌트, 최상위 컴포턴트입니다.</h1>
        <TodoList category="취업"></TodoList>
        <TodoList category="수업"></TodoList>
        <TodoList category="게임"></TodoList>
    </div>
</template>

<script>
import TodoList from './components/TodoList.vue'
export default {
    components: {
        TodoList
    }
}
</script>

<style lang="">

</style>