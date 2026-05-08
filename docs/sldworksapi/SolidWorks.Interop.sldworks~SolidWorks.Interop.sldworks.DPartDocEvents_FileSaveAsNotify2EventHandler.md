# DPartDocEvents_FileSaveAsNotify2EventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler`

Sends pre-notification before displaying the File, Save dialog.
Sends pre-notification before displaying the File, Save dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DPartDocEvents_FileSaveAsNotify2EventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DPartDocEvents_FileSaveAsNotify2EventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DPartDocEvents_FileSaveAsNotify2EventHandler( 
   System.string FileName
)
```

```

public delegate System.int DPartDocEvents_FileSaveAsNotify2EventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the saved file

Remarks

In this event handler, the user can specify the filename that the file should be saved to by using [IModelDoc2::SetSaveAsFileName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveAsFileName.md) and also returning S\_false from the event handler. After providing an appropriate filename and after S\_false is returned from the event handler,  the File, Save dialog is not displayed; instead, the filename that was provided with IModelDoc2::SetSaveAsFileName is used.

If developing a C++ application, use [swPartFileSaveAsNotify2](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DPartDocEvents\_FileSaveAsNotify2EventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
