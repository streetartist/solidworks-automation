# DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler`

Fired when publishing an assembly document to SOLIDWORKS MBD 3D PDF.
Fired when publishing an assembly document to SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler( _
   ByVal Path As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler( 
   System.string Path
)
```

```

public delegate System.int DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler( 
   System.String^ Path
)
```

#### Parameters

*Path*
:   :   Path where SOLIDWORKS MBD 3D PDF is saved

Remarks

If developing a C++ application, use [swAssemblyPublishTo3DPDFNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_PublishTo3DPDFNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_PublishTo3DPDFNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
