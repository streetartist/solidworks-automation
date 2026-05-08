# GetLineCount Method (ISFSymbol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineCount`

Gets number of line items in this surface finish symbol.
Gets number of line items in this surface finish symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetLineCount() As System.Integer
```

```

Dim instance As ISFSymbol
Dim value As System.Integer
 
value = instance.GetLineCount()
```

```

System.int GetLineCount()
```

```

System.int GetLineCount(); 
```

#### Return Value

Number of lines

Remarks

Call this method before calling [ISFSymbol::GetLineAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineAtIndex.md) and [ISFSymbol::IGetLineAtIndex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol~GetLineAtIndex.md) to get the number of lines in this surface finish symbol.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISFSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol.md)  
[ISFSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISFSymbol_members.md)
