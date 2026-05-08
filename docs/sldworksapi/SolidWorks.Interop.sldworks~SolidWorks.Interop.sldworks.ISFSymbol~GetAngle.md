# GetAngle Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetAngle`

Gets the angle of this surface finish symbol.
Gets the angle of this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAngle() As System.Double
```

```

Dim instance As ISFSymbol
Dim value As System.Double
 
value = instance.GetAngle()
```

```

System.double GetAngle()
```

```

System.double GetAngle(); 
```

#### Return Value

Symbol angle

Remarks

See [ISFSymbol::Orientation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~Orientation.md) and [ISFSymbol::SetAngle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetAngle.md) for details on how to set the angle of a surface finish symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
