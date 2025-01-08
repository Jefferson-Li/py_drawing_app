import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("簡單繪圖程式")
        
        # 創建畫布
        self.canvas = tk.Canvas(root, width=800, height=600, bg='white')
        self.canvas.pack(expand=True, fill='both')
        
        # 初始化變數
        self.old_x = None
        self.old_y = None
        self.line_width = 2
        self.color = 'black'
        
        # 綁定滑鼠事件
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        
        # 創建工具列
        self.create_toolbox()
        
    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                                 width=self.line_width, fill=self.color,
                                 capstyle=tk.ROUND, smooth=True)
        self.old_x = event.x
        self.old_y = event.y
        
    def reset(self, event):
        self.old_x = None
        self.old_y = None
        
    def change_color(self):
        color = colorchooser.askcolor(color=self.color)[1]
        if color:
            self.color = color
            
    def clear_canvas(self):
        self.canvas.delete('all')
        
    def create_toolbox(self):
        # 創建工具按鈕
        frame = tk.Frame(self.root)
        frame.pack(side='top', fill='x')
        
        tk.Button(frame, text='選擇顏色', command=self.change_color).pack(side='left')
        tk.Button(frame, text='清除畫布', command=self.clear_canvas).pack(side='left')
        
        # 筆刷大小滑動條
        tk.Label(frame, text='筆刷大小:').pack(side='left')
        self.size_scale = tk.Scale(frame, from_=1, to=10, orient='horizontal',
                                 command=lambda x: setattr(self, 'line_width', int(x)))
        self.size_scale.set(2)
        self.size_scale.pack(side='left')

if __name__ == '__main__':
    root = tk.Tk()  # 修正這行
    app = DrawingApp(root)
    root.mainloop()