# SectionProfileCenter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter`

Gets or sets the center point of the section profile of the spring.
Gets or sets the center point of the section profile of the spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SectionProfileCenter As MathPoint
```

```

Dim instance As ISpring
Dim value As MathPoint
 
instance.SectionProfileCenter = value
 
value = instance.SectionProfileCenter
```

```

MathPoint SectionProfileCenter {get; set;}
```

```

property MathPoint^ SectionProfileCenter {
   MathPoint^ get();
   void set (    MathPoint^ value);
}
```

#### Property Value

[Center point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathPoint.md)

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
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.md)
