# HatchScope Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~HatchScope`

Gets or sets the scope for this face hatch.
Gets or sets the scope for this face hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HatchScope As System.Integer
```

```

Dim instance As IFaceHatch
Dim value As System.Integer
 
instance.HatchScope = value
 
value = instance.HatchScope
```

```

System.int HatchScope {get; set;}
```

```

property System.int HatchScope {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Hatch scope as defined in [swAreaHatchingScope\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAreaHatchingScope_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
