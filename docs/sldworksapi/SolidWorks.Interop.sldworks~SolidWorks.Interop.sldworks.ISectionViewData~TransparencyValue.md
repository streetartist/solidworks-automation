# TransparencyValue Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyValue`

Gets or sets the level of transparency for the specified transparently sectioned bodies in the multibody part or the specified transparently sectioned components in the assembly in this section view.
Gets or sets the level of transparency for the specified transparently sectioned bodies in the multibody part or the specified transparently sectioned components in the assembly in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransparencyValue As System.Double
```

```

Dim instance As ISectionViewData
Dim value As System.Double
 
instance.TransparencyValue = value
 
value = instance.TransparencyValue
```

```

System.double TransparencyValue {get; set;}
```

```

property System.double TransparencyValue {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.01 (least transparent) to 1.0 (most transparent)

Remarks

To specify the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section, call [ISectionViewData::TransparencyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.md) and [ISectionViewData::SectionTransparentItemsTransparent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent.md).

This property is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.md) and [ISectionViewData::TransparentSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.md) are true.

Example

[Selectively and Transparently Section a Section View (C#)](Selectively_and_Transparently_Section_a_Section_View_Example_CSharp.htm)  
[Selectively and Transparently Section a Section View (VB.NET)](Selectively_and_Transparently_Section_a_Section_View_Example_VBNET.htm)  
[Selectively and Transparently Section a Section View (VBA)](Selectively_and_Transparently_Section_a_Section_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISectionViewData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData.md)  
[ISectionViewData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData_members.md)
