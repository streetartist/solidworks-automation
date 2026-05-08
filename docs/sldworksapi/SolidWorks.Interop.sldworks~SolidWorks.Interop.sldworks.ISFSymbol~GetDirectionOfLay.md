# GetDirectionOfLay Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetDirectionOfLay`

Gets the direction of lay value for this surface finish symbol.
Gets the direction of lay value for this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDirectionOfLay() As System.Integer
```

```

Dim instance As ISFSymbol
Dim value As System.Integer
 
value = instance.GetDirectionOfLay()
```

```

System.int GetDirectionOfLay()
```

```

System.int GetDirectionOfLay(); 
```

#### Return Value

Direction of lay as defined in [swSFLaySym\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSFLaySym_e.html)

Remarks

To set the direction of lay value, use [ISFSymbol::SetDirectionOfLay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~SetDirectionOfLay.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
