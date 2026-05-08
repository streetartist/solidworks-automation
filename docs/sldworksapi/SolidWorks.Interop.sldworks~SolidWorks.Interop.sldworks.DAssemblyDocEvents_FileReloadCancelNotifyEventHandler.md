# DAssemblyDocEvents_FileReloadCancelNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileReloadCancelNotifyEventHandler`

Fired if the IAssembly event FileReloadNotify is canceled.
Fired if the IAssembly event [FileReloadNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileReloadNotifyEventHandler.md) is canceled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FileReloadCancelNotifyEventHandler( _
   ByVal ErrorCode As System.Integer _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FileReloadCancelNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FileReloadCancelNotifyEventHandler( 
   System.int ErrorCode
)
```

```

public delegate System.int DAssemblyDocEvents_FileReloadCancelNotifyEventHandler( 
   System.int ErrorCode
)
```

#### Parameters

*ErrorCode*
:   Error as defined in [swComponentReloadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

Remarks

If developing a C++ application, use [swAssemblyFileReloadCancelNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FileReloadCancelNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileReloadCancelNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
