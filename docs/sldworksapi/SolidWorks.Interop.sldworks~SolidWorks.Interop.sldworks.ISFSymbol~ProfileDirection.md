# ProfileDirection Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileDirection`

Gets or sets the profile direction of this surface finish symbol.
Gets or sets the profile direction of this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileDirection As System.Integer
```

```

Dim instance As ISFSymbol
Dim value As System.Integer
 
instance.ProfileDirection = value
 
value = instance.ProfileDirection
```

```

System.int ProfileDirection {get; set;}
```

```

property System.int ProfileDirection {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Profile direction as defined by [swSFProfileDirection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSFProfileDirection_e.html)

Remarks

If this property sets swSFProfileDirection\_e.swSFProfileDirectionDefinedAngle, then use [ISFSymbol::ProfileAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~ProfileAngle.md) to specify the angle.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
