# DPartDocEvents_ModifyNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ModifyNotifyEventHandler`

Notifies the user program when a document is marked as dirty for the first time.
Notifies the user program when a document is marked as dirty for the first time.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_ModifyNotifyEventHandler() As System.Integer
```

```

Dim instance As New DPartDocEvents_ModifyNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_ModifyNotifyEventHandler()
```

```

public delegate System.int DPartDocEvents_ModifyNotifyEventHandler();
```

Remarks

If the user saves the document in the current SOLIDWORKS session, then the event is fired when the document is marked dirty again.

If developing a C++ application, use [swPartModifyNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_ModifyNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_ModifyNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
