# DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler`

Obsolete. Superseded by DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler.
Obsolete. Superseded by [DAssemblyDocEvents\_ComponentStateChangeNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotify2EventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler( _
   ByVal componentModel As System.Object, _
   ByVal oldCompState As System.Short, _
   ByVal newCompState As System.Short _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler( 
   System.object componentModel,
   System.short oldCompState,
   System.short newCompState
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler( 
   System.Object^ componentModel,
   System.short oldCompState,
   System.short newCompState
)
```

#### Parameters

*componentModel*

*oldCompState*

*newCompState*

#### Return Value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentStateChangeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
