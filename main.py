import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import matplotlib.pyplot as plt

data = {}

def next_step(step):
    for widget in root.winfo_children():
        widget.destroy()

    if step == 1:
        ttk.Label(root, text="🏏 Enter Player Names", font=("Arial", 18, "bold")).pack(pady=10)

        entries = {}
        for key, text in [("p1","Player 1 (Team A)"),("p2","Player 2 (Team A)"),
                          ("p3","Player 3 (Team B)"),("p4","Player 4 (Team B)")]:
            ttk.Label(root, text=text, font=("Arial", 12)).pack()
            e = ttk.Entry(root, width=25, bootstyle=INFO); e.pack(pady=5)
            entries[key] = e

        def save():
            for k,v in entries.items():
                data[k] = v.get()
            next_step(2)

        ttk.Button(root, text="Next ➡", bootstyle=SUCCESS, command=save).pack(pady=20)

    elif step == 2:
        ttk.Label(root, text="⚡ Team A Innings (12 Balls)", font=("Arial", 18, "bold")).pack(pady=10)
        entries = []
        for i in range(1,13):
            ttk.Label(root, text=f"Ball {i}", font=("Arial", 12)).pack()
            ent = ttk.Entry(root, width=10, bootstyle=PRIMARY); ent.pack(pady=3)
            entries.append(ent)

        def save():
            for i in range(12):
                data[f"i1ball{i+1}"] = int(entries[i].get())
            next_step(3)

        ttk.Button(root, text="Next ➡", bootstyle=SUCCESS, command=save).pack(pady=20)

    elif step == 3:
        ttk.Label(root, text="🏏 Team A Batting & Extras", font=("Arial", 18, "bold")).pack(pady=10)

        tkvars = {}
        for key, text in [("ar","Runs by Player 1"),("br","Runs by Player 2"),("ex","Extras (by Team B)")]:
            ttk.Label(root, text=text, font=("Arial", 12)).pack()
            e = ttk.Entry(root, width=20, bootstyle=INFO); e.pack(pady=5)
            tkvars[key] = e

        def save():
            for k,v in tkvars.items():
                data[k] = int(v.get())
            next_step(4)

        ttk.Button(root, text="Next ➡", bootstyle=SUCCESS, command=save).pack(pady=20)

    elif step == 4:
        ttk.Label(root, text="🎯 Team B Bowling", font=("Arial", 18, "bold")).pack(pady=10)

        tkvars = {}
        for key, text in [("db","Runs conceded by P3"),("eb","Runs conceded by P4")]:
            ttk.Label(root, text=text, font=("Arial", 12)).pack()
            e = ttk.Entry(root, width=20, bootstyle=WARNING); e.pack(pady=5)
            tkvars[key] = e

        def save():
            for k,v in tkvars.items():
                data[k] = int(v.get())
            next_step(5)

        ttk.Button(root, text="Next ➡", bootstyle=SUCCESS, command=save).pack(pady=20)

    elif step == 5:
        ttk.Label(root, text="⚡ Team B Innings (12 Balls)", font=("Arial", 18, "bold")).pack(pady=10)
        entries = []
        for i in range(1,13):
            ttk.Label(root, text=f"Ball {i}", font=("Arial", 12)).pack()
            ent = ttk.Entry(root, width=10, bootstyle=DANGER); ent.pack(pady=3)
            entries.append(ent)

        def save():
            for i in range(12):
                data[f"i2ball{i+1}"] = int(entries[i].get())
            next_step(6)

        ttk.Button(root, text="Next ➡", bootstyle=SUCCESS, command=save).pack(pady=20)

    elif step == 6:
        ttk.Label(root, text="🏏 Team B Batting & Extras", font=("Arial", 18, "bold")).pack(pady=10)

        tkvars = {}
        for key, text in [("dr","Runs by Player 3"),("er","Runs by Player 4"),("ey","Extras (by Team A)")]:
            ttk.Label(root, text=text, font=("Arial", 12)).pack()
            e = ttk.Entry(root, width=20, bootstyle=INFO); e.pack(pady=5)
            tkvars[key] = e

        def save():
            for k,v in tkvars.items():
                data[k] = int(v.get())
            next_step(7)

        ttk.Button(root, text="Next ➡", bootstyle=SUCCESS, command=save).pack(pady=20)

    elif step == 7:
        ttk.Label(root, text="🎯 Team A Bowling (2nd Innings)", font=("Arial", 18, "bold")).pack(pady=10)

        tkvars = {}
        for key, text in [("ab","Runs conceded by P1"),("bb","Runs conceded by P2")]:
            ttk.Label(root, text=text, font=("Arial", 12)).pack()
            e = ttk.Entry(root, width=20, bootstyle=WARNING); e.pack(pady=5)
            tkvars[key] = e

        def save():
            for k,v in tkvars.items():
                data[k] = int(v.get())
            finish()

        ttk.Button(root, text="🏆 Finish & Show Result", bootstyle=SUCCESS, command=save).pack(pady=20)


