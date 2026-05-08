# DPartDocEvents_FlipLoopNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler`

Fired when a loop is flipped.
Fired when a loop is flipped.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FlipLoopNotifyEventHandler( _
   ByVal TheLoop As System.Object, _
   ByVal TheEdge As System.Object _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FlipLoopNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FlipLoopNotifyEventHandler( 
   System.object TheLoop,
   System.object TheEdge
)
```

```

public delegate System.int DPartDocEvents_FlipLoopNotifyEventHandler( 
   System.Object^ TheLoop,
   System.Object^ TheEdge
)
```

#### Parameters

*TheLoop*
:   [Loop](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md) that was flipped

*TheEdge*
:   [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) about which the loop was flipped

Remarks

If developing a C++ application, use [swPartFlipLoopNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FlipLoopNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DAssemblyDocEvents\_FlipLoopNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FlipLoopNotifyEventHandler.md)  
[ILoop2::Select Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~Select.md)
