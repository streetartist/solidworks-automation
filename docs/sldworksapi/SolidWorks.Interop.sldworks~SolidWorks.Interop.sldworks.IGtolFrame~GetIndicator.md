# GetIndicator Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetIndicator`

Gets the indicator border type, tolerance type, and datum at the specified indicator index for this Gtol frame.
Gets the indicator border type, tolerance type, and datum at the specified indicator index for this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIndicator( _
   ByVal IndicatorIndex As System.Integer, _
   ByRef BorderType As System.Integer, _
   ByRef TolType As System.Integer, _
   ByRef Datum As System.String _
) As System.Boolean
```

```

Dim instance As IGtolFrame
Dim IndicatorIndex As System.Integer
Dim BorderType As System.Integer
Dim TolType As System.Integer
Dim Datum As System.String
Dim value As System.Boolean
 
value = instance.GetIndicator(IndicatorIndex, BorderType, TolType, Datum)
```

```

System.bool GetIndicator( 
   System.int IndicatorIndex,
   out System.int BorderType,
   out System.int TolType,
   out System.string Datum
)
```

```

System.bool GetIndicator( 
   System.int IndicatorIndex,
   [Out] System.int BorderType,
   [Out] System.int TolType,
   [Out] System.String^ Datum
) 
```

#### Parameters

*IndicatorIndex*
:   One-based index of tolerance indicator to retrieve

*BorderType*
:   Type of border as defined by [swGtolIndicatorBorderType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolIndicatorBorderType_e.html)

*TolType*
:   Tolerance type as defined by [swGtolGeomCharSymbol\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)

*Datum*
:   Datum feature symbol that refers to the BorderType

#### Return Value

True if indicator successfully retrieved, false if not

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
