# TransparentSection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection`

Gets or sets whether transparent sectioning is enabled in this section view.
Gets or sets whether transparent sectioning is enabled in this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransparentSection As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.TransparentSection = value
 
value = instance.TransparentSection
```

```

System.bool TransparentSection {get; set;}
```

```

property System.bool TransparentSection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if transparent sectioning is enabled, false if not

Remarks

You can specify which sectioned bodies in multibody parts or which sectioned components in assemblies to transparently section. See [ISectionViewData::TransparencyList](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyList.md) and [ISectionViewData::SectionTransparentItemsTransparent](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionTransparentItemsTransparent.md).

ISectionViewData::TransparentSection is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.md) is true.

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
[ISectionViewData::TransparencyValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparencyValue.md)  
[ISectionViewData::SelectiveSection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SelectiveSection.md)
