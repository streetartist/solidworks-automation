# WatermarkTransparencyLevel Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel`

Gets or sets the transparency level of a note specified to be a watermark.
Gets or sets the transparency level of a note specified to be a watermark.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WatermarkTransparencyLevel As System.Double
```

```

Dim instance As INote
Dim value As System.Double
 
instance.WatermarkTransparencyLevel = value
 
value = instance.WatermarkTransparencyLevel
```

```

System.double WatermarkTransparencyLevel {get; set;}
```

```

property System.double WatermarkTransparencyLevel {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 <= Level of transparency <= 1.0 (see **Remarks**)

Remarks

This property is only available when [INote::WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.md) is true.

A transparency level of 0.0 indicates that the transparency level is not set for the watermark; a transparency level of 1.0 indicates that the watermark is fully transparent.

Example

[Add Watermark to Part (C#)](Add_Watermark_to_Part_Example_CSharp.htm)  
[Add Watermark to Part (VB.NET)](Add_Watermark_to_Part_Example_VBNET.htm)  
[Add Watermark to Part (VBA)](Add_Watermark_to_Part_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[INote Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote.md)  
[INote Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote_members.md)  
[INote::WatermarkBehindGeometry Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry.md)