def finish():
    # Calculate scores
    i1ov1 = sum([data[f"i1ball{i}"] for i in range(1,7)])
    i1ov2 = sum([data[f"i1ball{i}"] for i in range(7,13)])
    x = i1ov1 + i1ov2

    i2ov1 = sum([data[f"i2ball{i}"] for i in range(1,7)])
    i2ov2 = sum([data[f"i2ball{i}"] for i in range(7,13)])
    y = i2ov1 + i2ov2

    overs = ['TEAM 1 OVER 1', 'TEAM 2 OVER 1', 'TEAM 1 OVER 2', 'TEAM 2 OVER 2']
    runs = [i1ov1, i2ov1, i1ov2, i2ov2]

    if x > y:
        result = f"🏆 TEAM A WON THE MATCH BY {x-y} RUNS"
        show_scoreboard(result, overs, runs)
    elif y > x:
        result = f"🏆 TEAM B WON THE MATCH BY {y-x} RUNS"
        show_scoreboard(result, overs, runs)
    else:
        decider_ball(overs, runs)


def decider_ball(overs, runs):
    for widget in root.winfo_children():
        widget.destroy()

    ttk.Label(root, text="⚡ DECIDER BALL (TIE-BREAKER)", font=("Arial", 18, "bold")).pack(pady=15)

    ttk.Label(root, text="Runs scored by Team A (Decider Ball):", font=("Arial", 12)).pack()
    e1 = ttk.Entry(root, width=15, bootstyle=SUCCESS); e1.pack(pady=5)

    ttk.Label(root, text="Runs scored by Team B (Decider Ball):", font=("Arial", 12)).pack()
    e2 = ttk.Entry(root, width=15, bootstyle=SUCCESS); e2.pack(pady=5)

    def save():
        dcb1, dcb2 = int(e1.get()), int(e2.get())
        if dcb1 > dcb2:
            result = "🏆 TEAM A WON THE MATCH (Decider Ball)"
        elif dcb2 > dcb1:
            result = "🏆 TEAM B WON THE MATCH (Decider Ball)"
        else:
            result = "🤝 IT WAS A WELL FOUGHT TIE (EVEN DECIDER BALL!)"
        show_scoreboard(result, overs, runs)

    ttk.Button(root, text="Show Final Result", bootstyle=SUCCESS, command=save).pack(pady=20)


def show_scoreboard(result, overs, runs):
    scoreboard = f"""
    🏏 SCORECARD
    ---------------------
    TEAM A
    Batting:
    {data['p1']} - {data['ar']} runs
    {data['p2']} - {data['br']} runs

    Bowling:
    {data['p1']} - {data['ab']} conceded
    {data['p2']} - {data['bb']} conceded

    TEAM B
    Batting:
    {data['p3']} - {data['dr']} runs
    {data['p4']} - {data['er']} runs

    Bowling:
    {data['p3']} - {data['db']} conceded
    {data['p4']} - {data['eb']} conceded

    RESULT:
    {result}
    """

    messagebox.showinfo("🏏 Match Result", scoreboard)

    plt.bar(overs, runs, color=["green","red","green","red"])
    plt.title("MATCH STATS")
    plt.xlabel("Overs")
    plt.ylabel("Runs")
    plt.show()


# Run app
root = ttk.Window(themename="darkly")  # modern dark theme
root.title("Cricket Scoreboard 🏏")
root.geometry("500x600")
next_step(1)
root.mainloop()
