# DDrawingDocEvents_FileSaveAsNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler`

Sends pre-notification before displaying the File, Save dialog.
Sends pre-notification before displaying the File, Save dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_FileSaveAsNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_FileSaveAsNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_FileSaveAsNotify2EventHandler( 
   System.string FileName
)
```

```

public delegate System.int DDrawingDocEvents_FileSaveAsNotify2EventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the saved file

Remarks

SOLIDWORKS sends this notification before it displays the Save dialog.

In the FileSaveAsNotify2 event handler, you can specify an alternate file name using [IModelDoc2::SetSaveAsFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveAsFileName.md) and return S\_false from the event handler to indicate that the notification is handled. If you do not set an alternative filename using IModelDoc2::SetSaveAsFileName and S\_false is returned, then the document is not saved. You can omit using IModelDoc2::SetSaveAsFileName to not set an alternative filename.

You can return S\_false to stop SOLIDWORKS from proceeding with the action that caused the notification. In .NET,  you can return 1 instead of S\_false.

NOTE:  Because this event is very similar to the now obsolete Drawing Doc event [FileSaveAsNotify](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotifyEventHandler.md), do not listen for both notifications at the same time.

If developing a C++ application, use [swDrawingFileSaveAsNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDrawingNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_FileSaveAsNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
