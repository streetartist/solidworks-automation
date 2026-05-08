# SectionProfile Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile`

Gets or sets the section profile for the spring.
Gets or sets the section profile for the spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SectionProfile As Body2
```

```

Dim instance As ISpring
Dim value As Body2
 
instance.SectionProfile = value
 
value = instance.SectionProfile
```

```

Body2 SectionProfile {get; set;}
```

```

property Body2^ SectionProfile {
   Body2^ get();
   void set (    Body2^ value);
}
```

#### Property Value

[Body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md) (see **Remarks**)

Remarks

The profile refers to the body associated with a circular edge that determines the base diameter of the spring. For example, to create a spring on a circular sketch, use [ISketch::GetContourEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.md) or [ISketch::IGetContours](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges.md) and [IEdge::GetBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge~GetBody.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)  
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.md)  
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.md)  
[ISpring::ProfileParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.md)  
[ISpring::ProfileType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.md)  
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.md)
