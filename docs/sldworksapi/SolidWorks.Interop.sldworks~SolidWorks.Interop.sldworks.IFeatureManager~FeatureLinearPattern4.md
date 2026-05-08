# FeatureLinearPattern4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern4`

Obsolete. Superseded by IFeatureManager::FeatureLinearPattern5.
Obsolete. Superseded by [IFeatureManager::FeatureLinearPattern5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureLinearPattern4( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal FlipDir1 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal VaryInstance As System.Boolean, _
   ByVal HasOffset1 As System.Boolean, _
   ByVal HasOffset2 As System.Boolean, _
   ByVal CtrlByNum1 As System.Boolean, _
   ByVal CtrlByNum2 As System.Boolean, _
   ByVal FromCentroid1 As System.Boolean, _
   ByVal FromCentroid2 As System.Boolean, _
   ByVal RevOffset1 As System.Boolean, _
   ByVal RevOffset2 As System.Boolean, _
   ByVal Offset1 As System.Double, _
   ByVal Offset2 As System.Double _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Num1 As System.Integer
Dim Spacing1 As System.Double
Dim Num2 As System.Integer
Dim Spacing2 As System.Double
Dim FlipDir1 As System.Boolean
Dim FlipDir2 As System.Boolean
Dim DName1 As System.String
Dim DName2 As System.String
Dim GeometryPattern As System.Boolean
Dim VaryInstance As System.Boolean
Dim HasOffset1 As System.Boolean
Dim HasOffset2 As System.Boolean
Dim CtrlByNum1 As System.Boolean
Dim CtrlByNum2 As System.Boolean
Dim FromCentroid1 As System.Boolean
Dim FromCentroid2 As System.Boolean
Dim RevOffset1 As System.Boolean
Dim RevOffset2 As System.Boolean
Dim Offset1 As System.Double
Dim Offset2 As System.Double
Dim value As Feature
 
value = instance.FeatureLinearPattern4(Num1, Spacing1, Num2, Spacing2, FlipDir1, FlipDir2, DName1, DName2, GeometryPattern, VaryInstance, HasOffset1, HasOffset2, CtrlByNum1, CtrlByNum2, FromCentroid1, FromCentroid2, RevOffset1, RevOffset2, Offset1, Offset2)
```

```

Feature FeatureLinearPattern4( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.string DName1,
   System.string DName2,
   System.bool GeometryPattern,
   System.bool VaryInstance,
   System.bool HasOffset1,
   System.bool HasOffset2,
   System.bool CtrlByNum1,
   System.bool CtrlByNum2,
   System.bool FromCentroid1,
   System.bool FromCentroid2,
   System.bool RevOffset1,
   System.bool RevOffset2,
   System.double Offset1,
   System.double Offset2
)
```

```

Feature^ FeatureLinearPattern4( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.String^ DName1,
   System.String^ DName2,
   System.bool GeometryPattern,
   System.bool VaryInstance,
   System.bool HasOffset1,
   System.bool HasOffset2,
   System.bool CtrlByNum1,
   System.bool CtrlByNum2,
   System.bool FromCentroid1,
   System.bool FromCentroid2,
   System.bool RevOffset1,
   System.bool RevOffset2,
   System.double Offset1,
   System.double Offset2
) 
```

#### Parameters

*Num1*
:   Number of instances of the linear pattern in Direction 1, including the original

*Spacing1*
:   Spacing in meters between each instance of the linear pattern in Direction 1

*Num2*
:   Number of instances of the linear pattern in Direction 2, including the original

*Spacing2*
:   Spacing in meters between each instance of the linear pattern in Direction 2

*FlipDir1*
:   True to reverse the direction of the linear pattern in Direction 1, false to not

*FlipDir2*
:   True to reverse the direction of the linear pattern in Direction 2, false to not

*DName1*
:   Name of the dimension defining Direction 1

*DName2*
:   Name of the dimension defining Direction 2

*GeometryPattern*
:   True to use geometry pattern, false to not

*VaryInstance*
:   True to vary the dimensions and spacing of individual pattern instances, false to not; valid only if GeometryPattern = false (see **Remarks**)

*HasOffset1*
:   True if using Offset1 to specify an offset of the pattern seed from a selected reference in Direction 1, false if not

*HasOffset2*
:   True if using Offset2 to specify an offset of the pattern seed from a selected reference in Direction 2, false if not

*CtrlByNum1*
:   True to control pattern spacing using Num1, false to control it using Spacing1; valid only if HasOffset1 is true

*CtrlByNum2*
:   True to control pattern spacing using Num2, false to control it using Spacing2; valid only if HasOffset2 is true

*FromCentroid1*
:   True if Offset1 is measured from the centroid of the seed instance, false if it is measured from a selected reference on the seed instance; valid only if HasOffset1 is true (see **Remarks**)

*FromCentroid2*
:   True if Offset2 is measured from the centroid of the seed instance, false if it is measured from a selected reference on the seed instance; valid only if HasOffset2 is true (see **Remarks**)

*RevOffset1*
:   True to reverse the direction of Offset1, false to not; valid only if HasOffset1 is true

*RevOffset2*
:   True to reverse the direction of Offset2, false to not; valid only if HasOffset2 is true

*Offset1*
:   Offset in meters from a selected reference in Direction 1 (see **Remarks**); valid only if HasOffset1 is true

*Offset2*
:   Offset in meters from a selected reference in Direction 2 (see **Remarks**); valid only if HasOffset2 is true

#### Return Value

Linear pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

| If... | To select a feature, use... | To select a component, use... |
| --- | --- | --- |
| Using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select features and components, ordered selection of the features and components is required | - 1 to mark Direction 1, and 2 to mark Direction 2 - 4 to mark the features to pattern - 2097152 to mark references for Offset1 and Offset2 - 8388608 to mark a seed instance reference when FromCentroid1 or FromCentroid2 is false | - 1 to mark the components to pattern - 2 and 4 to mark the directions |
| Directly selecting a feature or component using [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) | - 1 to mark Direction 1, and 2 to mark Direction 2 - 4 to mark the features to pattern - 2097152 to mark references for Offset1 and Offset2 - 8388608 to mark a seed instance reference when FromCentroid1 or FromCentroid2 is false | [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) and [IComponent2::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select4.md)   - 1 to mark the components to pattern - 2 and 4 to mark the directions |

If VaryInstance = true, then to indicate how to vary the individual pattern instances, decide on the type of pattern and call its corresponding method before calling this method:

| Type | Method |
| --- | --- |
| Increment | [IFeatureManager::InsertVaryInstanceIncrement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceIncrement.md) |
| Override | [IFeatureManager::InsertVaryInstanceOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.md) |

Example

[Create Linear Pattern (VBA)](Create_Linear_Pattern_Example_VB.htm)  
[Create Linear Pattern (VB.NET)](Create_Linear_Pattern_Example_VBNET.htm)  
[Create Linear Pattern (C#)](Create_Linear_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)  
[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.md)
