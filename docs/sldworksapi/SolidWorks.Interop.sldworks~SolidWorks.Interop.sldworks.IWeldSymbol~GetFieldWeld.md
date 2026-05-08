# GetFieldWeld Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetFieldWeld`

Gets the field or site weld property of this weld symbol.
Gets the field or site weld property of this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFieldWeld() As System.Integer
```

```

Dim instance As IWeldSymbol
Dim value As System.Integer
 
value = instance.GetFieldWeld()
```

```

System.int GetFieldWeld()
```

```

System.int GetFieldWeld(); 
```

#### Return Value

Value indicating whether this is a field or site weld, and, if so, whether the flag points up or down as defined in [swWeldSymbolField\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolField_e.html)

Remarks

To set the field or site weld property of a weld symbol, use [IWeldSymbol::SetFieldWeld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetFieldWeld.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
