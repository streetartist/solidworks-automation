# GetArcCount Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArcCount`

Gets the number of arcs in this surface finish symbol.
Gets the number of arcs in this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetArcCount() As System.Integer
```

```

Dim instance As ISFSymbol
Dim value As System.Integer
 
value = instance.GetArcCount()
```

```

System.int GetArcCount()
```

```

System.int GetArcCount(); 
```

#### Return Value

Number of arcs

Remarks

Call this method before calling [ISFSymbol::GetArcAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetArcAtIndex.md) and [ISFSymbol::IGetArcAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~IGetArcAtIndex.md) to find out the number of arcs in this surface finish symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
