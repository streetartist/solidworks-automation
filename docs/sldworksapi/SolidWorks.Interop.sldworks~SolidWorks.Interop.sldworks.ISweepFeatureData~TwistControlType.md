# TwistControlType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType`

Gets or sets the type of twist control for this sweep feature.
Gets or sets the type of twist control for this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TwistControlType As System.Short
```

```

Dim instance As ISweepFeatureData
Dim value As System.Short
 
instance.TwistControlType = value
 
value = instance.TwistControlType
```

```

System.short TwistControlType {get; set;}
```

```

property System.short TwistControlType {
   System.short get();
   void set (    System.short value);
}
```

#### Property Value

Twist control as defined in [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTwistControlType_e.html) (see **Remarks**)

Remarks

| For user interface options... | | Set... | |
| --- | --- | --- | --- |
| **Profile Orientation set to...** | **And Profile Twist set to...** | **ISweepFeatureData::TwistControlType as defined in swTwistControlType\_e to...** | **And** [**ISweepFeatureData::PathAlignmentType**](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType.md) **as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTangencyType_e.html) to...** |
| Follow Path | None | swTwistControlFollowPath | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath | swTangencyNone |
| Specify Direction Vector | swTwistControlFollowPath | swTangencyDirectionVector |
| Follow Path and First Guide Curve (option appears with at least one guide curve) | swTwistControlFollowPathFirstGuideCurve | swTangencyNone |
| Follow Path and First and Second Guide Curves (option appears with at least two guide curves) | swTwistControlFollowFirstSecondGuideCurves | swTangencyNone |
| Tangent to Adjacent Faces | swTwistControlFollowPath | swTangencyAllFaces |
| Minimum Twist (available only with a 3D path) | swTwistControlFollowPath | swMinimumTwist |
| Natural | swTwistControlFollowPath | swTangencyNone |
| Keep Normal Constant | None | swTwistControlKeepNormalConstant | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath + swTwistControlKeepNormalConstant | swTangencyNone |

If you specify this property with swTwistControlType\_e.swTwistControlConstantTwistAlongPath to specify profile twist values, you must set [ISweepFeatureData::AlignWithEndFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~AlignWithEndFaces.md) to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::GetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetTwistAngle.md)  
[ISweepFeatureData::SetTwistAngle Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetTwistAngle.md)  
[ISweepFeatureData::D1ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D1ReverseTwistDir.md)  
[ISweepFeatureData::D2ReverseTwistDir Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~D2ReverseTwistDir.md)  
[ISweepFeatureData::GetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetD2TwistAngle.md)  
[ISweepFeatureData::SetD2TwistAngle Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetD2TwistAngle.md)
