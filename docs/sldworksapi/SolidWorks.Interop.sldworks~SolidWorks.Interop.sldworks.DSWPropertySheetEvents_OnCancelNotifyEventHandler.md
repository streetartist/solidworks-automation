# DSWPropertySheetEvents_OnCancelNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnCancelNotifyEventHandler`

Fired when the Cancel button on the property sheet is clicked. Your add-in can perform clean-up activities in this event.
Fired when the Cancel button on the property sheet is clicked. Your add-in can perform clean-up activities in this event.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSWPropertySheetEvents_OnCancelNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSWPropertySheetEvents_OnCancelNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSWPropertySheetEvents_OnCancelNotifyEventHandler()
```

```

public delegate System.int DSWPropertySheetEvents_OnCancelNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swPropertySheetOnCancelNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSWPropertySheetEvents\_OnCancelNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnCancelNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
