# ShowSectionCap Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ShowSectionCap`

Gets or sets whether to cap the section views.
Gets or sets whether to cap the section views.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowSectionCap As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.ShowSectionCap = value
 
value = instance.ShowSectionCap
```

```

System.bool ShowSectionCap {get; set;}
```

```

property System.bool ShowSectionCap {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to cap the section views, false to see inside the model (see **Remarks**)

Remarks

After setting this property to true, specify whether to color the caps by setting [ISectionViewData::KeepCapColor](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~KeepCapColor.md).

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
