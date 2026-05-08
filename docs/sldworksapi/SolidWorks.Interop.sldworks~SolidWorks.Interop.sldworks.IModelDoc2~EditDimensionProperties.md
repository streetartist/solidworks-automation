# EditDimensionProperties Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDimensionProperties`

Obsolete. Superseded by IModelDoc2::EditDimensionProperties3.
Obsolete. Superseded by [IModelDoc2::EditDimensionProperties3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditDimensionProperties3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EditDimensionProperties( _
   ByVal TolType As System.Integer, _
   ByVal TolMax As System.Double, _
   ByVal TolMin As System.Double, _
   ByVal TolMaxFit As System.String, _
   ByVal TolMinFit As System.String, _
   ByVal UseDocPrec As System.Boolean, _
   ByVal Precision As System.Integer, _
   ByVal ArrowsIn As System.Integer, _
   ByVal UseDocArrows As System.Boolean, _
   ByVal Arrow1 As System.Integer, _
   ByVal Arrow2 As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim TolType As System.Integer
Dim TolMax As System.Double
Dim TolMin As System.Double
Dim TolMaxFit As System.String
Dim TolMinFit As System.String
Dim UseDocPrec As System.Boolean
Dim Precision As System.Integer
Dim ArrowsIn As System.Integer
Dim UseDocArrows As System.Boolean
Dim Arrow1 As System.Integer
Dim Arrow2 As System.Integer
Dim value As System.Boolean
 
value = instance.EditDimensionProperties(TolType, TolMax, TolMin, TolMaxFit, TolMinFit, UseDocPrec, Precision, ArrowsIn, UseDocArrows, Arrow1, Arrow2)
```

```

System.bool EditDimensionProperties( 
   System.int TolType,
   System.double TolMax,
   System.double TolMin,
   System.string TolMaxFit,
   System.string TolMinFit,
   System.bool UseDocPrec,
   System.int Precision,
   System.int ArrowsIn,
   System.bool UseDocArrows,
   System.int Arrow1,
   System.int Arrow2
)
```

```

System.bool EditDimensionProperties( 
   System.int TolType,
   System.double TolMax,
   System.double TolMin,
   System.String^ TolMaxFit,
   System.String^ TolMinFit,
   System.bool UseDocPrec,
   System.int Precision,
   System.int ArrowsIn,
   System.bool UseDocArrows,
   System.int Arrow1,
   System.int Arrow2
) 
```

#### Parameters

*TolType*

*TolMax*

*TolMin*

*TolMaxFit*

*TolMinFit*

*UseDocPrec*

*Precision*

*ArrowsIn*

*UseDocArrows*

*Arrow1*

*Arrow2*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
