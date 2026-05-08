# SetPartialFilletParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~SetPartialFilletParameters`

Sets the properties of this partial edge fillet.
Sets the properties of this partial edge fillet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPartialFilletParameters( _
   ByVal AlongEdgeDirection As System.Boolean, _
   ByVal StartCondition As System.Integer, _
   ByVal StartValue As System.Double, _
   ByVal StartReference As System.Object, _
   ByVal EndCondition As System.Integer, _
   ByVal EndValue As System.Double, _
   ByVal EndReference As System.Object _
) As System.Integer
```

```

Dim instance As IPartialEdgeFilletData
Dim AlongEdgeDirection As System.Boolean
Dim StartCondition As System.Integer
Dim StartValue As System.Double
Dim StartReference As System.Object
Dim EndCondition As System.Integer
Dim EndValue As System.Double
Dim EndReference As System.Object
Dim value As System.Integer
 
value = instance.SetPartialFilletParameters(AlongEdgeDirection, StartCondition, StartValue, StartReference, EndCondition, EndValue, EndReference)
```

```

System.int SetPartialFilletParameters( 
   System.bool AlongEdgeDirection,
   System.int StartCondition,
   System.double StartValue,
   System.object StartReference,
   System.int EndCondition,
   System.double EndValue,
   System.object EndReference
)
```

```

System.int SetPartialFilletParameters( 
   System.bool AlongEdgeDirection,
   System.int StartCondition,
   System.double StartValue,
   System.Object^ StartReference,
   System.int EndCondition,
   System.double EndValue,
   System.Object^ EndReference
) 
```

#### Parameters

*AlongEdgeDirection*
:   True to start the fillet at the start point of the edge, false to start the fillet at the end point of the edge

*StartCondition*
:   Start condition as defined in [swSimpleFilletPartialEdgeCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletPartialEdgeCondition_e.html) (see **Remarks**)

*StartValue*
:   Distance or percent offset from the start point (see **Remarks**)

*StartReference*
:   Offset reference (2D/3D sketch [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), reference [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)); valid only if StartCondition is swPartialEdgeReferenceOffset

*EndCondition*
:   End condition as defined in [swSimpleFilletPartialEdgeCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSimpleFilletPartialEdgeCondition_e.html) (see **Remarks**)

*EndValue*
:   Distance or percent offset from the end point (see **Remarks**)

*EndReference*
:   Offset reference (2D/3D sketch [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), reference [point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md), planar [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)); valid only if EndCondition is swPartialEdgeReferenceOffset

#### Return Value

Result code as defined in [swFeatureError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFeatureError_e.html)

Remarks

StartValue (or EndValue) is a:

- Distance if StartCondition (or EndCondition) is swSimpleFilletPartialEdgeCondition\_e.swPartialEdgeDistanceOffset.
- Percent value if StartCondition (or EndCondition) is swSimpleFilletPartialEdgeCondition\_e.swPartialEdgePercentOffset.

Example

See the [IPartialEdgeFilletData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartialEdgeFilletData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData.md)  
[IPartialEdgeFilletData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData_members.md)  
[IPartialEdgeFilletData::AlongEdgeDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~AlongEdgeDirection.md)  
[IPartialEdgeFilletData::DistanceOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetEnd.md)  
[IPartialEdgeFilletData::DistanceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~DistanceOffsetStart.md)  
[IPartialEdgeFilletData::PercentOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetEnd.md)  
[IPartialEdgeFilletData::PercentOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~PercentOffsetStart.md)  
[IPartialEdgeFilletData::ReferenceOffsetEnd Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetEnd.md)  
[IPartialEdgeFilletData::ReferenceOffsetStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartialEdgeFilletData~ReferenceOffsetStart.md)
