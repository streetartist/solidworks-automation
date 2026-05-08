# ZonalSection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection`

Gets or sets whether the section method is zonal or planar.
Gets or sets whether the section method is zonal or planar.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ZonalSection As System.Boolean
```

```

Dim instance As ISectionViewData
Dim value As System.Boolean
 
instance.ZonalSection = value
 
value = instance.ZonalSection
```

```

System.bool ZonalSection {get; set;}
```

```

property System.bool ZonalSection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the section method is zonal, false if it is planar

Remarks

Call [ISectionViewData::SectionedZones](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionedZones.md) to specify the section zones.

ISectionViewData::ZonalSection must be true for [transparent sectioning](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~TransparentSection.md).

**NOTE:** Zonal sectioning is only supported on graphics cards that support OpenGL 4.0; zonal sectioning is not supported in Software Only OpenGL.

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
