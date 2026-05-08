# ReverseDirection Property (ISpring)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~ReverseDirection`

Gets or sets the direction of a compression, extension, or torsion spring.
Gets or sets the direction of a compression, extension, or torsion spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReverseDirection As System.Boolean
```

```

Dim instance As ISpring
Dim value As System.Boolean
 
instance.ReverseDirection = value
 
value = instance.ReverseDirection
```

```

System.bool ReverseDirection {get; set;}
```

```

property System.bool ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)
