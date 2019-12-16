from tkinter import *
from school import inter


def tkmain():
    root = Tk()
    Label(root, text="请输入学号").grid(row=0, column=0)
    Label(root, text="请输入密码").grid(row=1, column=0)

    e1 = Entry(root)
    e1.grid(row=0, column=1, padx=10, pady=5)
    e2 = Entry(root, show="*")
    e2.grid(row=1, column=1, padx=10, pady=5)

    txta = e1.get()
    txtb = e2.get()

    Button(root, text="确定", width=10, command=lambda: inter(txta, txtb)).grid(row=3, column=0, sticky=W, padx=10,
                                                                              pady=5)
    Button(root, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, padx=10, pady=5)

    mainloop()


if __name__ == '__main__':
    tkmain()
