# EditMate3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate3`

Obsolete. Superseded by IAssemblyDoc::EditMate4.
Obsolete. Superseded by [IAssemblyDoc::EditMate4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditMate3( _
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
   ByVal ForPositioningOnly As System.Boolean, _
   ByVal LockRotation As System.Boolean, _
   ByVal WidthMateOption As System.Integer, _
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
Dim ForPositioningOnly As System.Boolean
Dim LockRotation As System.Boolean
Dim WidthMateOption As System.Integer
Dim ErrorStatus As System.Integer
 
instance.EditMate3(MateTypeFromEnum, AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, GearRatioNumerator, GearRatioDenominator, Angle, AngleAbsUpperLimit, AngleAbsLowerLimit, ForPositioningOnly, LockRotation, WidthMateOption, ErrorStatus)
```

```

void EditMate3( 
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
   System.bool ForPositioningOnly,
   System.bool LockRotation,
   System.int WidthMateOption,
   out System.int ErrorStatus
)
```

```

void EditMate3( 
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
   System.bool ForPositioningOnly,
   System.bool LockRotation,
   System.int WidthMateOption,
   [Out] System.int ErrorStatus
) 
```

#### Parameters

*MateTypeFromEnum*
:   Type of mate as defined in [swMateType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateType_e.html)

*AlignFromEnum*
:   Type of alignment as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)

*Flip*
:   True to flip the component, false to not

*Distance*
:   Distance value; valid only if MateTypeFromEnum is swMateType\_e.swMateDISTANCE

*DistanceAbsUpperLimit*
:   Absolute maximum distance allowed; valid only if MateTypeFromEnum is swMateType\_e.swMateDISTANCE

*DistanceAbsLowerLimit*
:   Absolute minimum distance allowed; valid only if MateTypeFromEnum is swMateType\_e.swMateDISTANCE

*GearRatioNumerator*
:   Gear ratio numerator value; valid only if MateTypeFromEnum is swMateType\_e.swMateGEAR

*GearRatioDenominator*
:   Gear ratio denominator value; valid only if MateTypeFromEnum is swMateType\_e.swMateGEAR

*Angle*
:   Angle value; valid only if MateTypeFromEnum is swMateType\_e.swMateANGLE

*AngleAbsUpperLimit*
:   Absolute maximum angle allowed; valid only if MateTypeFromEnum is swMateType\_e.swMateANGLE

*AngleAbsLowerLimit*
:   Absolute minimum angle allowed; valid only if MateTypeFromEnum is swMateType\_e.swMateANGLE

*ForPositioningOnly*
:   True to only position the components according to the mating relationship and not return a mate, false to return a mate

*LockRotation*
:   True to lock component rotation, false to not

*WidthMateOption*
:   Width mate options as defined in [swMateWidthOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateWidthOptions_e.html); valid only if MateTypeFromEnum is swMateType\_e.swMateWIDTH

*ErrorStatus*
:   Success or error as defined by [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

Remarks

The first selections should be the two items that are mated (that is, two faces, edge and face, and so on), and the third selection should be the mate feature to be edited. The mate feature must be selected last. The two mated items must be selected with a selection mark of 1. See [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) or [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) for details on using selection marks.

If MateTypeFromEnum is swMateType\_e.swMateDISTANCE or swMateType\_e.swMateANGLE, and the mate is applied to the closest position that meets the mate condition specified by Distance or Angle, then setting Flip to true moves the assembly to the other possible mate position.

This method does not support editing **Inplace** mates.

Example

[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Edit Mate (VB.NET)](Edit_Mate_Example_VBNET.htm)  
[Edit Mate (C#)](Edit_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::AddMate5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.md)
