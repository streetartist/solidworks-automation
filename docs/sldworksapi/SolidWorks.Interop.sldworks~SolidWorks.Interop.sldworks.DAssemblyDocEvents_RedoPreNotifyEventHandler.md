# DAssemblyDocEvents_RedoPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RedoPreNotifyEventHandler`

Fired before a Redo operation occurs in an assembly document.
Fired before a Redo operation occurs in an assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_RedoPreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_RedoPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_RedoPreNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_RedoPreNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyRedoPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_CSharp.htm)  
[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VB.NET)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VBNET.htm)  
[Fire Undo and Redo Pre- and Post-notifications in Assembly Document (VBA)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Assembly_Document_Example_VB6.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_RedoPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RedoPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
