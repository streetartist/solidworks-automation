# Value Property (ITextAndCustomProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITextAndCustomProperty~Value`

Gets or sets the value of the text or custom property in a theme for a SOLIDWORKS MBD 3D PDF.
Gets or sets the value of the text or custom property in a [theme](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData~ThemeName.md) for a [SOLIDWORKS MBD 3D PDF](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMBD3DPdfData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Value As System.String
```

```

Dim instance As ITextAndCustomProperty
Dim value As System.String
 
instance.Value = value
 
value = instance.Value
```

```

System.string Value {get; set;}
```

```

property System.String^ Value {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Value

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
