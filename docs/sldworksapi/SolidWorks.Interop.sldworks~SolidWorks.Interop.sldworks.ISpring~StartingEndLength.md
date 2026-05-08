# StartingEndLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndLength`

Gets or sets the starting end length of a torsion spring.
Gets or sets the starting end length of a torsion spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property StartingEndLength As System.Double
```

```

Dim instance As ISpring
Dim value As System.Double
 
instance.StartingEndLength = value
 
value = instance.StartingEndLength
```

```

System.double StartingEndLength {get; set;}
```

```

property System.double StartingEndLength {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Starting end length

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)  
[ISpring::EndingEndLength Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndLength.md)  
[ISpring::EndingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~EndingEndType.md)  
[ISpring::StartingEndType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~StartingEndType.md)
