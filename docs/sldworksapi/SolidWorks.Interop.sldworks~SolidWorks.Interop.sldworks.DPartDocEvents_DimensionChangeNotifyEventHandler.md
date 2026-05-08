# DPartDocEvents_DimensionChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DimensionChangeNotifyEventHandler`

Fired when a dimension is changed through the Dimension dialog.
Fired when a dimension is changed through the Dimension dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_DimensionChangeNotifyEventHandler( _
   ByVal displayDim As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_DimensionChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_DimensionChangeNotifyEventHandler( 
   System.object displayDim
)
```

```

public delegate System.int DPartDocEvents_DimensionChangeNotifyEventHandler( 
   System.Object^ displayDim
)
```

#### Parameters

*displayDim*
:   [Display dimension](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayDimension.md) that changed

Remarks

If developing a C++ application, use [swPartDimensionChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_DimensionChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_DimensionChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
