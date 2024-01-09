#!/usr/bin/env python
# coding: utf-8

# In[4]:


import tkinter as tk
from tkinter import ttk, messagebox
import random
import sys

class WardrobeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("选择困难症的电子衣橱")

        self.tops = ["scuba half-zip骨白", "枯玫瑰色Hoodie", "淡蓝色小花开衫", "淡紫色毛衣", "黄白色开衫"]
        self.bottoms = ["lulu flare", "ff 碳尘色", "agolde牛仔", "白色垂坠裤"]
        self.outerwears = ["反光羽绒服", "define 白色", "淡粉lulu", "紫毛绒羽绒服", "黑色大衣", "淡蓝皮衣"]
        self.shoes = ["crocs鲸鱼", "honka", "allbirds"]

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="今日搭配").pack(pady=10)

        self.top_label = ttk.Label(self.root, text="上衣：")
        self.top_label.pack()

        self.bottom_label = ttk.Label(self.root, text="裤子：")
        self.bottom_label.pack()

        self.outerwear_label = ttk.Label(self.root, text="外套：")
        self.outerwear_label.pack()

        self.shoes_label = ttk.Label(self.root, text="鞋子：")
        self.shoes_label.pack()

        ttk.Button(self.root, text="生成随机搭配", command=self.generate_outfit).pack(pady=20)

        ttk.Button(self.root, text="OK", command=self.show_outfit_message).pack(pady=10)
        

        
    def generate_outfit(self):
        top = random.choice(self.tops)
        bottom = random.choice(self.bottoms)
        outerwear = random.choice(self.outerwears)
        shoe = random.choice(self.shoes)

        self.top_label.config(text="上衣：" + top)
        self.bottom_label.config(text="裤子：" + bottom)
        self.outerwear_label.config(text="外套：" + outerwear)
        self.shoes_label.config(text="鞋子：" + shoe)

    def show_outfit_message(self):
        outfit_message = "你今天真美！愿你一切顺利！"
        tk.messagebox.showinfo("穿搭提醒", outfit_message)
        

if __name__ == "__main__":
    root = tk.Tk()
    app = WardrobeApp(root)
    root.mainloop()

