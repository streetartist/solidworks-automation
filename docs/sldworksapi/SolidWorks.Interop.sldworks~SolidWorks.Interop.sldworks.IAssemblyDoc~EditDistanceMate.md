# EditDistanceMate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate`

Edits a distance mate.
Edits a distance mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub EditDistanceMate( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal DistanceAbsUpperLimit As System.Double, _
   ByVal DistanceAbsLowerLimit As System.Double, _
   ByVal FirstArcCondition As System.Integer, _
   ByVal SecondArcCondition As System.Integer, _
   ByRef ErrorStatus As System.Integer _
) 
```

```

Dim instance As IAssemblyDoc
Dim AlignFromEnum As System.Integer
Dim Flip As System.Boolean
Dim Distance As System.Double
Dim DistanceAbsUpperLimit As System.Double
Dim DistanceAbsLowerLimit As System.Double
Dim FirstArcCondition As System.Integer
Dim SecondArcCondition As System.Integer
Dim ErrorStatus As System.Integer
 
instance.EditDistanceMate(AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, FirstArcCondition, SecondArcCondition, ErrorStatus)
```

```

void EditDistanceMate( 
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.int FirstArcCondition,
   System.int SecondArcCondition,
   out System.int ErrorStatus
)
```

```

void EditDistanceMate( 
   System.int AlignFromEnum,
   System.bool Flip,
   System.double Distance,
   System.double DistanceAbsUpperLimit,
   System.double DistanceAbsLowerLimit,
   System.int FirstArcCondition,
   System.int SecondArcCondition,
   [Out] System.int ErrorStatus
) 
```

#### Parameters

*AlignFromEnum*
:   Type of alignment as defined in [swMateAlign\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateAlign_e.html)

*Flip*
:   True to flip the mate entities, false to not (see **Remarks**)

*Distance*
:   Distance value (see **Remarks**)

*DistanceAbsUpperLimit*
:   Absolute maximum distance value (see **Remarks**)

*DistanceAbsLowerLimit*
:   Absolute minimum distance value (see **Remarks**)

*FirstArcCondition*
:   First arc condition as defined in [swDistanceMateArcConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html); valid only for cylindrical distance mates (see **Remarks**)

*SecondArcCondition*
:   Second arc condition as defined in swDistanceMateArcConditions\_e; valid only for cylindrical distance mates (see **Remarks**)

*ErrorStatus*
:   Success or error as defined by [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

Remarks

Select these entities before calling this method:

- Two entities that define the distance mate (use [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md) with Data = Nothing)
- Distance mate feature (use [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) with Mark = 0)

If the mate is applied to the closest position that meets the mate condition specified by Distance, then setting Flip to true moves the components to the other possible mate position.

Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after calling this method.

See [IAssemblyDoc::AddDistanceMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.md) Remarks.

Example

[Add and Edit Distance Mate (VBA)](Add_and_Edit_Distance_Mate_Example_VB.htm)  
[Add and Edit Distance Mate (VB.NET)](Add_and_Edit_Distance_Mate_Example_VBNET.htm)  
[Add and Edit Distance Mate (C#)](Add_and_Edit_Distance_Mate_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::EditMate4 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditMate4.md)  
[IMate2::DistanceFirstArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition.md)  
[IMate2::DistanceSecondArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.md)
