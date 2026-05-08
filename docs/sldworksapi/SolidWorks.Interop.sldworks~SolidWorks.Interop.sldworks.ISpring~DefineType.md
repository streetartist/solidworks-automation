# DefineType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~DefineType`

Gets or sets how the number of revolutions, pitch, and height of the spring are defined.
Gets or sets how the number of revolutions, pitch, and height of the spring are defined.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DefineType As System.Integer
```

```

Dim instance As ISpring
Dim value As System.Integer
 
instance.DefineType = value
 
value = instance.DefineType
```

```

System.int DefineType {get; set;}
```

```

property System.int DefineType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

How the number of revolutions, pitch, and height  of spring are defined as defined in [swSpringDefineType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringDefineType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)  
[ISpring::SpringType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SpringType.md)
