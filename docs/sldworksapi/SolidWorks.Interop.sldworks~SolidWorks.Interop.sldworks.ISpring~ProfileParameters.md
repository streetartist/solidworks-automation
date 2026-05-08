# ProfileParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileParameters`

Gets or sets the section profile parameters for the spring.
Gets or sets the section profile parameters for the spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileParameters As System.Object
```

```

Dim instance As ISpring
Dim value As System.Object
 
instance.ProfileParameters = value
 
value = instance.ProfileParameters
```

```

System.object ProfileParameters {get; set;}
```

```

property System.Object^ ProfileParameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of three doubles (see Remarks)

Remarks

The values of the array depend on the type of profile.

|  |  |
| --- | --- |
| **Type of profile** | **Values** |
| Circular | [ diameter, 0, 0 ] |
| Square | [ height, width ] |
| Trapezoid | [ height, bottom, top ] |

Use [ISpring::ProfileType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ProfileType.md) to set the spring's type of profile.

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
