# IsTaskPaneExpanded Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneExpanded`

Gets whether the Task Pane is expanded.
Gets whether the Task Pane is expanded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsTaskPaneExpanded() As System.Boolean
```

```

Dim instance As ISldWorks
Dim value As System.Boolean
 
value = instance.IsTaskPaneExpanded()
```

```

System.bool IsTaskPaneExpanded()
```

```

System.bool IsTaskPaneExpanded(); 
```

#### Return Value

True if the Task Pane is expanded, false if not

Example

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ITaskpaneView::IsActiveTab Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView~IsActiveTab.md)  
[ISldWorks::IsTaskPaneVisible Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IsTaskPaneVisible.md)
