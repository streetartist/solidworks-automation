# DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler`

Fired before a reference component's display mode is changed in an assembly.
Fired before a reference component's display mode is changed in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler( _
   ByVal Component As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler( 
   System.object Component
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler( 
   System.Object^ Component
)
```

#### Parameters

*Component*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentDisplayModeChangePreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayModeChangePreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
