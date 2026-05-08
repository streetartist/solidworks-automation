# DAssemblyDocEvents_FeatureEditPreNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureEditPreNotifyEventHandler`

Pre-notifies the user program when the user edits the definition of a selected feature.
Pre-notifies the user program when the user edits the definition of a selected feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FeatureEditPreNotifyEventHandler( _
   ByVal EditFeature As System.Object _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FeatureEditPreNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FeatureEditPreNotifyEventHandler( 
   System.object EditFeature
)
```

```

public delegate System.int DAssemblyDocEvents_FeatureEditPreNotifyEventHandler( 
   System.Object^ EditFeature
)
```

#### Parameters

*EditFeature*
:   Edited [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) definition

Remarks

If developing a C++ application, use [swAssemblyFeatureEditPreNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FeatureEditPreNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FeatureEditPreNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
