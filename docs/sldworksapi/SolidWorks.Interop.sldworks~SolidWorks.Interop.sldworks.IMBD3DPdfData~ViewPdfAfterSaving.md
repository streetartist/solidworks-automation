# ViewPdfAfterSaving Property (IMBD3DPdfData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ViewPdfAfterSaving`

Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after publishing it.
Gets or sets whether to display this SOLIDWORKS MBD 3D PDF after [publishing it](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~PublishTo3DPDF.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ViewPdfAfterSaving As System.Boolean
```

```

Dim instance As IMBD3DPdfData
Dim value As System.Boolean
 
instance.ViewPdfAfterSaving = value
 
value = instance.ViewPdfAfterSaving
```

```

System.bool ViewPdfAfterSaving {get; set;}
```

```

property System.bool ViewPdfAfterSaving {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the SOLIDWORKS MBD 3D PDF after publishing it, false to not

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
