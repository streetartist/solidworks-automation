# WatermarkNote Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkNote`

Gets or sets whether the note is a watermark in a part or assembly.
Gets or sets whether the note is a watermark in a part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property WatermarkNote As System.Boolean
```

```

Dim instance As INote
Dim value As System.Boolean
 
instance.WatermarkNote = value
 
value = instance.WatermarkNote
```

```

System.bool WatermarkNote {get; set;}
```

```

property System.bool WatermarkNote {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the note is a watermark in a part or assembly, false if not

Remarks

To add a watermark to a part or assembly document:

1. Open a part or assembly document.
2. Expand the **Annotations** folder in the FeatureManager design tree.
3. Right click **Notes Area** and click **Activate**.
4. Click **Insert > Annotations > Note**
5. Place the note in the graphics area, type the note text, and click **OK** in the Notes PropertyManager page.
6. Right-click the note and click **Watermark**.

Use [ISheet::BehindSheet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~BehindSheet.md) to place a note on the sheet format behind a drawing sheet, which allows you to display the note as watermark in a drawing.

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
[INote::WatermarkTransparencyLevel Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.INote~WatermarkTransparencyLevel.md)
