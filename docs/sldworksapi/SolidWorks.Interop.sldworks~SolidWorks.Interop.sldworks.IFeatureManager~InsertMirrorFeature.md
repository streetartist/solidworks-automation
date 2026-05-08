# InsertMirrorFeature Method (IFeatureManager)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature`

Obsolete. Superseded by IFeatureManager::InsertMirrorFeature2.
Obsolete. Superseded by [IFeatureManager::InsertMirrorFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMirrorFeature( _
   ByVal BMirrorBody As System.Boolean, _
   ByVal BGeometryPattern As System.Boolean, _
   ByVal BMerge As System.Boolean, _
   ByVal BKnit As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BMirrorBody As System.Boolean
Dim BGeometryPattern As System.Boolean
Dim BMerge As System.Boolean
Dim BKnit As System.Boolean
Dim value As Feature
 
value = instance.InsertMirrorFeature(BMirrorBody, BGeometryPattern, BMerge, BKnit)
```

```

Feature InsertMirrorFeature( 
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit
)
```

```

Feature^ InsertMirrorFeature( 
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit
) 
```

#### Parameters

*BMirrorBody*
:   True to mirror solid bodies; false to mirror a feature or face

*BGeometryPattern*
:   True to mirror only the feature geometry, false to solve the entire feature; applies  
    to mirroring features only

*BMerge*
:   True to merge any mirrored solid bodies, false to not; applies to mirroring solid  
    bodies only

*BKnit*
:   True to knit surfaces, false to not; applies to mirroring surfaces only

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

This method attempts to create the mirror feature without displaying a dialog box to get information from the user. It relies on preselected and marked entities, as well as arguments.

|  |  |
| --- | --- |
| **Any...** | **Must be preselected and marked with a value of...** |
| Features to be mirrored | 1 |
| Faces to be mirrored | 128 |
| Bodies to be mirrored | 256 |
| Plane or planar face | 2 |

For information on selecting and marking entities, see [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.md)  
[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md)
