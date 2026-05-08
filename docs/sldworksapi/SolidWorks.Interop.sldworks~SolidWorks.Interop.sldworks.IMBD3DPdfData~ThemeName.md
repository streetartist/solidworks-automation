# ThemeName Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName`

Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF.
Gets or sets the path and file name of the theme for this SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThemeName As System.String
```

```

Dim instance As IMBD3DPdfData
Dim value As System.String
 
instance.ThemeName = value
 
value = instance.ThemeName
```

```

System.string ThemeName {get; set;}
```

```

property System.String^ ThemeName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Path and file name of the theme

Remarks

You can also get or set the SOLIDWORKS MBD 3D PDF path for a theme using:

- SOLIDWORKS API. Call:
  - [ISldWorks::GetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.md)(swUserPreferenceStringValue\_e.swFileLocationsThemeFolder) or
  - [ISldWorks::SetUserPreferenceStringValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetUserPreferenceStringValue.md)(swUserPreferenceStringValue\_e.swFileLocationsThemeFolder, <V*alue*>)
- SOLIDWORKS user interface. Click **Tools > System Options > File Locations > 3D PDF Themes** in **Show folders for**.

Example

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md) examples.

Example

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)  
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)  
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md)  
[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)  
[IMBD3DPdfData::SetIndependentViewPort Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetIndependentViewPort.md)
