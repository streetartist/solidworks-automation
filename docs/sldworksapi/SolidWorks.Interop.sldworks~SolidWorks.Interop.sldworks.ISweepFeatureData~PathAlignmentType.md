# PathAlignmentType Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~PathAlignmentType`

Gets or sets the alignment of the sweep path in this sweep feature.
Gets or sets the alignment of the sweep path in this sweep feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PathAlignmentType As System.Integer
```

```

Dim instance As ISweepFeatureData
Dim value As System.Integer
 
instance.PathAlignmentType = value
 
value = instance.PathAlignmentType
```

```

System.int PathAlignmentType {get; set;}
```

```

property System.int PathAlignmentType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Sweep path alignment as defined in [swTangencyType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swTangencyType_e.html):

- swTangencyAllFaces
- swTangencyDirectionVector
- swTangencyNone

Remarks

| For user interface option... | | Set... | |
| --- | --- | --- | --- |
| **Profile Orientation set to...** | **And Profile Twist set to...** | **[ISweepFeatureData::TwistControlType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~TwistControlType.md) as defined in [swTwistControlType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swTwistControlType_e.html) to...** | **And** **ISweepFeatureData::PathAlignmentType** **as defined in swTangencyType\_e to...** |
| Follow Path | None | swTwistControlFollowPath | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath | swTangencyNone |
| Specify Direction Vector | swTwistControlFollowPath | swTangencyDirectionVector; call [ISweepFeatureData::SetPathAlignmentDirectionVector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~SetPathAlignmentDirectionVector.md) to specify the direction vector |
| Follow Path and First Guide Curve (option appears with at least one guide curve) | swTwistControlFollowPathFirstGuideCurve | swTangencyNone |
| Follow Path and First and Second Guide Curves (option appears with at least two guide curves) | swTwistControlFollowFirstSecondGuideCurves | swTangencyNone |
| Tangent to Adjacent Faces | swTwistControlFollowPath | swTangencyAllFaces |
| Minimum Twist (available only with a 3D path) | swTwistControlFollowPath | swMinimumTwist |
| Natural | swTwistControlFollowPath | swTangencyNone |
| Keep Normal Constant | None | swTwistControlKeepNormalConstant | swTangencyNone |
| Specify Twist Value | swTwistControlConstantTwistAlongPath + swTwistControlKeepNormalConstant | swTangencyNone |

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISweepFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISweepFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData.md)  
[ISweepFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData_members.md)  
[ISweepFeatureData::GetPathAlignmentDirectionVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathAlignmentDirectionVector.md)  
[ISweepFeatureData::GetPathType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISweepFeatureData~GetPathType.md)
