# SetIndicator Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~SetIndicator`

Sets the indicator border type, tolerance type, and datum at the specified indicator index on the right side of this Gtol frame.
Sets the indicator border type, tolerance type, and datum at the specified indicator index on the right side of this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetIndicator( _
   ByVal IndicatorIndex As System.Integer, _
   ByVal BorderType As System.Integer, _
   ByVal TolType As System.Integer, _
   ByVal Datum As System.String _
) As System.Boolean
```

```

Dim instance As IGtolFrame
Dim IndicatorIndex As System.Integer
Dim BorderType As System.Integer
Dim TolType As System.Integer
Dim Datum As System.String
Dim value As System.Boolean
 
value = instance.SetIndicator(IndicatorIndex, BorderType, TolType, Datum)
```

```

System.bool SetIndicator( 
   System.int IndicatorIndex,
   System.int BorderType,
   System.int TolType,
   System.string Datum
)
```

```

System.bool SetIndicator( 
   System.int IndicatorIndex,
   System.int BorderType,
   System.int TolType,
   System.String^ Datum
) 
```

#### Parameters

*IndicatorIndex*
:   One-based index of Gtol frame indicator to set

*BorderType*
:   Type of border as defined by [swGtolIndicatorBorderType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolIndicatorBorderType_e.html)

*TolType*
:   Tolerance type as defined by [swGtolGeomCharSymbol\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)

*Datum*
:   Datum feature symbol that refers to the BorderType

#### Return Value

True if indicator successfully set, false if not

Remarks

Before calling this method, use [IGtolFrame:GetIndicatorCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicatorCount.md) to determine IndicatorIndex.

TolType may be one of only swGtolGeomCharSymbol\_e.:

- swGcsANG
- swGcsPARALLEL
- swGcsPERP
- swGcsCIRCRUNOUT
- swGcsSYMMETRY

Example

See the [IGtolFrame](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtolFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame.md)  
[IGtolFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame_members.md)
