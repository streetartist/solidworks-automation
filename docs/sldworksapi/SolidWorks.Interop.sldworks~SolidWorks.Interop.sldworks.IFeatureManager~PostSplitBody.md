# PostSplitBody Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody`

Obsolete. Superseded by IFeatureManager::PostSplitBody2.
Obsolete. Superseded by [IFeatureManager::PostSplitBody2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PostSplitBody2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PostSplitBody( _
   ByVal BodiesToMark As System.Object, _
   ByVal ConsumeCut As System.Boolean, _
   ByVal Origins As System.Object, _
   ByVal SavePaths As System.Object _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BodiesToMark As System.Object
Dim ConsumeCut As System.Boolean
Dim Origins As System.Object
Dim SavePaths As System.Object
Dim value As Feature
 
value = instance.PostSplitBody(BodiesToMark, ConsumeCut, Origins, SavePaths)
```

```

Feature PostSplitBody( 
   System.object BodiesToMark,
   System.bool ConsumeCut,
   System.object Origins,
   System.object SavePaths
)
```

```

Feature^ PostSplitBody( 
   System.Object^ BodiesToMark,
   System.bool ConsumeCut,
   System.Object^ Origins,
   System.Object^ SavePaths
) 
```

#### Parameters

*BodiesToMark*
:   Bodies to mark for the split operation

*ConsumeCut*
:   True to remove the bodies from the part, false to not

*Origins*
:   Array of origins of the bodies to save

*SavePaths*
:   Array of paths and filenames of part documents to which to save BodiesToMark

#### Return Value

Pointer to the split-body [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

To create a split-body feature:

1. Select the entities to use to split the part into multiple bodies.
2. Call [IFeatureManager::PreSplitBody](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~PreSplitBody.md) to get all of the bodies created by splitting the part.
3. Call this method to create the split-body feature.

The size of the BodiesToMark, Origins, and SavePaths arrays must be equal and greater than 0. If you pass an empty path and filename for a body, then that body is only marked and not saved. It remains with the original part.

To find out if the bodies in a split-body feature were consumed, use [ISplitBodyFeatureData::Consume](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~Consume.md).

[IFeature::GetTypeName2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName2.md) and [IFeature::GetTypeName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetTypeName.md) return:

- **Split** for a feature that was created by splitting a part into multiple parts by using either this method or the **Split** feature in the user interface. You can access a split-body feature's data using the [ISplitBodyFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData.md) interface.
- **SplitBody** for a body created by splitting a part and saving the body to a part. You cannot access the data of a split body saved to a part.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISplitBodyFeatureData::GetSplitBodies Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~GetSplitBodies.md)  
[ISplitBodyFeatureData::SetSplitBodies2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitBodyFeatureData~SetSplitBodies2.md)
