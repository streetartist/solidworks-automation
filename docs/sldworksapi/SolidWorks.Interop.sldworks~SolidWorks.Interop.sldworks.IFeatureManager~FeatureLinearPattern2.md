# FeatureLinearPattern2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern2`

Obsolete. Superseded by IFeatureManager::FeatureLinearPattern3.
Obsolete. Superseded by [IFeatureManager::FeatureLinearPattern3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureLinearPattern3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureLinearPattern2( _
   ByVal Num1 As System.Integer, _
   ByVal Spacing1 As System.Double, _
   ByVal Num2 As System.Integer, _
   ByVal Spacing2 As System.Double, _
   ByVal FlipDir1 As System.Boolean, _
   ByVal FlipDir2 As System.Boolean, _
   ByVal DName1 As System.String, _
   ByVal DName2 As System.String, _
   ByVal GeometryPattern As System.Boolean _
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
Dim value As Feature
 
value = instance.FeatureLinearPattern2(Num1, Spacing1, Num2, Spacing2, FlipDir1, FlipDir2, DName1, DName2, GeometryPattern)
```

```

Feature FeatureLinearPattern2( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.string DName1,
   System.string DName2,
   System.bool GeometryPattern
)
```

```

Feature^ FeatureLinearPattern2( 
   System.int Num1,
   System.double Spacing1,
   System.int Num2,
   System.double Spacing2,
   System.bool FlipDir1,
   System.bool FlipDir2,
   System.String^ DName1,
   System.String^ DName2,
   System.bool GeometryPattern
) 
```

#### Parameters

*Num1*
:   Number of instances of the linear pattern in Direction 1, including the original

*Spacing1*
:   Spacing between each instance of the linear pattern in Direction 1 in meters

*Num2*
:   Number of instances of the linear pattern in Direction 2, including the original

*Spacing2*
:   Spacing between each instance of the linear pattern in Direction 2 in meters

*FlipDir1*
:   True if you want to reverse the direction the linear pattern in Direction 1, false if not

*FlipDir2*
:   True if you want to reverse the direction of the linear pattern in Direction 2, false if not

*DName1*
:   Name of the dimension defining Direction 1

*DName2*
:   Name of the dimension defining Direction 2

*GeometryPattern*
:   True to use geometry pattern, false to not

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

|  |  |  |
| --- | --- | --- |
| If... | To select a feature, use... | To select a component, use... |
| Using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select features and components, ordered selection of the features and components is required | - 1 and 2 to mark the directions - 4 to mark the features to pattern | - 1 to mark the components to pattern - 2 and 4 to mark the directions |
| Directly selecting a feature or component | [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) | [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) and [Component2::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.md) |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ILinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearPatternFeatureData.md)
