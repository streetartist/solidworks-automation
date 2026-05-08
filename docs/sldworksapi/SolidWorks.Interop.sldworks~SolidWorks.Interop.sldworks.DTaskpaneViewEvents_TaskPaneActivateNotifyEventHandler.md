# DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler`

Post-notifies the user program when an application-level Task Pane view is activated.
Post-notifies the user program when an application-level Task Pane view is activated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler() As System.Integer
```

```

Dim instance As New DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler()
```

```

public delegate System.int DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAppTaskPaneActivateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTaskPaneNotify_e.html) to register for this notification.

Example

[Add Buttons to Task Pane (VBA)](Add_Buttons_to_Task_Pane_Example_VB.htm)  
[Add Buttons to Task Pane (VB.NET)](Add_Buttons_to_Task_Pane_Example_VBNET.htm)  
[Add Buttons to Task Pane (C#)](Add_Buttons_to_Task_Pane_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DTaskpaneViewEvents\_TaskPaneActivateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DTaskpaneViewEvents_TaskPaneActivateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
