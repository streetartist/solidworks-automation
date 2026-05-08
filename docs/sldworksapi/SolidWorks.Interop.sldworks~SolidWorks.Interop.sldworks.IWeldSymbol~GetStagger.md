# GetStagger Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetStagger`

Gets whether this weld symbol is a stagger weld.
Gets whether this weld symbol is a stagger weld.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetStagger() As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim value As System.Boolean
 
value = instance.GetStagger()
```

```

System.bool GetStagger()
```

```

System.bool GetStagger(); 
```

#### Return Value

True if this is a stagger weld, false if not

Remarks

To set the weld symbol to a stagger weld, use [IWeldSymbol::SetStagger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetStagger.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
