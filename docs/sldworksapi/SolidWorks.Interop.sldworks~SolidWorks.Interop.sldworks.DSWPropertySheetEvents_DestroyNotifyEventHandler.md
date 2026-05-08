# DSWPropertySheetEvents_DestroyNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_DestroyNotifyEventHandler`

Fired when the property sheet is in the process of being destroyed.
Fired when the property sheet is in the process of being destroyed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSWPropertySheetEvents_DestroyNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSWPropertySheetEvents_DestroyNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSWPropertySheetEvents_DestroyNotifyEventHandler()
```

```

public delegate System.int DSWPropertySheetEvents_DestroyNotifyEventHandler();
```

Remarks

When this event is fired, the window associated with the destroyed property sheet is still alive, but any API pages have already been removed.

 If developing a C++ application, use [swPropertySheetDestroyNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSWPropertySheetEvents\_DestroyNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_DestroyNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
