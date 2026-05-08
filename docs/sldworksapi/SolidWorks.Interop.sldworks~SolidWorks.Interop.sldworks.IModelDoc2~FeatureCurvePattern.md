# FeatureCurvePattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureCurvePattern`

Obsolete. See IFeatureManager::CreateFeature and the Remarks of ICurveDrivenPatternFeatureData.
Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) and the Remarks of [ICurveDrivenPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub FeatureCurvePattern( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal FlipDir1 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal EqualSpacing1 As System.Boolean, _
   ByVal EqualSpacing2 As System.Boolean, _
   ByVal UseCentroid As System.Boolean, _
   ByVal AlignToSeed As System.Boolean, _
   ByVal OffsetCurve As System.Boolean, _
   ByVal PatternSeedOnly As System.Boolean _
) 
```

```

Dim instance As IModelDoc2
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim FlipDir1 As System.Boolean
Dim FlipDir2 As System.Boolean
Dim EqualSpacing1 As System.Boolean
Dim EqualSpacing2 As System.Boolean
Dim UseCentroid As System.Boolean
Dim AlignToSeed As System.Boolean
Dim OffsetCurve As System.Boolean
Dim PatternSeedOnly As System.Boolean
 
instance.FeatureCurvePattern(Num1, Spacing1, Num2, Spacing2, FlipDir1, FlipDir2, EqualSpacing1, EqualSpacing2, UseCentroid, AlignToSeed, OffsetCurve, PatternSeedOnly)
```

```

void FeatureCurvePattern( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.bool EqualSpacing1,
   System.bool EqualSpacing2,
   System.bool UseCentroid,
   System.bool AlignToSeed,
   System.bool OffsetCurve,
   System.bool PatternSeedOnly
)
```

```

void FeatureCurvePattern( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.bool EqualSpacing1,
   System.bool EqualSpacing2,
   System.bool UseCentroid,
   System.bool AlignToSeed,
   System.bool OffsetCurve,
   System.bool PatternSeedOnly
) 
```

#### Parameters

*Num1*
:   Number of instances in the first direction, including the original

*Spacing1*
:   Spacing in radians

*Num2*
:   Number of instances in the second direction

*Spacing2*
:   Spacing in radians

*FlipDir1*
:   True flips the direction of the first direction, false does not

*FlipDir2*
:   True flips the direction of the second direction, false does not

*EqualSpacing1*
:   True uses equal spacing between instances in the first direction, false does not

*EqualSpacing2*
:   True uses equal spacing between instances in the second direction, false does not

*UseCentroid*
:   True uses the centroid as reference point, false does not

*AlignToSeed*
:   True aligns the new objects with the seed feature, false does not

*OffsetCurve*
:   True offsets the curve, false transforms it

*PatternSeedOnly*
:   True uses only the seed feature in the second direction, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
