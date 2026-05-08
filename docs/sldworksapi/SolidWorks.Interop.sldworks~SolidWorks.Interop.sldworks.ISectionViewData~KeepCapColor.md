# KeepCapColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~KeepCapColor`

Gets or sets whether to color the caps of section views.
Gets or sets whether to color the caps of section views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property KeepCapColor As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.KeepCapColor = value
 
value = instance.KeepCapColor
```

```

System.bool KeepCapColor {get; set;}
```

```

property System.bool KeepCapColor {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to color the caps of section views, false to not (see **Remarks**)

Remarks

This property is valid only if [ISectionViewData::ShowSectionCap](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ShowSectionCap.md) is true and [ISectionViewData::GraphicsOnlySection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GraphicsOnlySection.md) is false.

Example

[Create Section View in Model (VBA)](Create_Section_View_in_Model_Example_VB.htm)  
[Create Section View in Model (VB.NET)](Create_Section_View_in_Model_Example_VBNET.htm)  
[Create Section View in Model (C#)](Create_Section_View_in_Model_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)
