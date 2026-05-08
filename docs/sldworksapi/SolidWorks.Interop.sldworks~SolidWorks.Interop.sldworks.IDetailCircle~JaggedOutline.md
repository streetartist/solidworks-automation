# JaggedOutline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~JaggedOutline`

Gets or sets whether to show a jagged outline in the detail view.
Gets or sets whether to show a jagged outline in the detail view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property JaggedOutline As System.Boolean
```

```

Dim instance As IDetailCircle
Dim value As System.Boolean
 
instance.JaggedOutline = value
 
value = instance.JaggedOutline
```

```

System.bool JaggedOutline {get; set;}
```

```

property System.bool JaggedOutline {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show a jagged outline in the detail view, false to not (see **Remarks**)

Remarks

This property is only available when [IDetailCircle::NoOutline](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline.md) is false.

To set the intensity of the jagged outline, call [IDetailCircle::ShapeIntensity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~ShapeIntensity.md).

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
