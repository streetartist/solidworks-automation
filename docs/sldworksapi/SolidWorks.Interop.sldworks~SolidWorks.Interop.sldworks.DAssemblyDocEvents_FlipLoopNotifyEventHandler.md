# DAssemblyDocEvents_FlipLoopNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FlipLoopNotifyEventHandler`

Notifies your program when a loop flips.
Notifies your program when a loop flips.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FlipLoopNotifyEventHandler( _
   ByVal TheLoop As System.Object, _
   ByVal TheEdge As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FlipLoopNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FlipLoopNotifyEventHandler( 
   System.object TheLoop,
   System.object TheEdge
)
```

```

public delegate System.int DAssemblyDocEvents_FlipLoopNotifyEventHandler( 
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

If developing a C++ application, use [swAssemblyFlipLoopNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FlipLoopNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FlipLoopNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[DPartDocEvents\_FlipLoopNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler.md)  
[ILoop2::Select Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~Select.md)
