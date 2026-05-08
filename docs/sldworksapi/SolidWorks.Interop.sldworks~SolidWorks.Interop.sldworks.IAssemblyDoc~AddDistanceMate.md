# AddDistanceMate Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate`

Adds a distance mate to this assembly.
Adds a distance mate to this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddDistanceMate( _
   ByVal AlignFromEnum As System.Integer, _
   ByVal Flip As System.Boolean, _
   ByVal Distance As System.Double, _
   ByVal DistanceAbsUpperLimit As System.Double, _
   ByVal DistanceAbsLowerLimit As System.Double, _
   ByVal FirstArcCondition As System.Integer, _
   ByVal SecondArcCondition As System.Integer, _
   ByRef ErrorStatus As System.Integer _
) As Mate2
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
Dim value As Mate2
 
value = instance.AddDistanceMate(AlignFromEnum, Flip, Distance, DistanceAbsUpperLimit, DistanceAbsLowerLimit, FirstArcCondition, SecondArcCondition, ErrorStatus)
```

```

Mate2 AddDistanceMate( 
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

Mate2^ AddDistanceMate( 
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
:   True to flip mate entities, false to not (see **Remarks**)

*Distance*
:   Distance value (see **Remarks**)

*DistanceAbsUpperLimit*
:   Absolute maximum distance value (see **Remarks**)

*DistanceAbsLowerLimit*
:   Absolute minimum distance value (see **Remarks**)

*FirstArcCondition*
:   First arc condition as defined in [swDistanceMateArcConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html); valid only for cylindrical distance mates (see **Remarks**)

*SecondArcCondition*
:   Second arc condition as defined in swDistanceMateArcConditions\_e; valid only for cylindrical distance mates (see **Remarks**)

*ErrorStatus*
:   Success or error as defined by [swAddMateError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAddMateError_e.html)

#### Return Value

[IMate2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)

Remarks

To specify a distance mate without limits, set the DistanceAbsUpperLimit and DistanceAbsLowerLimit parameters equal to the Distance parameter.

If the mate is applied to the closest position that meets the mate condition specified by Distance, then setting Flip to true moves the components to the other possible mate position.

For cylindrical distance mates only, the following FirstArcCondition-to-SecondArcCondition distance combinations are possible:

| FirstArcCondition as defined in [swDistanceMateArcConditions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swDistanceMateArcConditions_e.html) | to | SecondArcCondition as defined in swDistanceMateArcConditions\_e |
| --- | --- | --- |
| swArcCondition\_Center |  | swArcCondition\_Center |
| swArcCondition\_Center |  | swArcCondition\_Minimum |
| swArcCondition\_Center |  | swArcCondition\_Maximum |
| swArcCondition\_Minimum |  | swArcCondition\_Center |
| swArcCondition\_Minimum |  | swArcCondition\_Minimum |
| swArcCondition\_Minimum |  | swArcCondition\_Maximum |
| swArcCondition\_Maximum |  | swArcCondition\_Center |
| swArcCondition\_Maximum |  | swArcCondition\_Minimum |
| swArcCondition\_Maximum |  | swArcCondition\_Maximum |

To add a distance mate:

1. Call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) and [ISelectionMgr::GetSelectedObject6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~GetSelectedObject6.md) to get each mate entity. (For cylindrical distance mates, the selections must be two cylindrical faces or one cylindrical face and one axis.)
2. Call [IModelDoc2::ClearSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ClearSelection2.md).
3. Call [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md) to select each entity.
4. Call this method.
5. Call [IModelDoc2::EditRebuild3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) after the mate is created.

If entities are not preselected, then ErrorStatus is swAddMateError\_e.swAddMateError\_IncorrectSelections, and nothing is returned.

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
[IAssemblyDoc::AddMate5 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddMate5.md)  
[IAssemblyDoc::EditDistanceMate Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~EditDistanceMate.md)  
[IMate2::DistanceFirstArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceFirstArcCondition.md)  
[IMate2::DistanceSecondArcCondition Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~DistanceSecondArcCondition.md)
