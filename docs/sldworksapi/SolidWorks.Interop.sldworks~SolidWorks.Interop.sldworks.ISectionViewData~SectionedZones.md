# SectionedZones Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~SectionedZones`

Gets or sets the intersection zones that define how to section this section view.
Gets or sets the intersection zones that define how to section this section view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SectionedZones As System.Integer
```

```

Dim instance As ISectionViewData
Dim value As System.Integer
 
instance.SectionedZones = value
 
value = instance.SectionedZones
```

```

System.int SectionedZones {get; set;}
```

```

property System.int SectionedZones {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Intersection zones as defined in [swZonalSectionViewZones\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swZonalSectionViewZones_e.html) (see **Remarks**)

Remarks

In the SOLIDWORKS API, zones are defined by the intersections of the sectioning planes. This table describes the intersection zones and the enumerators to which they correspond.

| Number of sectioning planes | Zones | Intersection zones | swZonalSectionViewZones\_e enumerators |
| --- | --- | --- | --- |
| 1 | 1 | Front side of sectioning plane 1 | swZonalSectionViewZones\_swZonalSectionViewZone\_1 |
|  | 2 | Back side of sectioning plane 2 | swZonalSectionViewZones\_swZonalSectionViewZone\_2 |
| 2 | 1 | - Front side of sectioning plane 1 - Front side of sectioning plane 2 | swZonalSectionViewZones\_swZonalSectionViewZone\_1 |
|  | 2 | - Back side of sectioning plane 1 - Front side of sectioning plane 2 | swZonalSectionViewZones\_swZonalSectionViewZone\_2 |
|  | 3 | - Front side of sectioning plane 1 - Back side of sectioning plane 2 | swZonalSectionViewZones\_swZonalSectionViewZone\_3 |
|  | 4 | - Back side of sectioning plane 1 - Back side of sectioning plane 2 | swZonalSectionViewZones\_swZonalSectionViewZone\_4 |
| 3 | 1 | - Front side of sectioning plane 1 - Front side of sectioning plane 2 - Front side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_1 |
|  | 2 | - Back side of sectioning plane 1 - Front side of sectioning plane 2 - Front side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_2 |
|  | 3 | - Front side of sectioning plane 1 - Back side of sectioning plane 2 - Front side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_3 |
|  | 4 | - Back side of sectioning plane 1 - Back side of sectioning plane 2 - Front side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_4 |
|  | 5 | - Front side of sectioning plane 1 - Front side of sectioning plane 2 - Back side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_5 |
|  | 6 | - Back side of sectioning plane 1 - Front side of sectioning plane 2 - Back side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_6 |
|  | 7 | - Front side of sectioning plane 1 - Back side of sectioning plane 2 - Back side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_7 |
|  | 8 | - Back side of sectioning plane 1 - Back side of sectioning plane 2 - Back side of sectioning plane 3 | swZonalSectionViewZones\_swZonalSectionViewZone\_8 |

This property is only available if [ISectionViewData::ZonalSection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISectionViewData~ZonalSection.md) is true.

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
