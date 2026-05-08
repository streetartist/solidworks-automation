# DModelViewEvents_RepaintPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RepaintPostNotifyEventHandler`

Post-notifies the user program when a view has been repainted.
Post-notifies the user program when a view has been repainted.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_RepaintPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DModelViewEvents_RepaintPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_RepaintPostNotifyEventHandler()
```

```

public delegate System.int DModelViewEvents_RepaintPostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swViewRepaintPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_RepaintPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_RepaintPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
