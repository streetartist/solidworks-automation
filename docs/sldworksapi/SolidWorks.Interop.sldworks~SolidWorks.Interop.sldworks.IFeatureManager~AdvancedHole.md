# AdvancedHole Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole`

Obsolete. Superseded by IFeatureManager::AdvancedHole2.
Obsolete. Superseded by [IFeatureManager::AdvancedHole2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AdvancedHole2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AdvancedHole( _
   ByVal AdvancedHoleNearElementArray As System.Object, _
   ByVal AdvancedHoleFarElementArray As System.Object, _
   ByVal UseBaselineDimensions As System.Boolean, _
   ByVal IsCustomCallout As System.Boolean, _
   ByRef ResultArray As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim AdvancedHoleNearElementArray As System.Object
Dim AdvancedHoleFarElementArray As System.Object
Dim UseBaselineDimensions As System.Boolean
Dim IsCustomCallout As System.Boolean
Dim ResultArray As System.Object
Dim value As Feature
 
value = instance.AdvancedHole(AdvancedHoleNearElementArray, AdvancedHoleFarElementArray, UseBaselineDimensions, IsCustomCallout, ResultArray)
```

```

Feature AdvancedHole( 
   System.object AdvancedHoleNearElementArray,
   System.object AdvancedHoleFarElementArray,
   System.bool UseBaselineDimensions,
   System.bool IsCustomCallout,
   out System.object ResultArray
)
```

```

Feature^ AdvancedHole( 
   System.Object^ AdvancedHoleNearElementArray,
   System.Object^ AdvancedHoleFarElementArray,
   System.bool UseBaselineDimensions,
   System.bool IsCustomCallout,
   [Out] System.Object^ ResultArray
) 
```

#### Parameters

*AdvancedHoleNearElementArray*
:   Array of near side hole data objects (see **Remarks**)

*AdvancedHoleFarElementArray*
:   Array of far side hole data objects (see **Remarks**)

*UseBaselineDimensions*
:   True to use baseline dimensions, false to not (see **Remarks**)

*IsCustomCallout*
:   True to customize the hole callout, false to use a default hole callout (see **Remarks**)

*ResultArray*
:   Array of result codes as defined in [swAdvancedHoleResults\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swAdvancedHoleResults_e.html) (see **Remarks**)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md); Nothing or null if this method results in an invalid geometry condition (see **Remarks**)

Remarks

The Advanced Hole feature:

- is separate from the Hole Wizard functionality (see [FeatureManager::HoleWizard5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~HoleWizard5.md)).
- consists of several hole elements, e.g., counterbore, countersink, straight, and tapered tap, that are stacked from the near and far side faces inward. The near and far side stacks, combined, form the Advanced Hole.
- can be added only to parts at this time.

AdvancedHoleNearElementArray and AdvancedHoleFarElementArray each contain one or more hole type-specific objects in order as they stack from the near and far side faces:

- [ICounterboreElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICounterboreElementData.md)
- [ICountersinkElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICountersinkElementData.md)
- [IStraightElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightElementData.md)
- [IStraightTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)
- [ITaperedTapElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITaperedTapElementData.md)

The hole type-specific interfaces above extend the parent interface, [IAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData.md), which you use to set general Advanced Hole properties.

UseBaseLineDimensions controls which hole type-specific properties are valid. See [IAdvancedHoleFeatureData::UseBaselineDimensions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData~UseBaselineDimensions.md).

IsCustomCallout set to true allows you to set a custom callout string for individual hole elements using [IAdvancedHoleElementData::CalloutString](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleElementData~CalloutString.md).

ResultArray contains a return code for each element in AdvancedHoleNearElementArray and AdvancedHoleFarElementArray. It is possible for this method to fail to create an advanced hole, even though ResultArray contains all success result codes. If the individual hole elements all combine to produce invalid geometry (e.g., a disjoint body or a self-intersecting face) or if incorrect near or far side faces are selected, then this method returns Nothing or null.

To create an Advanced Hole feature, follow the examples which do the following:

1. Call [IModelDocExtension::SelectByRay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByRay.md) to select the near side (Mark = 256) and far side (Mark = 512) faces of the Advanced Hole. You must select these faces by location, so do not use [IEntity::Select4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity~Select4.md).
2. Call [IModelDocExtension::CreateAdvancedHoleElementData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CreateAdvancedHoleElementData.md) to create an AdvancedHoleElementData object.
3. Set the general Advanced Hole properties using the AdvancedHoleElementData object.
4. Cast the AdvancedHoleElementData object using one of the hole type-specific interfaces.
5. Set the specific Advanced Hole properties using the hole type-specific object.
6. Repeat steps 2 - 5 for each hole element you want to add to the near and far side stacks of the Advanced Hole.
7. Create near and far side arrays of the hole type-specific objects in stacking order from each face inward. The innermost elements of each stack should match to create a contiguous hole that extends from near side face to far side face.
8. Pass the near and far side arrays to IFeatureManager::AdvancedHole to create the Advanced Hole.
9. Delete the defining Advanced Hole sketch point and call [ISketchManager::CreatePoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreatePoint.md) one or more times to insert the Advanced Hole in multiple locations.

To edit an Advanced Hole feature, call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.md) to access [IAdvancedHoleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedHoleFeatureData.md). See [Accessing Selections that Define Features](sldworksapiprogguide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)
