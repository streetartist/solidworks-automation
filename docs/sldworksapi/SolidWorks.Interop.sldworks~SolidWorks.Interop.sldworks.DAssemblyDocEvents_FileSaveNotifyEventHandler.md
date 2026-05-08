# DAssemblyDocEvents_FileSaveNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveNotifyEventHandler`

Pre-notifies the user program when a file is about to be saved and passes the current document name.
Pre-notifies the user program when a file is about to be saved and passes the current document name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FileSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FileSaveNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FileSaveNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DAssemblyDocEvents_FileSaveNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the saved file

Remarks

If developing a C++ application, use [swAssemblyFileSaveNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

When a user saves a document for the first time, SOLIDWORKS generates a[FileSaveAsNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.md) event instead of a FileSaveNotify event.

If the user attempts to close the document and S\_false is returned, then the document does not close; it remains open and is not saved.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FileSaveNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
