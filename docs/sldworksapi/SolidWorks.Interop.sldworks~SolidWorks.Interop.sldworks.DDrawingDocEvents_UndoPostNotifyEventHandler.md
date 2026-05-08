# DDrawingDocEvents_UndoPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UndoPostNotifyEventHandler`

Fired after an Undo action occurs in a drawing document.
Fired after an Undo action occurs in a drawing document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_UndoPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_UndoPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_UndoPostNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_UndoPostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swDrawingUndoPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Example

[Undo Deleted Note and Fire Undo Pre- and Post-notify Events (VBA)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VB.htm)  
[Undo Deleted Note and Fire Undo Pre- and Post-notify Events (VB.NET)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_VBNET.htm)  
[Undo Deleted Note and Fire Undo Pre- and Post-notify Events (C#)](Undo_Deleted_Note_and_Fire_Undo_Post-Notify_Event_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_UndoPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_UndoPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDoc2::EditUndo2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditUndo2.md)  
[DAssemblyDocEvents\_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_UndoPostNotifyEventHandler.md)  
[DPartDocEvents\_UndoPostNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_UndoPostNotifyEventHandler.md)
