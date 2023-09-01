import tkinter as tk
from tic_tac_toe import AIagent_move, Win_Result, Draw_scenario

class TTT_GUI:
    def __init__(_SELF_):
        _SELF_.window = tk.Tk()
        _SELF_.window.title("Tic Tac Toe")
        _SELF_.board = [[' ' for _ in range(3)] for _ in range(3)]
        _SELF_.buttons = [[None for _ in range(3)] for _ in range(3)]
        _SELF_.Frame_ui()
        _SELF_.window.mainloop()

    def Frame_ui(_SELF_):
      
        board_frame = tk.Frame(_SELF_.window)
        board_frame.pack()

        
        for row in range(3):
            for col in range(3):
                _SELF_.buttons[row][col] =  tk.Button(board_frame, text=' ', font=('Helvetica', 40), width=7, height=2, command=lambda row=row, col=col: _SELF_.Humans_Play(row, col), fg='white', bg='black')
                _SELF_.buttons[row][col].grid(row=row, column=col)

    
        control_frame = tk.Frame(_SELF_.window)
        control_frame.pack()

     
        restart_button = tk.Button(control_frame, text='RESTART', command=_SELF_.restart)
        restart_button.pack(side=tk.LEFT)

        exit_button = tk.Button(control_frame, text='EXIT', command=_SELF_.window.destroy)
        exit_button.pack(side=tk.RIGHT)

    def Humans_Play(_SELF_, row, col):
        if _SELF_.board[row][col] == ' ':
            _SELF_.board[row][col] = 'X'
            _SELF_.buttons[row][col].config(text='X', state='disabled')
            if Win_Result(_SELF_.board,'X'):
                _SELF_.Declare_result("YOU WON the Game, Congratulations")
                return
            if Draw_scenario(_SELF_.board):
                _SELF_.Declare_result("The Game is DRAW!!, Try harder")
                return
            _SELF_.AIs_Play()

    def AIs_Play(_SELF_):
        row, col = AIagent_move(_SELF_.board)
        _SELF_.board[row][col] = 'O'
        _SELF_.buttons[row][col].config(text='O', state='disabled')
        if Win_Result(_SELF_.board,'O'):
            _SELF_.Declare_result("AI WON the Game, better luck next time")
            return
        if Draw_scenario(_SELF_.board):
            _SELF_.Declare_result("The Game is DRAW!!, Try harder")
            return

    def Declare_result(_SELF_, result):
        result_window = tk.Toplevel(_SELF_.window)
        result_window.title("Result")
        tk.Label(result_window, text=result).pack()
        tk.Button(result_window, text="OK", command=result_window.destroy).pack()

    def restart(_SELF_):
        for row in range(3):
            for col in range(3):
                _SELF_.board[row][col] = ' '
                _SELF_.buttons[row][col].config(text=' ', state='normal')

if __name__ == "__main__":
    TTT_GUI()
