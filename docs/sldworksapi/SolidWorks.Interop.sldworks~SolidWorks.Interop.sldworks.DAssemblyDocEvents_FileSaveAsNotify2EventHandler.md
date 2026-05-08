# DAssemblyDocEvents_FileSaveAsNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler`

Pre-notifies the user program when a file is about to be saved with a new name and passes the new document name. This event is sent before SOLIDWORKS displays the File Save dialog.
Pre-notifies the user program when a file is about to be saved with a new name and passes the new document name. This event is sent before SOLIDWORKS displays the File Save dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DAssemblyDocEvents_FileSaveAsNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DAssemblyDocEvents_FileSaveAsNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DAssemblyDocEvents_FileSaveAsNotify2EventHandler( 
   System.string FileName
)
```

```

public delegate System.int DAssemblyDocEvents_FileSaveAsNotify2EventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the saved file

Remarks

If developing a C++ application, use [swAssemblyFileSaveAsNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

In the FileSaveAsNotify2 event handler, the user can specify the filename that the file should be saved as using [IModelDoc2::SetSaveAsFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveAsFileName.md). The user should also return S\_false from the event handler to indicate the notification is handled. After an appropriate filename is provided and S\_false is returned from the event handler, SOLIDWORKS does not display the File Save dialog, but uses the filename that was provided with IModelDoc2::SetSaveAsFileName.

If you do not set an alternative filename using IModelDoc2::SetSaveAsFileName and S\_false is returned, then the document is not saved. You can omit using ModelDoc2::SetSaveAsFileName to not set an alternative filename.

NOTE:  Because this event is very similar to the now obsolete IAssemblyDoc event FileSaveAsNotify, do not listen for both notifications at the same time.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DAssemblyDocEvents\_FileSaveAsNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
