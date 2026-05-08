# DPartDocEvents_FileDropPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileDropPostNotifyEventHandler`

Post-notifies user applications when a part is dropped from File Explorer into a part document.
Post-notifies user applications when a part is dropped from File Explorer into a part document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FileDropPostNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FileDropPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FileDropPostNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DPartDocEvents_FileDropPostNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Full path and name of file dropped

Remarks

The part document may be replaced by the dropped file.

SOLIDWORKS passes the file name of the dropped part into the event handler. The event handler can use [IPartDoc::SetDroppedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetDroppedFileName.md) to replace this document with a temporary document. For example, this is useful when the file being dropped is managed by a project data management (PDM) system or otherwise not accessible directly by SOLIDWORKS. Your application (the PDM system in this example) is responsible for ensuring that the files and references are properly updated.

If developing a C++ application, use [swPartFileDropPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FileDropPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileDropPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
