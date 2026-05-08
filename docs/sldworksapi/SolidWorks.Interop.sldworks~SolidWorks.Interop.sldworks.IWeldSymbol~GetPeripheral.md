# GetPeripheral Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetPeripheral`

Gets whether this is a peripheral weld.
Gets whether this is a peripheral weld.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetPeripheral() As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim value As System.Boolean
 
value = instance.GetPeripheral()
```

```

System.bool GetPeripheral()
```

```

System.bool GetPeripheral(); 
```

#### Return Value

True if a peripheral weld, false if not

Remarks

To set the peripheral property of a weld symbol, use [IWeldSymbol::SetPeripheral](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetPeripheral.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
