# FeatureCircularPattern2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern2`

Obsolete. Superseded by IFeatureManager::FeatureCircularPattern3.
Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureCircularPattern2( _
   ByVal Num As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDir As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Num As System.Integer
Dim Spacing As System.Double
Dim FlipDir As System.Boolean
Dim DName As System.String
Dim GeometryPattern As System.Boolean
Dim value As Feature
 
value = instance.FeatureCircularPattern2(Num, Spacing, FlipDir, DName, GeometryPattern)
```

```

Feature FeatureCircularPattern2( 
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.string DName,
   System.bool GeometryPattern
)
```

```

Feature^ FeatureCircularPattern2( 
   System.int Num,
   System.double Spacing,
   System.bool FlipDir,
   System.String^ DName,
   System.bool GeometryPattern
) 
```

#### Parameters

*Num*
:   Number of instances of the circular pattern to insert, including the original

*Spacing*
:   Spacing between each instance of the circular pattern in radians

*FlipDir*
:   True to flip the direction of the circular pattern, false to not

*DName*
:   Name of the angular dimension defining the direction of the pattern

*GeometryPattern*
:   True to use geometry pattern, false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method requires ordered selection of the features and components.

- Features and axis: Use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with a Mark of 4 for the features to pattern and a Mark of 1 for the axis. You can also use [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) to select the features and the axis.
- Components and axis: Use IModelDocExtension::SelectByID2 with a Mark of 1 for the components to pattern and a Mark of 2 for the axis.

You must select the features or components before selecting the axis.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)
