# SetStagger Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetStagger`

Sets the stagger property of this weld symbol.
Sets the stagger property of this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStagger( _
   ByVal Stagger As System.Boolean _
) As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim Stagger As System.Boolean
Dim value As System.Boolean
 
value = instance.SetStagger(Stagger)
```

```

System.bool SetStagger( 
   System.bool Stagger
)
```

```

System.bool SetStagger( 
   System.bool Stagger
) 
```

#### Parameters

*Stagger*
:   True if this is a stagger weld, false if not

#### Return Value

True if the stagger weld setting is set successfully, false if not

Remarks

To retrieve the stagger property of a weld symbol, use [IWeldSymbol::GetStagger](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetStagger.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
