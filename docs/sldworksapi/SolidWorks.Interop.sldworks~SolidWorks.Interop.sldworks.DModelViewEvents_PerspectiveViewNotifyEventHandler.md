# DModelViewEvents_PerspectiveViewNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PerspectiveViewNotifyEventHandler`

Post-notifies the user program when the perspective view is changed (for example, if the user rotates the perspective view).
Post-notifies the user program when the perspective view is changed (for example, if the user rotates the perspective view).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DModelViewEvents_PerspectiveViewNotifyEventHandler( _
   ByVal Left As System.Double, _
   ByVal Right As System.Double, _
   ByVal bottom As System.Double, _
   ByVal Top As System.Double, _
   ByVal zNear As System.Double, _
   ByVal zFar As System.Double _
) As System.Integer
```

```

Dim instance As New DModelViewEvents_PerspectiveViewNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DModelViewEvents_PerspectiveViewNotifyEventHandler( 
   System.double Left,
   System.double Right,
   System.double bottom,
   System.double Top,
   System.double zNear,
   System.double zFar
)
```

```

public delegate System.int DModelViewEvents_PerspectiveViewNotifyEventHandler( 
   System.double Left,
   System.double Right,
   System.double bottom,
   System.double Top,
   System.double zNear,
   System.double zFar
)
```

#### Parameters

*Left*
:   Coordinate of the left vertical clipping plane

*Right*
:   Coordinate of the right vertical clipping plane

*bottom*
:   Coordinate of the bottom horizontal clipping plane

*Top*
:   Coordinate of the top horizontal clipping plane

*zNear*
:   Distance to the near depth clipping plane

*zFar*
:   Distance to the far depth clipping plane

Remarks

If developing a C++ application, use [swViewPerspectiveViewNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swViewNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DModelViewEvents\_PerspectiveViewNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DModelViewEvents_PerspectiveViewNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
