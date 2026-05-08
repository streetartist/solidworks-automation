# DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler`

Notifies the application that the visible state of a body within this assembly has changed.
Notifies the application that the visible state of a body within this assembly has changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyBeginInContextEditNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_BodyVisibleChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_BodyVisibleChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
