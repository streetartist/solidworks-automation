# GetFrameToleranceType Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtolFrame~GetFrameToleranceType`

Gets the tolerance type of this Gtol frame.
Gets the tolerance type of this Gtol frame.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFrameToleranceType( _
   ByRef TolType As System.Integer _
) As System.Boolean
```

```

Dim instance As IGtolFrame
Dim TolType As System.Integer
Dim value As System.Boolean
 
value = instance.GetFrameToleranceType(TolType)
```

```

System.bool GetFrameToleranceType( 
   out System.int TolType
)
```

```

System.bool GetFrameToleranceType( 
   [Out] System.int TolType
) 
```

#### Parameters

*TolType*
:   Tolerance type as defined by [swGtolGeomCharSymbol\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGtolGeomCharSymbol_e.html) (see **Remarks**)

#### Return Value

True if Gtol frame tolerance type successfully retrieved, false if not

Remarks

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
