# IsTaskPaneVisible Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneVisible`

Gets whether the Task Pane is visible.
Gets whether the Task Pane is visible.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTaskPaneVisible() As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
value = instance.IsTaskPaneVisible()
```

```

System.bool IsTaskPaneVisible()
```

```

System.bool IsTaskPaneVisible(); 
```

#### Return Value

True if the Task Pane is visible, false if not

Example

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ITaskpaneView::IsActiveTab Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~IsActiveTab.md)  
[ISldWorks::IsTaskPaneExpanded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneExpanded.md)
