# DAssemblyDocEvents_FileDropPostNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropPostNotifyEventHandler`

Post-notifies user applications when a part is dropped from File Explorer into an assembly.
Post-notifies user applications when a part is dropped from File Explorer into an assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FileDropPostNotifyEventHandler() As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FileDropPostNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FileDropPostNotifyEventHandler()
```

```

public delegate System.int DAssemblyDocEvents_FileDropPostNotifyEventHandler();
```

Remarks

If developing a C++ application, use [swAssemblyFileDropPostNotify](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

SOLIDWORKS passes the file name of the dropped part into the event handler. The event handler can use [IAssemblyDoc::SetDroppedFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SetDroppedFileName.md) to replace this document with a temporary document. For example, this is useful when the file being dropped is managed by a project data management (PDM) system or otherwise not accessible directly by SOLIDWORKS. Your application (the PDM system in this example) is responsible for ensuring that the files and references are properly updated.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FileDropPostNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropPostNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
