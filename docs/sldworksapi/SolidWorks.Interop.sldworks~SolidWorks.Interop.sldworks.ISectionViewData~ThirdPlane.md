# ThirdPlane Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ThirdPlane`

Gets or sets the section plane for the third section of the section view for the part or assembly.
Gets or sets the section plane for the third section of the section view for the part or assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ThirdPlane As System.Object
```

```

Dim instance As ISectionViewData
Dim value As System.Object
 
instance.ThirdPlane = value
 
value = instance.ThirdPlane
```

```

System.object ThirdPlane {get; set;}
```

```

property System.Object^ ThirdPlane {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) or [planar face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

To select the section plane for the third section, specify a mark of 4 for [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

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
[ISectionViewData::GetFirstPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetFirstPlaneParameters.md)  
[ISectionViewData::GetSecondPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetSecondPlaneParameters.md)  
[ISectionViewData::GetThirdPlaneParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~GetThirdPlaneParameters.md)  
[ISectionViewData::FirstPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~FirstPlane.md)  
[ISectionViewData::SecondPlane Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SecondPlane.md)
