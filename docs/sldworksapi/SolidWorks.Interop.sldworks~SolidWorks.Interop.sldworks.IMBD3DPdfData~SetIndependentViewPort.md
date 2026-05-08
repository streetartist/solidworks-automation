# SetIndependentViewPort Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetIndependentViewPort`

Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF.
Sets the specified view for an independent viewport for the SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetIndependentViewPort( _
   ByVal ViewName As System.String _
) As System.Boolean
```

```

Dim instance As IMBD3DPdfData
Dim ViewName As System.String
Dim value As System.Boolean
 
value = instance.SetIndependentViewPort(ViewName)
```

```

System.bool SetIndependentViewPort( 
   System.string ViewName
)
```

```

System.bool SetIndependentViewPort( 
   System.String^ ViewName
) 
```

#### Parameters

*ViewName*
:   Name of the view (e.g., "Top View" or "\*Top")

#### Return Value

True if the specified view is set for an independent viewport for the SOLIDWORKS MBD 3D PDF, false if not (see **Remarks**)

Remarks

The [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) for the SOLIDWORKS MBD 3D PDF must contain an independent viewport. See the examples for instructions on how to add an independent viewport to a theme and how to set a view for that independent viewport.

Example

[Set Independent Viewport for MBD 3D PDF (C#)](Set_Independent_Viewport_for_MBD_3D_PDF_Example_CSharp.htm)  
[Set Independent Viewport for MBD 3D PDF (VB.NET)](Set_Independent_Viewport_for_MBD_3D_PDF_Example_VBNET.htm)  
[Set Independent Viewport for MBD 3D PDF (VBA)](Set_Independent_Viewport_for_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)
