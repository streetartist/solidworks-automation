# StartingEndType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndType`

Gets or sets the starting end type for either an extension spring or a torsion spring.
Gets or sets the starting end type for either an extension spring or a torsion spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartingEndType As System.Integer
```

```

Dim instance As ISpring
Dim value As System.Integer
 
instance.StartingEndType = value
 
value = instance.StartingEndType
```

```

System.int StartingEndType {get; set;}
```

```

property System.int StartingEndType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Starting end type as defined in [swSpringExtensionEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringExtensionEndType_e.html) for an extension spring or [swSpringTorsionEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringTorsionEndType_e.html) for a torsion spring

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)  
[ISpring::StartingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndLength.md)  
[ISpring::EndingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndLength.md)  
[ISpring::EndingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndType.md)
