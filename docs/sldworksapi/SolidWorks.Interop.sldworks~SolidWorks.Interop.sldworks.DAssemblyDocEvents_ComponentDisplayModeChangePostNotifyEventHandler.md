# DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler`

Fired after a reference component's display mode is changed in an assembly.
Fired after a reference component's display mode is changed in an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler( _
   ByVal Component As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler( 
   System.object Component
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler( 
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

[DAssemblyDocEvents\_ComponentDisplayModeChangePostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentDisplayModeChangePostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
