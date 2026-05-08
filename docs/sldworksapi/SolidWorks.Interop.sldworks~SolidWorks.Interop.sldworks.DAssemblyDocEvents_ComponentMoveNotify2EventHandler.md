# DAssemblyDocEvents_ComponentMoveNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentMoveNotify2EventHandler`

Post-notification that is sent when a user releases the mouse button indicating that the components have been moved to the desired destination.
Post-notification that is sent when a user releases the mouse button indicating that the components have been moved to the desired destination.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentMoveNotify2EventHandler( _
   ByRef Components As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentMoveNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentMoveNotify2EventHandler( 
   ref System.object Components
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentMoveNotify2EventHandler( 
   System.Object^% Components
)
```

#### Parameters

*Components*
:   Array of [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s

Remarks

If developing a C++ application, use [swAssemblyComponentMoveNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentMoveNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentMoveNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
