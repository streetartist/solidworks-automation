# DPartDocEvents_RedoPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RedoPostNotifyEventHandler`

Fired after a Redo operation occurs in a part document.
Fired after a Redo operation occurs in a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_RedoPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_RedoPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_RedoPostNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_RedoPostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swPartRedoPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Example

[Fire Undo and Redo Pre- and Post-notifications in a Part Document (C#)](Fire_Undo_and_Redo_Pre-_and_Post-notifications_in_Part_Document_Example_CSharp.htm)  
[Fire Undo and Redo Pre- and Post-notifications in a Part Document (VB.NET)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VBNET.htm)  
[Fire Undo and Redo Pre- and Post-notifications in a Part Document (VBA)](Fire_Events_When_Display_State_Changes_in_Part_Document_Example_VB6.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_RedoPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RedoPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
