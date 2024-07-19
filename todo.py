import reflex as rx



class TodoState(rx.State):
    tasks: list[dict] = []
    new_task: str = ""

    def add_task(self):
        if self.new_task:
            self.tasks.append({
                "description": self.new_task,
                "completed": False
            })
            self.new_task = ""

    def toggle_task(self, index: int):
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]

    def remove_task(self, index: int):
        self.tasks.pop(index)


def task_item(task: dict, index: int):
    return rx.hstack(
        rx.checkbox(
            is_checked=task["completed"],
            on_change=TodoState.toggle_task(index),
        ),
        rx.text(
            task["description"],
            text_decoration=rx.cond(task["completed"], "line-through", "none"),
        ),
        rx.button(
            "Remove",
            on_click=TodoState.remove_task(index),
            size="sm",
            color_scheme="red",
        ),
        width="100%",
        justify="space-between",
    )


def index():
    return rx.center(
        rx.input(
            placeholder="Add a new task",
                value=TodoState.new_task,
                on_change=TodoState.set_new_task
        ),
        rx.button(
            "Add Task",
            on_click=TodoState.add_task,
        ),
        rx.vstack(
            rx.foreach(
                TodoState.tasks,
                lambda task, index: task_item(task, index),
            ),
        ),
    ),



app = rx.App()
app.add_page(index)
