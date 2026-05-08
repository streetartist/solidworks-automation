# DAssemblyDocEvents_FileDropNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler`

Fired when a part is dropped from File Explorer into an assembly.
Fired when a part is dropped from File Explorer into an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FileDropNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FileDropNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FileDropNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DAssemblyDocEvents_FileDropNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   File name of the part

Remarks

If developing a C++ application, use [swAssemblyFileDropNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

[IAssemblyDoc::SetDroppedFileConfigName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileConfigName.md) allows you to set the configuration name for the recently dropped part, thereby avoiding the configuration name selection dialog.

SOLIDWORKS passes the file name of the dropped part into the event handler. The event handler can use [IAssemblyDoc::SetDroppedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.md) to replace this document with a temporary document. For example, this is useful when the file being dropped is managed by a project data management (PDM) system or otherwise not accessible directly by SOLIDWORKS. Your application (the PDM system in this example) is responsible for ensuring that the files and references are properly updated.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FileDropNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
