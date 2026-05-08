# FeatureChainPattern Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FeatureChainPattern`

Obsolete. See IFeatureManager::CreateFeature and the Remarks in IChainPatternFeatureData.
Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.md) and the Remarks in [IChainPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FeatureChainPattern( _
   ByVal PitchMethod As System.Integer, _
   ByVal FlipDirection As System.Boolean, _
   ByVal FillPath As System.Boolean, _
   ByVal Number As System.Integer, _
   ByVal Spacing As System.Double, _
   ByVal GroupOneFlipPlane As System.Boolean, _
   ByVal GroupTwoChain As System.Boolean, _
   ByVal GroupTwoFlipPlane As System.Boolean, _
   ByVal AlignMethod As System.Integer, _
   ByVal Options As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim PitchMethod As System.Integer
Dim FlipDirection As System.Boolean
Dim FillPath As System.Boolean
Dim Number As System.Integer
Dim Spacing As System.Double
Dim GroupOneFlipPlane As System.Boolean
Dim GroupTwoChain As System.Boolean
Dim GroupTwoFlipPlane As System.Boolean
Dim AlignMethod As System.Integer
Dim Options As System.Integer
Dim value As Feature
 
value = instance.FeatureChainPattern(PitchMethod, FlipDirection, FillPath, Number, Spacing, GroupOneFlipPlane, GroupTwoChain, GroupTwoFlipPlane, AlignMethod, Options)
```

```

Feature FeatureChainPattern( 
   System.int PitchMethod,
   System.bool FlipDirection,
   System.bool FillPath,
   System.int Number,
   System.double Spacing,
   System.bool GroupOneFlipPlane,
   System.bool GroupTwoChain,
   System.bool GroupTwoFlipPlane,
   System.int AlignMethod,
   System.int Options
)
```

```

Feature^ FeatureChainPattern( 
   System.int PitchMethod,
   System.bool FlipDirection,
   System.bool FillPath,
   System.int Number,
   System.double Spacing,
   System.bool GroupOneFlipPlane,
   System.bool GroupTwoChain,
   System.bool GroupTwoFlipPlane,
   System.int AlignMethod,
   System.int Options
) 
```

#### Parameters

*PitchMethod*
:   Pitch method as defined in [swChainPatternPitchMethod\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternPitchMethod_e.html); available for all types of chain patterns

*FlipDirection*
:   True to reverse the direction of the chain pattern, false to not; available for all types of chain patterns

*FillPath*
:   True to automatically set the number of pattern instances to fill the path, false to not; available for all types of chain patterns and when EqualSpacing is false for distance and linkage distance chain patterns

*Number*
:   Number of pattern instances; available for all types of chain patterns when FillPath is false

*Spacing*
:   Distance between the pattern instances when EqualSpacing is false; only available for distance and linkage distance chain patterns when EqualSpacing is false

*GroupOneFlipPlane*
:   True to flip the path alignment plane for **Chain Group 1**, false to not; available for all types of chain patterns

*GroupTwoChain*
:   True to set the component to pattern for **Chain Group 2**, false to not; only available for connected linkage chain patterns

*GroupTwoFlipPlane*
:   True to flip the path alignment plane for **Chain Group 2**, false to not; only available for connected linkage chain patterns

*AlignMethod*
:   Alignment method as defined in [swChainPatternAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternAlignment_e.html); only available for distance and linkage distance chain patterns

*Options*
:   Option as defined in [swChainPatternOptions\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swChainPatternOptions_e.html); available for all types of chain patterns

#### Return Value

Chain pattern [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

You must pre-select the entities for the chain pattern feature. Using the selected entities, this method inserts one of these chain pattern features:

- distance
- distance linkage
- connected linkage

| Entity to select | Corresponding Chain Pattern PropertyManager control | Selection mark | Number of selections |
| --- | --- | --- | --- |
| - 2D or 3D [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) containing an open or closed loop, - [Sketch line](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchLine.md), or - Model [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) | **Path** | 2 | 1 for all types of chain patterns |
| Assembly [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) | **Chain Group 1 Component to Pattern** | 1 | 1 for all types of chain patterns |
| - Cylindrical [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md), - Circular or linear edge, - [Sketch point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md), - [Vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md), or - [Reference axis](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefAxis.md) | **Chain Group 1 Path Link 1** | 256 | 1 for all types of chain patterns |
| - Cylindrical face, - Circular or linear edge, - Sketch point, - Vertex, or - Reference axis | **Chain Group 1 Path Link 2** | 512 | - 1 for distance linkage or connected linkage - None for distance |
| Component [plane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md) or planar face | **Chain Group 1 Path Alignment Plane** | 16384 | 1 for all types of chain patterns |
| Assembly component | **Chain Group 2 Component to Pattern** | 2048 | - 1 for connected linkage - None for distance or linkage distance |
| - Cylindrical face, - Circular or linear edge, - Sketch point, - Vertex, or - Reference axis | **Chain Group 2 Path Link 1** | 4096 | - 1 for connected linkage - None for distance or linkage distance |
| - Cylindrical face, - Circular or linear edge, - Sketch point, - Vertex, or - Reference axis | **Chain Group 2 Path Link 2** | 8192 | - 1 for connected linkage - None for distance or linkage distance |
| Component plane or planar face | **Group 2 Path Alignment Plane** | 32768 | - 1 for connected linkage - None for distance or linkage distance |
| Assembly plane | **Face normal alignment** | 1024 | - 1 if the chain path is a sketch line - None for all other types of paths |

To [set equal spacing](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~SetEqualSpacing.md) between chain pattern instances, edit the chain pattern feature after creating it.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
