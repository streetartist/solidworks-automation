# DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler`

Fired when the display state, such as shaded, wireframe, and so on, of a component is changed.
Fired when the display state, such as shaded, wireframe, and so on, of a component is changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler( _
   ByVal Component As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler( 
   System.object Component
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler( 
   System.Object^ Component
)
```

#### Parameters

*Component*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

If developing a C++ application, use [swAssemblyComponentDisplayStateChangeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentDisplayStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
