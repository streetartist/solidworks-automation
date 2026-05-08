# DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler`

Fired whenever the state of a component within this assembly changes.
Fired whenever the state of a component within this assembly changes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler( _
   ByVal Component As System.Object, _
   ByVal CompName As System.String, _
   ByVal oldCompState As System.Short, _
   ByVal newCompState As System.Short _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler( 
   System.object Component,
   System.string CompName,
   System.short oldCompState,
   System.short newCompState
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler( 
   System.Object^ Component,
   System.String^ CompName,
   System.short oldCompState,
   System.short newCompState
)
```

#### Parameters

*Component*
:   [IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

*CompName*
:   Name of the component

*oldCompState*
:   Previous state of the component as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

*newCompState*
:   New state of the component as defined in [swComponentSuppressionState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentSuppressionState_e.html)

Remarks

If developing a C++ application, use [swAssemblyComponentStateChangeNotify3](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

SOLIDWORKS sends this notification:

- even if the assembly is not the active document.
- when a component gets suppressed due to an internal ID mismatch.
- not at all if a part is explicitly opened by the user or opened programmatically. In that case, SOLIDWORKS resolves the component part in any open assembly that references it. Your application must watch for the SOLIDWORKS event [FileOpenNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileOpenNotify2EventHandler.md).

When a component is resolved or unsuppressed, its model document becomes available to your application. Within this notification, you can get this object and register for other events. This might be useful for project data management (PDM) applications that want to ask the user to check out the assembly component if the user tries to make changes.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentStateChangeNotify3EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentStateChangeNotify3EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
