# SpringType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~SpringType`

Gets or sets the type of parameters that define the spring.
Gets or sets the type of parameters that define the spring.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SpringType As System.Integer
```

```

Dim instance As ISpring
Dim value As System.Integer
 
instance.SpringType = value
 
value = instance.SpringType
```

```

System.int SpringType {get; set;}
```

```

property System.int SpringType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of parameters that define the spring as defined in [swSpringType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSpringType_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISpring Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring.md)  
[ISpring Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring_members.md)  
[ISpring::DefineType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISpring~DefineType.md)
