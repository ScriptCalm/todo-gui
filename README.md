# To-Do GUI App (Python + Tkinter + SQLite)

A lightweight, installable desktop task manager built with Python.  
Includes a graphical user interface (GUI), persistent storage using SQLite, and clean modular code.

---

## Features

- Add, view, and delete tasks from a user-friendly window
- Tasks are **saved locally** in a database (`tasks.db`)
- Fully offline, no dependencies or internet required
- Clean interface built with `tkinter`
- Data persistence with `sqlite3`

---

## Antivirus & Windows Defender Warnings

This app is not code-signed yet, so you may receive warnings from:

- Microsoft Defender SmartScreen

- Antivirus software like AVG or Avast

If you trust the app (you can inspect the source code in this repo), you can:

- Click "More info" -> "Run anyway" (SmartScreen).

- Add the installer or .exe to your antivirus exceptions if it's blocked.

- Run the installer as Administrator.

## Packaging & Deployment

The To-Do App was packaged into a standalone Windows installer using [Inno Setup](https://jrsoftware.org/isinfo.php).

- The installer creates Start Menu and Desktop shortcuts.
- Installation requires Administrator privileges.
- No internet connection is required after download.
- To avoid false positives, add an exception in your antivirus for the installer.

> ⚠️ Note: Since the installer is unsigned, Windows Defender and some antivirus software may flag it. This is expected behavior for unsigned personal projects.


## **Download the App**

You can download the latest `.exe` version for Windows here:

https://github.com/ScriptCalm/todo-gui/releases/tag/v1.0.0

No Python installation required — just unzip and run `main.exe`.

