from tkinter import *
from tkinter import messagebox

from planner import Action, PlanningGraph
from graph_visualizer import visualize_plan


root = Tk()
root.title("Planning Graph Action Sequence Generator")
root.geometry("700x600")
root.configure(bg="#f0f0f0")


Label(
    root,
    text="Planning Graph Based Action Sequence Generator",
    font=("Arial", 18, "bold"),
    bg="#f0f0f0",
    fg="darkblue"
).pack(pady=20)


Label(root, text="Initial State (comma separated)", bg="#f0f0f0").pack()
initial_entry = Entry(root, width=70)
initial_entry.pack(pady=5)


Label(root, text="Goal State (comma separated)", bg="#f0f0f0").pack()
goal_entry = Entry(root, width=70)
goal_entry.pack(pady=5)


result_box = Text(root, height=15, width=70)
result_box.pack(pady=20)


# Sample Actions
sample_actions = [
    Action(
        "Move_A_to_B",
        ["At_A"],
        ["At_B"]
    ),

    Action(
        "Pick_Object",
        ["At_B"],
        ["Has_Object"]
    ),

    Action(
        "Move_B_to_C",
        ["At_B"],
        ["At_C"]
    ),

    Action(
        "Deliver_Object",
        ["At_C", "Has_Object"],
        ["Goal_Achieved"]
    )
]


current_plan = []


def generate_plan():
    global current_plan

    initial_state = initial_entry.get().split(',')
    goal_state = goal_entry.get().split(',')

    initial_state = [x.strip() for x in initial_state]
    goal_state = [x.strip() for x in goal_state]

    planner = PlanningGraph(
        initial_state,
        goal_state,
        sample_actions
    )

    plan = planner.generate_plan()

    result_box.delete(1.0, END)

    if plan:
        current_plan = plan

        result_box.insert(
            END,
            "Generated Action Sequence:\n\n"
        )

        for step, action in enumerate(plan, start=1):
            result_box.insert(
                END,
                f"Step {step}: {action}\n"
            )

    else:
        messagebox.showerror(
            "Error",
            "No valid plan found"
        )



def show_graph():
    if current_plan:
        visualize_plan(current_plan)
    else:
        messagebox.showwarning(
            "Warning",
            "Generate a plan first"
        )


Button(
    root,
    text="Generate Plan",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=generate_plan
).pack(pady=10)


Button(
    root,
    text="Visualize Graph",
    font=("Arial", 12, "bold"),
    bg="blue",
    fg="white",
    command=show_graph
).pack(pady=10)


root.mainloop()