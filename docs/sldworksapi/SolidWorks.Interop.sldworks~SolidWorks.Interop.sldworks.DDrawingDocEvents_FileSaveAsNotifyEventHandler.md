# DDrawingDocEvents_FileSaveAsNotifyEventHandler Delegate

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotifyEventHandler`

Obsolete. Superseded by DDrawingDocEvents_FileSaveAsNotify2EventHandler.
Obsolete. Superseded by [DDrawingDocEvents\_FileSaveAsNotify2EventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Delegate Function DDrawingDocEvents_FileSaveAsNotifyEventHandler( _
   ByVal FileName As System.String _
) As System.Integer
```

```

Dim instance As New DDrawingDocEvents_FileSaveAsNotifyEventHandler(AddressOf HandlerMethod)
```

```

public delegate System.int DDrawingDocEvents_FileSaveAsNotifyEventHandler( 
   System.string FileName
)
```

```

public delegate System.int DDrawingDocEvents_FileSaveAsNotifyEventHandler( 
   System.String^ FileName
)
```

#### Parameters

*FileName*
:   Name of the current document

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[DDrawingDocEvents\_FileSaveAsNotifyEventHandler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotifyEventHandler.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
