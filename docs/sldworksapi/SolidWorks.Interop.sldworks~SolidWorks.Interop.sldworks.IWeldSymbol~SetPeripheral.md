# SetPeripheral Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetPeripheral`

Sets the peripheral property of this weld symbol.
Sets the peripheral property of this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPeripheral( _
   ByVal Peripheral As System.Boolean _
) As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim Peripheral As System.Boolean
Dim value As System.Boolean
 
value = instance.SetPeripheral(Peripheral)
```

```

System.bool SetPeripheral( 
   System.bool Peripheral
)
```

```

System.bool SetPeripheral( 
   System.bool Peripheral
) 
```

#### Parameters

*Peripheral*
:   True if a peripheral weld, false if not

#### Return Value

True if the peripheral weld setting is set successfully, false if not

Remarks

To retrieve the peripheral property of a weld symbol, use [IWeldSymbol::GetPeripheral](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetPeripheral.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
