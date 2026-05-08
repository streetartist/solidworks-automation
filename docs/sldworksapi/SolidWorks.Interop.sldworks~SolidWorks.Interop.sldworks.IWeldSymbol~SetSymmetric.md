# SetSymmetric Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~SetSymmetric`

Sets whether this weld symbol is a symmetric weld.
Sets whether this weld symbol is a symmetric weld.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSymmetric( _
   ByVal Symmetric As System.Integer _
) As System.Boolean
```

```

Dim instance As IWeldSymbol
Dim Symmetric As System.Integer
Dim value As System.Boolean
 
value = instance.SetSymmetric(Symmetric)
```

```

System.bool SetSymmetric( 
   System.int Symmetric
)
```

```

System.bool SetSymmetric( 
   System.int Symmetric
) 
```

#### Parameters

*Symmetric*
:   Value indicating whether this should be a symmetric weld, and if not, whether the dashed line is above or below the horizontal line as defined in [swWeldSymbolSymmetric\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldSymbolSymmetric_e.html)

Remarks

To get whether a weld symbol is a symmetric weld, use [IWeldSymbol::GetSymmetric](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol~GetSymmetric.md).

Example

See the [IWeldSymbol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IWeldSymbol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol.md)  
[IWeldSymbol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldSymbol_members.md)
