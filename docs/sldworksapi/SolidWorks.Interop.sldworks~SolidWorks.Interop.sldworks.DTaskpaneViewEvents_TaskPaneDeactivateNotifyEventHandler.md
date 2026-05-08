# DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler`

Post-notifies the user program when an application-level Task Pane view is deactivated.
Post-notifies the user program when an application-level Task Pane view is deactivated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler() As System.Integer
```

```

Dim instance As New DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler()
```

```

public delegate System.int DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAppTaskPaneDeactivateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DTaskpaneViewEvents\_TaskPaneDeactivateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneDeactivateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
