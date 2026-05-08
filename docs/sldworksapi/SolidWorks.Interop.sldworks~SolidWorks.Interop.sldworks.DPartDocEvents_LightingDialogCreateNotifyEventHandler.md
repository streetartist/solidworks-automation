# DPartDocEvents_LightingDialogCreateNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LightingDialogCreateNotifyEventHandler`

Fired when a lighting dialog has been opened by the user.
Fired when a lighting dialog has been opened by the user.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_LightingDialogCreateNotifyEventHandler( _
   ByVal dialog As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_LightingDialogCreateNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_LightingDialogCreateNotifyEventHandler( 
   System.object dialog
)
```

```

public delegate System.int DPartDocEvents_LightingDialogCreateNotifyEventHandler( 
   System.Object^ dialog
)
```

#### Parameters

*dialog*
:   [Light dialog](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILightDialog.md)

Remarks

If developing a C++ application, use [swPartLightingDialogCreateNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_LightingDialogCreateNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_LightingDialogCreateNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
