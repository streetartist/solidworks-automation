# DAssemblyDocEvents_UndoPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UndoPostNotifyEventHandler`

Fired after an Undo operation occurs in an assembly document.
Fired after an Undo operation occurs in an assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_UndoPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_UndoPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_UndoPostNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_UndoPostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyUndoPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Undo Hidden Component and Fire Post-Notify Event (VBA)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Undo Hidden Component and Fire Post-Notify Event (VB.NET)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Hidden Component and Fire Post-Notify Event (C#)](Undo_Hidden_Component_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_UndoPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UndoPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
