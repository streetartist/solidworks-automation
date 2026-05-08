# WatermarkBehindGeometry Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkBehindGeometry`

Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly.
Gets or sets whether to place this note, specified to be a watermark, behind the geometry in a part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WatermarkBehindGeometry As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.WatermarkBehindGeometry = value
 
value = instance.WatermarkBehindGeometry
```

```

System.bool WatermarkBehindGeometry {get; set;}
```

```

property System.bool WatermarkBehindGeometry {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to place this note behind the geometry in a part or assembly, false to place this note in front of the geometry in a part or assembly

Remarks

This property is only available when [INote::WatermarkNote](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote.md) is true.

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
[INote::WatermarkTransparencyLevel Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.md)
