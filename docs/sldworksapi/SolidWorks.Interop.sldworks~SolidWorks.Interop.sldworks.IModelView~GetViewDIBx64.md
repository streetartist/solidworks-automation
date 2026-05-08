# GetViewDIBx64 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIBx64`

Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications.
Gets an image of the document as it looks in Normal view or in the print preview in 64-bit applications.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetViewDIBx64() As System.Long
```

```

Dim instance As IModelView
Dim value As System.Long
 
value = instance.GetViewDIBx64()
```

```

System.long GetViewDIBx64()
```

```

System.int64 GetViewDIBx64(); 
```

#### Return Value

Pointer to DIBSECTION for image

Remarks

The image type and resolution can be controlled interactively under TIFF export options.

If TIFF export is set to screen, then the output from this method is based on the current screen resolution. If it's set to print, then the output is based on the DPI specified in the TIFF options dialog.

The memory for the image bits (DIBSECTION.dsBm.bmBits) and this structure are allocated by the SOLIDWORKS application and must be deleted by the caller. For more information, see the description of Bitmap structures and DIBSECTION in Microsoft Help.

**NOTE:** This method is only available through early binding and with 64-bit versions of the SOLIDWORKS software.

Example

[Get Names of Components, Window Handles, and DIBSECTIONs (C#)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_CSharp.htm)  
[Get Names of Components, Window Handles, and DIBSECTIONs (VB.NET)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VBNET.htm)  
[Get Names of Components, Window Handles, and DIBSECTIONs (VBA)](Get_Names_of_Components_and_Window_Handle,_and_DIBSECTION_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView.md)  
[IModelView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView_members.md)  
[IModeler::GetViewDIB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelView~GetViewDIB.md)
