# SetFieldWeld Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetFieldWeld`

Sets the field or site weld property of this weld symbol.
Sets the field or site weld property of this weld symbol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetFieldWeld( _
   ByVal FieldWeld As System.Integer _
) As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim FieldWeld As System.Integer
Dim value As System.Boolean
 
value = instance.SetFieldWeld(FieldWeld)
```

```

System.bool SetFieldWeld( 
   System.int FieldWeld
)
```

```

System.bool SetFieldWeld( 
   System.int FieldWeld
) 
```

#### Parameters

*FieldWeld*
:   Value indicating whether this is to be a field or site weld, and, if so, whether the flag points up or down as defined in [swWeldSymbolField\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolField_e.html)

#### Return Value

True if the field or site weld setting is set successfully, false if not

Remarks

To retrieve the field or site weld property of a weld symbol, use [IWeldSymbol::GetFieldWeld](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetFieldWeld.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
