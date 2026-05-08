# SetSaveAsFileName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetSaveAsFileName`

Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog.
Sets the Save As filename from within the FileSaveAsNotify2 event handlers, thereby, bypassing the Save As dialog.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub SetSaveAsFileName( _
   ByVal FileName As System.String _
) 
```

```

Dim instance As IModelDoc2
Dim FileName As System.String
 
instance.SetSaveAsFileName(FileName)
```

```

void SetSaveAsFileName( 
   System.string FileName
)
```

```

void SetSaveAsFileName( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   **Save As** filename

Remarks

Use this method from within the FileSaveAsNotify2 event handler. When setting the Save As filename using this method, S\_false should be returned from the FileSaveAsNotify2 event handler. See [DAssemblyDocEvents FileSaveAsNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileSaveAsNotify2EventHandler.md), [DDrawingDocEvents FileSaveAsNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DDrawingDocEvents_FileSaveAsNotify2EventHandler.md), and [DPartDocEvents FileSaveAsNotify2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FileSaveAsNotify2EventHandler.md) notifications.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDocExtension::SaveAs Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs.md)
