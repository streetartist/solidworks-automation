# IsCustomProperty Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty~IsCustomProperty`

Gets whether this is text or a custom property in a theme for a SOLIDWORKS MBD 3D PDF.
Gets whether this is text or a custom property in a [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) for a [SOLIDWORKS MBD 3D PDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsCustomProperty As System.Boolean
```

```

Dim instance As ITextAndCustomProperty
Dim value As System.Boolean
 
value = instance.IsCustomProperty
```

```

System.bool IsCustomProperty {get;}
```

```

property System.bool IsCustomProperty {
   System.bool get();
}
```

#### Property Value

True if a custom property, false if text

Remarks

This property corresponds to a **Text Field** or **Custom Property Field** group box in a theme.

Example

[Publish Text and Custom Properties from Theme to MBD 3D PDF (C#)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_CSharp.htm)  
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VB.NET)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VBNET.htm)  
[Publish Text and Custom Properties from Theme to MBD 3D PDF (VBA)](Publish_Text_and_Custom_Properties_from_Theme_to_MBD_3D_PDF_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITextAndCustomProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty.md)  
[ITextAndCustomProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty_members.md)
