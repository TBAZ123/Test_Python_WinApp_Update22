from cx_Freeze import setup, Executable
setup(name="Python Appliction",
      options={"build_exe":{"packages":["tkinter"],
                            }},
                            version="1.2.3",
                            description="Python Appliction",
                            executables=[Executable(r"D:\Works\STD\Test_Python_WinApp_Update22\main.py",
                                                    shortcutName="Python Appliction",
                                                    shortcutDir="DesktopFolder",
                                                    base="Win32GUI")]
                                                    )
