# HatchType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch~HatchType`

Gets or sets the type of this face hatch.
Gets or sets the type of this face hatch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property HatchType As System.Integer
```

```

Dim instance As IFaceHatch
Dim value As System.Integer
 
instance.HatchType = value
 
value = instance.HatchType
```

```

System.int HatchType {get; set;}
```

```

property System.int HatchType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of face hatch as defined in [swAreaHatchFillStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAreaHatchFillStyle_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaceHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch.md)  
[IFaceHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaceHatch_members.md)
