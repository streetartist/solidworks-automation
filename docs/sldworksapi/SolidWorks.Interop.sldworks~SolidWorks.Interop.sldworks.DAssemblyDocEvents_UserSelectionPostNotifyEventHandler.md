# DAssemblyDocEvents_UserSelectionPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPostNotifyEventHandler`

Fired after an entity is selected in an assembly document.
Fired after an entity is selected in an assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_UserSelectionPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_UserSelectionPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_UserSelectionPostNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_UserSelectionPostNotifyEventHandler();
```

Remarks

Only selections made interactively fire this event; selections made programmatically are ignored by this event.

If developing a C++ application, use [swAssemblyUserSelectionPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Event After Selection Made (C#)](Fire_Event_After_Selection_Made_Example_CSharp.htm)  
[Fire Event After Selection Made (VB.NET)](Fire_Event_After_Selection_Made_Example_VBNET.htm)  
[Fire Event After Selection Made (VBA)](Fire_Event_After_Selection_Made_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_UserSelectionPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DAssemblyDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DDrawingDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DDrawingDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.md)
