# DSldWorksEvents_FileCloseNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler`

Notifies the user program when SOLIDWORKS is finished closing a file.
Notifies the user program when SOLIDWORKS is finished closing a file.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DSldWorksEvents_FileCloseNotifyEventHandler( _
   ByVal FileName As System.String, _
   ByVal reason As System.Integer _
) As System.Integer
```

```

Dim instance As New DSldWorksEvents_FileCloseNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DSldWorksEvents_FileCloseNotifyEventHandler( 
   System.string FileName,
   System.int reason
)
```

```

public delegate System.int DSldWorksEvents_FileCloseNotifyEventHandler( 
   System.String^ FileName,
   System.int reason
)
```

#### Parameters

*FileName*
:   Name of closed file

*reason*
:   Reason for closing as defined in [swFileCloseNotifyReason\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileCloseNotifyReason_e.html)

Remarks

This event occurs after a drawing document is closed using [ISldWorks::CloseAndReopen](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseAndReopen.md).

If developing a C++ application, use [swAppFileCloseNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html) to register for this notification.

Example

Contact SOLIDWORKS API Support to obtain **Close and Reopen a Drawing Document (VBA, VB.NET, C#).**

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DSldWorksEvents\_FileCloseNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_FileCloseNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
