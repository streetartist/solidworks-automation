# ActivateTaskPane Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ActivateTaskPane`

Activates the specified task pane.
Activates the specified task pane.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ActivateTaskPane( _
   ByVal TaskPaneID As System.Integer _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim TaskPaneID As System.Integer
Dim value As System.Boolean
 
value = instance.ActivateTaskPane(TaskPaneID)
```

```

System.bool ActivateTaskPane( 
   System.int TaskPaneID
)
```

```

System.bool ActivateTaskPane( 
   System.int TaskPaneID
) 
```

#### Parameters

*TaskPaneID*
:   ID of task pane as defined in [swTaskPaneTab\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneTab_e.html)

#### Return Value

True if the specified task pane is activated, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)  
[ISldWorks::CreateTaskpaneView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CreateTaskpaneView2.md)  
[ISldWorks::RefreshTaskpaneContent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RefreshTaskpaneContent.md)  
[ISldWorks::TaskPaneIsPinned Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~TaskPaneIsPinned.md)  
[ITaskpaneView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaskpaneView.md)
