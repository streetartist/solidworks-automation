# DAssemblyDocEvents_RegenPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotifyEventHandler`

Obsolete. Superseded by DAssemblyDocEvents RegenPostNotify2EventHandler.
Obsolete. Superseded by [DAssemblyDocEvents RegenPostNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_RegenPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_RegenPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_RegenPostNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_RegenPostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyRegenPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

You can also use [IModelDoc2::GetUpdateStamp](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUpdateStamp.md) to determine when changes take place in this document.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_RegenPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
