# DPartDocEvents_RedoPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RedoPreNotifyEventHandler`

Fired before a Redo operation occurs in a part document.
Fired before a Redo operation occurs in a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_RedoPreNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_RedoPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_RedoPreNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_RedoPreNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swPartRedoPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Undo and Redo Pre- and Post-notifications in Part Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm)  
[Fire Undo and Redo Pre- and Post-notifications in Part Document (VB.NET)](Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VBNET.htm)  
[Fire Undo and Redo Pre- and Post-notifications in Part Document (VBA)](Fire_Undo_and_Redo_Pre_and_Post-notifications_in_Part_Document_Example_VB6.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_RedoPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RedoPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
