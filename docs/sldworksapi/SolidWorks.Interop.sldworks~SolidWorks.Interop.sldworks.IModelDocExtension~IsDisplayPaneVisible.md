# IsDisplayPaneVisible Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsDisplayPaneVisible`

Gets whether the Display Pane is visible in this active document.
Gets whether the Display Pane is visible in this active document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsDisplayPaneVisible() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.IsDisplayPaneVisible()
```

```

System.bool IsDisplayPaneVisible()
```

```

System.bool IsDisplayPaneVisible(); 
```

#### Return Value

True if the Display Pane is visible, false if not

Example

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[ISldWorks::GetActiveDisplayPane Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetActiveDisplayPane.md)
