# GetViewDIB Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIB`

Gets an image of the document as it looks in Normal view or in the print preview.
Gets an image of the document as it looks in Normal view or in the print preview.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViewDIB() As System.Integer
```

```

Dim instance As IModelView
Dim value As System.Integer
 
value = instance.GetViewDIB()
```

```

System.int GetViewDIB()
```

```

System.int GetViewDIB(); 
```

#### Return Value

Pointer to DIBSECTION for image

Remarks

If your application must be x64 compatible, then use [IModelView::GetViewDIBx64](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIBx64.md).

The image type and resolution can be controlled interactively under TIFF export options.

If TIFF export is set to screen, then the output from this method is based on the current screen resolution. If it's set to print, then the output is based on the DPI specified in the TIFF options dialog.

The memory for the image bits (DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS application and must be deleted by the caller. For more information, see the description of Bitmap structures and DIBSECTION in Microsoft Help.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)
