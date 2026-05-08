# DPartDocEvents_FileReloadCancelNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileReloadCancelNotifyEventHandler`

Fired if FileReloadNotify is canceled.
Fired if [FileReloadNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileReloadNotifyEventHandler.md) is canceled.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FileReloadCancelNotifyEventHandler( _
   ByVal ErrorCode As System.Integer _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FileReloadCancelNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FileReloadCancelNotifyEventHandler( 
   System.int ErrorCode
)
```

```

public delegate System.int DPartDocEvents_FileReloadCancelNotifyEventHandler( 
   System.int ErrorCode
)
```

#### Parameters

*ErrorCode*
:   Error as defined in [swComponentReloadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swComponentReloadError_e.html)

Remarks

If developing a C++ application, use [swPartFileReloadCancelNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FileReloadCancelNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileReloadCancelNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
