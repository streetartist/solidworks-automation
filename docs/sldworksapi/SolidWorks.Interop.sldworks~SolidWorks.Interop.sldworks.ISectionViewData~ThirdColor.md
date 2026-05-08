# ThirdColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdColor`

Gets or sets the third color of the section view in this part or assembly.
Gets or sets the third color of the section view in this part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThirdColor As System.Integer
```

```

Dim instance As ISectionViewData
Dim value As System.Integer
 
instance.ThirdColor = value
 
value = instance.ThirdColor
```

```

System.int ThirdColor {get; set;}
```

```

property System.int ThirdColor {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Third RGB value of the color

Remarks

Use [ISectionViewData::ShowSectionCap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ShowSectionCap.md) to display the caps of section views and [ISectionView::KeepCapColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~KeepCapColor.md) to color them.

Example

[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)  
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)  
[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)  
[Get Section View Data (C#)](Get_Section_View_Data_Example_CSharp.htm)  
[Get Section View Data (VB.NET)](Get_Section_View_Data_Example_VBNET.htm)  
[Get Section View Data (VBA)](Get_Section_View_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)  
[ISectionViewData::FirstColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstColor.md)  
[ISectionViewData::SecondColor Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondColor.md)
