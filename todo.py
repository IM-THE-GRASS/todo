import reflex as rx
from reflex_motion import motion
theme = rx.theme(
    appearance="dark",
    has_background=True,
    radius="large",
    accent_color="teal",
)


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



def boingybutton(text, on_click = None,**kwargs):
    return motion(
        rx.button(
            text,
            on_click=on_click,
            **kwargs,
        ),
        while_hover={"scale": 1.1},
        while_tap={"scale": 0.95},
        transition={"type": "spring", "stiffness": 400, "damping": 17},
    )
    

def task_item(task: dict, index: int):
    return rx.hstack(
        motion(
            rx.checkbox(
                is_checked=task["completed"],
                on_change=TodoState.toggle_task(index),
            ),
            while_hover={"scale": 1.1},
            while_tap={"scale": 0.95},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        motion(
            rx.text(
                task["description"],
                text_decoration=rx.cond(task["completed"], "line-through", "none"),
            ),
            while_hover={"scale": 1.1},
            while_tap={"scale": 0.95},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        
        boingybutton(
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
        rx.container(
            rx.vstack(
                rx.heading("Todo App", font_size="2.5em", color = "#ADF0DD"),
                motion(
                    rx.input(
                        placeholder="Add a new task",
                        value=TodoState.new_task,
                        on_change=TodoState.set_new_task,
                        width="100%"
                    ),
                    while_hover={"scale": 1.1},
                    while_tap={"scale": 0.95},
                    transition={"type": "spring", "stiffness": 400, "damping": 17},
                ),
                
                boingybutton(
                    "Add Task",
                    on_click=TodoState.add_task,
                    width="100%"
                ),
                rx.divider(margin_y="1.2em"),
                rx.vstack(
                    rx.foreach(
                        TodoState.tasks,
                        lambda task, index: task_item(task, index),
                    ),
                    width="100%",
                    spacing="0.7em",
                ),
            ),
            width="100%",
            max_width="550px",
            padding="2.5em",
            background_color="#0D2D2A",
            border = "4px solid #207E73"
        ),
        height="100vh",
        background="#0D1514",
    )


app = rx.App(theme=theme)
app.add_page(index)
