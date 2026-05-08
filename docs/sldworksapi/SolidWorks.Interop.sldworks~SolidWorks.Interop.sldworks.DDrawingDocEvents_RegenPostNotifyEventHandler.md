# DDrawingDocEvents_RegenPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RegenPostNotifyEventHandler`

Post-notifies the user program when a drawing document has been regenerated.
Post-notifies the user program when a drawing document has been regenerated.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_RegenPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DDrawingDocEvents_RegenPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_RegenPostNotifyEventHandler()
```

```

public delegate System.int DDrawingDocEvents_RegenPostNotifyEventHandler();
```

Remarks

You can also use [IModelDoc2::GetUpdateStamp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUpdateStamp.md) to determine when changes have taken place in this document.

If developing a C++ application, use [swDrawingRegenPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_RegenPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_RegenPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
