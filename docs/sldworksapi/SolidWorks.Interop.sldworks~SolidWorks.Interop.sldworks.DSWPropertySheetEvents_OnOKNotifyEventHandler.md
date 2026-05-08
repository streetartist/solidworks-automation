# DSWPropertySheetEvents_OnOKNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnOKNotifyEventHandler`

Fired when the OK button on the property sheet is clicked.
Fired when the OK button on the property sheet is clicked.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSWPropertySheetEvents_OnOKNotifyEventHandler() As System.Integer
```

```

Dim instance As New DSWPropertySheetEvents_OnOKNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSWPropertySheetEvents_OnOKNotifyEventHandler()
```

```

public delegate System.int DSWPropertySheetEvents_OnOKNotifyEventHandler();
```

Remarks

Your add-in can perform clean-up activities in this event. Typically, this event calls [ISWPropertySheet::GetControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISWPropertySheet~GetControl.md) to retrieve data from your ActiveX control.

If developing a C++ application, use [swPropertySheetOnOKNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertySheetNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSWPropertySheetEvents\_OnOKNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSWPropertySheetEvents_OnOKNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
