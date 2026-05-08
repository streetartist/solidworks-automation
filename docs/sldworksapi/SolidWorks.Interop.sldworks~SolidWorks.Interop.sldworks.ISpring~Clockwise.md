# Clockwise Property (ISpring)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~Clockwise`

Gets or sets the direction of the coils of the spring.
Gets or sets the direction of the coils of the spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Clockwise As System.Boolean
```

```

Dim instance As ISpring
Dim value As System.Boolean
 
instance.Clockwise = value
 
value = instance.Clockwise
```

```

System.bool Clockwise {get; set;}
```

```

property System.bool Clockwise {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to set the direction of the coils of the spring clockwise, false to set their direction counter-clockwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)
