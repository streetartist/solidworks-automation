# ExitApp Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ExitApp`

Shuts down SOLIDWORKS.
Shuts down SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ExitApp() 
```

```

Dim instance As ISldWorks
 
instance.ExitApp()
```

```

void ExitApp()
```

```

void ExitApp(); 
```

Remarks

This method is not normally used with macros (\*.swp) because it shuts down your SOLIDWORKS session.

For C++ and Visual Basic projects, ending your program does not guarantee that the SOLIDWORKS processes are closed. During development, you can determine whether processes are left running by checking the Process Viewer and looking for any SLDWORKS processes. Typically, you do not want the SLDWORKS process running after your program has ended. Calling this method ensures that no SOLIDWORKS processes are left running when your program ends.

However, the CreateObject ("SldWorks.Application") statement used to start up the SOLIDWORKS software either creates a new SOLIDWORKS session or it attaches to an existing SOLIDWORKS session. If the end-user currently has an open SOLIDWORKS session, then your program attaches to it. Performing this method ends that session.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
