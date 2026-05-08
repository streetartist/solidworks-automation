# DDrawingDocEvents_FileSaveNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveNotifyEventHandler`

Pre-notifies the user program when a file is about to be saved and passes the current document name.
Pre-notifies the user program when a file is about to be saved and passes the current document name.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_FileSaveNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_FileSaveNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_FileSaveNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DDrawingDocEvents_FileSaveNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the file to save

Remarks

When a user selects File, Save for a document that has never been saved, SOLIDWORKS generates [FileSaveAsNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.md) instead of FileSaveNotify. You can return S\_false to stop SOLIDWORKS from proceeding with the action that generated the notification.

If the user attempts to close the document and S\_false is returned, then the document does not close; it remains open and is not saved.

If developing a C++ application, use [swDrawingFileSaveAsNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_FileSaveNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
