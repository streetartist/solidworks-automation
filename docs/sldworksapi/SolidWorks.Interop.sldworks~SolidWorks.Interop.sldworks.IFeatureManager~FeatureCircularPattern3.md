# FeatureCircularPattern3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern3`

Obsolete. Superseded by IFeatureManager::FeatureCircularPattern4.
Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureCircularPattern3( _
   ByVal Number As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDirection As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal EqualSpacing As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Number As System.Integer
Dim Spacing As System.Double
Dim FlipDirection As System.Boolean
Dim DName As System.String
Dim GeometryPattern As System.Boolean
Dim EqualSpacing As System.Boolean
Dim value As Feature
 
value = instance.FeatureCircularPattern3(Number, Spacing, FlipDirection, DName, GeometryPattern, EqualSpacing)
```

```

Feature FeatureCircularPattern3( 
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.string DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing
)
```

```

Feature^ FeatureCircularPattern3( 
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.String^ DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing
) 
```

#### Parameters

*Number*
:   Number of instances of the circular pattern to insert, including the original instance

*Spacing*
:   Spacing between each instance of the circular pattern or total angle if EqualSpacing is true (in radians)

*FlipDirection*
:   True to flip the direction of the circular pattern, false to not

*DName*
:   Name of the angular dimension defining the direction of the pattern

*GeometryPattern*
:   True to use geometry pattern, false to not

*EqualSpacing*
:   True to use equal spacing, false to not

#### Return Value

Circular pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

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
