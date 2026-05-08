# DPartDocEvents_FileSavePostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostNotifyEventHandler`

Post-notifies the user program when a part document is saved.
Post-notifies the user program when a part document is saved.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FileSavePostNotifyEventHandler( _
   ByVal saveType As System.Integer, _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FileSavePostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FileSavePostNotifyEventHandler( 
   System.int saveType,
   System.string FileName
)
```

```

public delegate System.int DPartDocEvents_FileSavePostNotifyEventHandler( 
   System.int saveType,
   System.String^ FileName
)
```

#### Parameters

*saveType*
:   Type of save as defined in [swFileSaveTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileSaveTypes_e.html)

*FileName*
:   Saved file name

Remarks

If developing a C++ application, use [swPartFileSavePostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FileSavePostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSavePostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
