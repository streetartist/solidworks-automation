# IMBD3DPdfData Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData`

Gains access to the details for publishing a SOLIDWORKS MBD 3D PDF.
Gains access to the details for publishing a SOLIDWORKS MBD 3D PDF.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface IMBD3DPdfData 
```

```

Dim instance As IMBD3DPdfData
```

```

public interface IMBD3DPdfData 
```

```

public interface class IMBD3DPdfData 
```

Remarks

SOLIDWORKS Model Based Definition (MBD) is an integrated drawingless manufacturing solution for SOLIDWORKS.

This interface and its methods and properties require that the SOLDWORKS MBD add-in be loaded. ([ISldWorks::LoadAddIn](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.md))

The MBD3DPdfData object corresponds to the SOLIDWORKS MBD **Publish to 3D PDF** PropertyManager page.

Typical steps for generating a SOLIDWORKS MBD 3D PDF using the SOLIDWORKS API are:

1. Get the MBD3DPdfData object using [IModelDocExtension::GetMBD3DPdfData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMBD3DPdfData.md).
2. Set the path and file name of the SOLIDWORKS MBD 3D PDF theme using [IMBD3DPdfData::ThemeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md).
3. Get standard and custom views using [IMBD3DPdfData::GetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetStandardViews.md) and [IMBD3DPdfData::GetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetMoreViews.md).
4. Set standard and custom views using [IMBD3DPdfData::SetStandardViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetStandardViews.md) and [IMBD3DPdfData::SetMoreViews](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~SetMoreViews.md).
5. Get and set text and custom properties in the theme using [IMBD3DPdfData::GetTextCustomProperties](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~GetTextAndCustomProperties.md) and [ITextAndCustomProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.md).
6. Set the path for the SOLIDWORKS MBD 3D PDF using [IMBD3DPdfData::FilePath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~FilePath.md).
7. Generate the SOLIDWORKS MBD 3D PDF using [IModelDocExtension::PublishTo3DPDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md).

See the SOLIDWORKS Help for details about MBD.

Example

See the [IMBDSTEP242Data](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBDSTEP242Data.md) examples.

Example

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)  
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)  
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)  
[Export BOM's Second Column to BOM Table Area (C#)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_CSharp.htm)  
[Export BOM's Second Column to BOM Table Area (VB.NET)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VBNET.htm)  
[Export BOM's Second Column to BOM Table Area (VBA)](Export_BOM's_Second_Column_to_BOM_Table_Area_Example_VB.htm)  
[Fire Notification When Publishing Part to MBD 3D PDF (VB.NET)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VBNET.htm)  
[Fire Notification When Publishing Part to MBD 3D PDF (C#)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_CSharp.htm)  
[Fire Notification When Publishing Part to MBD 3D PDF (VBA)](Fire_Notification_When_Publishing_Part_to_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMBD3DPdfData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)  
[IModelDocExtension::PublishTo3DPDF Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md)  
[IView3D Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView3D.md)
