# SectionTransparentItemsTransparent Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent`

Gets or sets whether the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view.
Gets or sets whether the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SectionTransparentItemsTransparent As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.SectionTransparentItemsTransparent = value
 
value = instance.SectionTransparentItemsTransparent
```

```

System.bool SectionTransparentItemsTransparent {get; set;}
```

```

property System.bool SectionTransparentItemsTransparent {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the specified sectioned bodies in the multibody part or the specified sectioned components in the assembly are transparently sectioned in this section view; false if all sectioned bodies in the multibody part or all sectioned components in the assembly, except for the specified sectioned bodies or the specified sectioned components, are transparently sectioned in this section view (see **Remarks**)

Remarks

Before calling this property, call [ISectionViewData::TransparentyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.md) to specify the sectioned bodies in the multibody part or the sectioned components in the assembly to transparently section. Call [ISectionViewData::TransparencyValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyValue.md) to set the level of transparency of the sectioned bodies in the multibody part or the sectioned components in the assembly.

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
