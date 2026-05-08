# NoOutline Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~NoOutline`

Gets or sets whether to show an outline in the detail view.
Gets or sets whether to show an outline in the detail view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NoOutline As System.Boolean
```

```

Dim instance As IDetailCircle
Dim value As System.Boolean
 
instance.NoOutline = value
 
value = instance.NoOutline
```

```

System.bool NoOutline {get; set;}
```

```

property System.bool NoOutline {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to not show an outline in the detail view, false to show an outline in the detail view

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
[IDetailCircle::HasFullOutline Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~HasFullOutline.md)  
[IDetailCircle::SetFullOutline Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~SetFullOutline.md)  
[IDetailCircle::JaggedOutline Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~JaggedOutline.md)
