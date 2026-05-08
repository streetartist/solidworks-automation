# DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler`

Generated when a body is cut into multiple bodies.
Generated when a body is cut into multiple bodies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler( _
   ByVal Feature As System.Object, _
   ByRef Bodies As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler( 
   System.object Feature,
   ref System.object Bodies
)
```

```

public delegate System.int DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler( 
   System.Object^ Feature,
   System.Object^% Bodies
)
```

#### Parameters

*Feature*
:   [Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

*Bodies*
:   Array of [bodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)

Remarks

If developing a C++ application, use [swAssemblyPromptBodiesToKeepNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_PromptBodiesToKeepNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PromptBodiesToKeepNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
