<script lang="ts">
	import { onMount } from 'svelte';
	import axios from 'axios';

	interface Todo {
		id: number;
		title: string;
		complete: boolean;
	}

	let error: string | null = null;
	let todos: Todo[] = [];
	let todoItem = '';

	const getTodos = async () => {
		try {
			const res = await axios.get('http://localhost:8000/todos');
			todos = res.data;
		} catch (e: unknown) {
			error = e as string;
		}
	};

	const addTodo = async () => {
		try {
			if (!todoItem) return alert('please add a goal for today!');
			const res = await axios.post('http://localhost:8000/todo', {
				title: todoItem
			});
			todos = [...todos, res?.data];
			todoItem = '';
		} catch (e: unknown) {
			error = e as string;
		}
	};

	const toggleComplete = async (todo) => {
		const todoIndex = todos.indexOf(todo);
		try {
			const { data } = await axios.put(`http://localhost:8000/todo/${todo.id}`);
			todos[todoIndex].complete = data.complete;
		} catch (e: unknown) {
			error = e as string;
		}
	};

	const deleteTodo = async (todo) => {
		try {
			await axios.delete(`http://localhost:8000/todo/${todo.id}`);
			todos = todos.filter((to) => to.id !== todo.id);
		} catch (e: unknown) {
			error = e as string;
		}
	};

	onMount(() => {
		getTodos();
	});
</script>

<body class="container max-w-xl mx-auto">
	<h1 class="font-bold text-2xl my-16">Yet another TODO app! 😛</h1>

	<div class="grid grid-cols-7 gap-2">
		<input class="col-span-5 input input-bordered" type="text" name="todo" bind:value={todoItem} />
		<button class="btn btn-accent col-span-2" on:click={addTodo}> Create Todo </button>
	</div>
	{#if error}
		<p class="text-xl mb-2 text-red-600">{error}</p>
	{/if}
	{#each todos as todo}
		<div id="todos" class="my-8 w-full">
			<div class="grid grid-cols-7 gap-2 mt-4">
				<p class="col-span-5" class:line-through={todo.complete}>
					{todo.title}
				</p>
				<button class="btn btn-success hover:bg-green-300" on:click={toggleComplete(todo)}>
					&#10003;
				</button>
				<button class="btn btn-error hover:bg-red-300" on:click={deleteTodo(todo)}>
					&#x2717;
				</button>
			</div>
		</div>
	{:else}
		<p>No goals for today!</p>
	{/each}
</body>
