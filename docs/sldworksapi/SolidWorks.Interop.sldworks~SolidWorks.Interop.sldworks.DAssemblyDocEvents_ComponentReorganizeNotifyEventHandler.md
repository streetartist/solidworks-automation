# DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler`

Fired when one or more components are reorganized in an assembly or sub-assembly.
Fired when one or more components are reorganized in an assembly or sub-assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler( _
   ByVal sourceName As System.String, _
   ByVal targetName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler( 
   System.string sourceName,
   System.string targetName
)
```

```

public delegate System.int DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler( 
   System.String^ sourceName,
   System.String^ targetName
)
```

#### Parameters

*sourceName*
:   Source name

*targetName*
:   Target name

Remarks

If developing a C++ application, use [swAssemblyComponentReorganizeNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Example

[Reorganize Components (VBA)](Reorganize_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_ComponentReorganizeNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IAssemblyDoc::IReorganizeComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IReorganizeComponents.md)  
[IAssemblyDoc::ReorganizeComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReorganizeComponents.md)
