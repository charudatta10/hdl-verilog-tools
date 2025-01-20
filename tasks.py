from invoke import task, Collection, Context


@task
def commit(ctx, message="init"):
    ctx.run("git add .")
    ctx.run(f"git commit -m \"{message}\"")

@task
def quit(ctx):
    print("Copyright © 2024 Charudatta")

@task
def test(ctx):
    ctx.run("python -m unittest discover -s tests")

@task
def run(ctx, file_name):
    ctx.run(f"iverilog -o build/{{file_name}}.vvp src/{{file_name}}.v tests/test_{{file_name}}.v")
    ctx.run(f"vvp build/{{file_name}}.vvp")
    ctx.run(f"gtkwave build/{{file_name}}.vcd")

@task(default=True)
def default(ctx):
    # Get a list of tasks
    tasks = sorted(ns.tasks.keys())
    # Display tasks and prompt user
    for i, task_name in enumerate(tasks, 1):
        print(f"{i}: {task_name}")
    choice = int(input("Enter the number of your choice: "))
    ctx.run(f"invoke {tasks[choice - 1]}")

# Create a collection of tasks
ns = Collection( commit, quit, test, run, default)
