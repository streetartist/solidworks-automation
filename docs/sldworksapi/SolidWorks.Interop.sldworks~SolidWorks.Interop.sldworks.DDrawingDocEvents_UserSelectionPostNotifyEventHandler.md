# DDrawingDocEvents_UserSelectionPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPostNotifyEventHandler`

Fired after an entity is selected in a drawing document.
Fired after an entity is selected in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_UserSelectionPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_UserSelectionPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_UserSelectionPostNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_UserSelectionPostNotifyEventHandler();
```

Remarks

Only selections made interactively fire this event; selections made programmatically are ignored by this event.

If developing a C++ application, use [swDrawingUserSelectionPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Example

[Fire Event After Selection Made (C#)](Fire_Event_After_Selection_Made_Example_CSharp.htm)  
[Fire Event After Selection Made (VB.NET)](Fire_Event_After_Selection_Made_Example_VBNET.htm)  
[Fire Event After Selection Made (VBA)](Fire_Event_After_Selection_Made_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_UserSelectionPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DDrawingDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DAssemblyDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DAssemblyDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UserSelectionPreNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPostNotifyEventHandler.md)  
[DPartDocEvents\_UserSelectionPreNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UserSelectionPreNotifyEventHandler.md)
