# ProfileType Property (ISpring)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType`

Gets or sets the section profile type of the spring.
Gets or sets the section profile type of the spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileType As System.Integer
```

```

Dim instance As ISpring
Dim value As System.Integer
 
instance.ProfileType = value
 
value = instance.ProfileType
```

```

System.int ProfileType {get; set;}
```

```

property System.int ProfileType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Section profile type as defined in [swSpringProfileType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringProfileType_e.html)

Remarks

Use [ISpring::ProfileParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters.md) to set the spring's section profile parameters.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)  
[ISpring::BaseProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~BaseProfile.md)  
[ISpring::GetProfilePoints Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~GetProfilePoints.md)  
[ISpring::SectionProfile Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfile.md)  
[ISpring::SectionProfileCenter Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SectionProfileCenter.md)
