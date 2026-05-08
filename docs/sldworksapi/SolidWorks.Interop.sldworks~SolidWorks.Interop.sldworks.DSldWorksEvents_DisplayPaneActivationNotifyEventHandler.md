# DSldWorksEvents_DisplayPaneActivationNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DisplayPaneActivationNotifyEventHandler`

Fired when the Display Pane is activated.
Fired when the Display Pane is activated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_DisplayPaneActivationNotifyEventHandler( _
   ByVal ActivePaneIndex As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_DisplayPaneActivationNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_DisplayPaneActivationNotifyEventHandler( 
   System.int ActivePaneIndex
)
```

```

public delegate System.int DSldWorksEvents_DisplayPaneActivationNotifyEventHandler( 
   System.int ActivePaneIndex
)
```

#### Parameters

*ActivePaneIndex*
:   Display Pane as defined by [swDisplayPaneIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDisplayPaneIndex_e.html)

Remarks

If developing a C++ application, use [swAppDisplayPaneActivationNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

[Create Task Pane View Add-in (C#)](Create_TaskPaneView_Add-in_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_DisplayPaneActivationNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_DisplayPaneActivationNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
