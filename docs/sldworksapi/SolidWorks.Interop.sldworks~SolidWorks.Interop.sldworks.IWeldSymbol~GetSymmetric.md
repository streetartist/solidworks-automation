# GetSymmetric Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetSymmetric`

Gets whether this weld symbol is a symmetric weld.
Gets whether this weld symbol is a symmetric weld.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSymmetric() As System.Integer
```

```

Dim instance As IWeldSymbol
Dim value As System.Integer
 
value = instance.GetSymmetric()
```

```

System.int GetSymmetric()
```

```

System.int GetSymmetric(); 
```

#### Return Value

Value indicating whether this is a symmetric weld, and if not, whether the dashed line is above or below the horizontal line as defined in [swWeldSymbolSymmetric\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolSymmetric_e.html)

Remarks

To set a weld symbol to a symmetric weld, use [IWeldSymbol::SetSymmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetSymmetric.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
