# EditMate2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate2`

Obsolete. Superseded by IAssemblyDoc::EditMate3.
Obsolete. Superseded by [IAssemblyDoc::EditMate3.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate3.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditMate2( _
   ByVal MateTypeFromEnum As System.Integer, _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal DistanceAbsUpperLimit As System.Double, _
   ByVal DistanceAbsLowerLimit As System.Double, _
   ByVal GearRatioNumerator As System.Double, _
   ByVal GearRatioDenominator As System.Double, _
   ByVal Angle As System.Double, _
   ByVal AngleAbsUpperLimit As System.Double, _
   ByVal AngleAbsLowerLimit As System.Double, _
   ByRef ErrorStatus As System.Integer _
) 
```

```

Dim instance As IAssemblyDoc
Dim MateTypeFromEnum As System.Integer
Dim AlignFromEnum As System.Integer
Dim Flip As System.Boolean
Dim Distance As System.Double
Dim DistanceAbsUpperLimit As System.Double
Dim DistanceAbsLowerLimit As System.Double
Dim GearRatioNumerator As System.Double
Dim GearRatioDenominator As System.Double
Dim Angle As System.Double
Dim AngleAbsUpperLimit As System.Double
Dim AngleAbsLowerLimit As System.Double
Dim ErrorStatus As System.Integer
 
instance.EditMate2(MateTypeFromEnum, AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, GearRatioNumerator, GearRatioDenominator, Angle, AngleAbsUpperLimit, AngleAbsLowerLimit, ErrorStatus)
```

```

void EditMate2( 
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.double GearRatioNumerator,
   System.double GearRatioDenominator,
   System.double Angle,
   System.double AngleAbsUpperLimit,
   System.double AngleAbsLowerLimit,
   out System.int ErrorStatus
)
```

```

void EditMate2( 
   System.int MateTypeFromEnum,
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.double GearRatioNumerator,
   System.double GearRatioDenominator,
   System.double Angle,
   System.double AngleAbsUpperLimit,
   System.double AngleAbsLowerLimit,
   [Out] System.int ErrorStatus
) 
```

#### Parameters

*MateTypeFromEnum*
:   Type of mate as defined in [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html)

*AlignFromEnum*
:   Type of alignment desired as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)

*Flip*
:   True to flip the component, false to not

*Distance*
:   Distance value to use with distance or limit mates

*DistanceAbsUpperLimit*
:   Absolute maximum distance allowed

*DistanceAbsLowerLimit*
:   Absolute minimum distance allowed

*GearRatioNumerator*
:   Gear ratio numerator value for gear mates

*GearRatioDenominator*
:   Gear ratio denominator value for gear mates

*Angle*
:   Angle value to use with angle mates

*AngleAbsUpperLimit*
:   Absolute maximum angle allowed

*AngleAbsLowerLimit*
:   Absolute minimum angle allowed

*ErrorStatus*
:   Success or error as defined by [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

Remarks

The first selection should be the two items that are mated (that is, two faces, edge and face, and so on), and the third selection should be the mate feature to be edited. The mate feature must be selected last. The two mated items must be selected with a selection mark of 1. See [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for details on using selection marks.

If mateType is swMateDISTANCE or swMateANGLE when the mate is applied to the closest position that meets the mate condition specified by distance or angle, then setting flip to True moves the assembly to the other possible mate position.

This method does not support editing **Inplace** mates.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddMate3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate3.md)
