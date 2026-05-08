# FeatureCircularPattern4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern4`

Obsolete. Superseded by IFeatureManager::FeatureCircularPattern5.
Obsolete. Superseded by [IFeatureManager::FeatureCircularPattern5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureCircularPattern5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureCircularPattern4( _
   ByVal Number As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal FlipDirection As System.Boolean, _
   ByVal DName As System.String, _
   ByVal GeometryPattern As System.Boolean, _
   ByVal EqualSpacing As System.Boolean, _
   ByVal VaryInstance As System.Boolean _
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
Dim VaryInstance As System.Boolean
Dim value As Feature
 
value = instance.FeatureCircularPattern4(Number, Spacing, FlipDirection, DName, GeometryPattern, EqualSpacing, VaryInstance)
```

```

Feature FeatureCircularPattern4( 
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.string DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing,
   System.bool VaryInstance
)
```

```

Feature^ FeatureCircularPattern4( 
   System.int Number,
   System.double Spacing,
   System.bool FlipDirection,
   System.String^ DName,
   System.bool GeometryPattern,
   System.bool EqualSpacing,
   System.bool VaryInstance
) 
```

#### Parameters

*Number*
:   Number of instances of the circular pattern to insert, including the original instance

*Spacing*
:   Spacing between each instance of the circular pattern; total angle in radians if EqualSpacing is true

*FlipDirection*
:   True to flip the direction of the circular pattern, false to not

*DName*
:   Name of the angular dimension defining the direction of the pattern

*GeometryPattern*
:   True to use geometry pattern, false to not

*EqualSpacing*
:   True to use equal spacing, false to not

*VaryInstance*
:   True to vary the dimensions or spacing of individual pattern instances, false to not; valid only if GeometryPattern = false (see **Remarks**)

#### Return Value

Circular pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

|  |  |  |
| --- | --- | --- |
| If... | To select a feature, use... | To select a component, use... |
| Using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select features and components, ordered selection of the features and components is required | - 1 to mark the direction axis - 4 to mark the features to pattern | - 1 to mark the components to pattern - 2 to mark the direction axis |
| Directly selecting a feature or axis using [IFeature::Select2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~Select2.md) | - 1 to mark the direction axis - 4 to mark the features to pattern | [ISelectData::Mark](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData~Mark.md) and [Component2::Select3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Select3.md)   - 1 to mark the components to pattern - 2 to mark the direction axis |

If VaryInstance = true, then to indicate how to vary the individual pattern instances, decide on the type of pattern and call its corresponding method before calling this method:

| Type... | Method... |
| --- | --- |
| Increment | [IFeatureManager::InsertVaryInstanceIncrement](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceIncrement.md) |
| Override | [IFeatureManager::InsertVaryInstanceOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertVaryInstanceOverride.md) |

Example

[Create Circular Pattern (VBA)](Create_Circular_Pattern_Example_VB.htm)  
[Create Circular Pattern (VB.NET)](Create_Circular_Pattern_Example_VBNET.htm)  
[Create Circular Pattern (C#)](Create_Circular_Pattern_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ICircularPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICircularPatternFeatureData.md)
