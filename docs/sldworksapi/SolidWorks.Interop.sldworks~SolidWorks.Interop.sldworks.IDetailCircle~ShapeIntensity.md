# ShapeIntensity Property (IDetailCircle)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~ShapeIntensity`

Gets or sets the shape intensity of the jagged outline in the detail view.
Gets or sets the shape intensity of the jagged outline in the detail view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShapeIntensity As System.Integer
```

```

Dim instance As IDetailCircle
Dim value As System.Integer
 
instance.ShapeIntensity = value
 
value = instance.ShapeIntensity
```

```

System.int ShapeIntensity {get; set;}
```

```

property System.int ShapeIntensity {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Shape intensity of the jagged outline; valid range is 1 (most) to 5 (least) (see **Remarks**)

Remarks

This property is only available when [IDetailCircle::JaggedOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~JaggedOutline.md) is true and [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.md) is false.

Example

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)  
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)  
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)
