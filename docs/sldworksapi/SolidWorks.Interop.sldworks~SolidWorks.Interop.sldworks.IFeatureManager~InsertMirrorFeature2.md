# InsertMirrorFeature2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMirrorFeature2`

Mirrors selected features, faces, bodies, and structure systems about a selected plane or planar face.
Mirrors selected features, faces, bodies, and structure systems about a selected plane or planar face.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMirrorFeature2( _
   ByVal BMirrorBody As System.Boolean, _
   ByVal BGeometryPattern As System.Boolean, _
   ByVal BMerge As System.Boolean, _
   ByVal BKnit As System.Boolean, _
   ByVal ScopeOptions As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BMirrorBody As System.Boolean
Dim BGeometryPattern As System.Boolean
Dim BMerge As System.Boolean
Dim BKnit As System.Boolean
Dim ScopeOptions As System.Integer
Dim value As Feature
 
value = instance.InsertMirrorFeature2(BMirrorBody, BGeometryPattern, BMerge, BKnit, ScopeOptions)
```

```

Feature InsertMirrorFeature2( 
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit,
   System.int ScopeOptions
)
```

```

Feature^ InsertMirrorFeature2( 
   System.bool BMirrorBody,
   System.bool BGeometryPattern,
   System.bool BMerge,
   System.bool BKnit,
   System.int ScopeOptions
) 
```

#### Parameters

*BMirrorBody*
:   True to mirror solid bodies; false to mirror a feature or face

*BGeometryPattern*
:   True to mirror only the feature geometry, false to solve the entire feature; applies to mirroring features only

*BMerge*
:   True to merge any mirrored solid bodies, false to not; applies to mirroring solid bodies only

*BKnit*
:   True to knit surfaces, false to not; applies to mirroring surfaces only

*ScopeOptions*
:   Feature scope as defined by [swFeatureScope\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureScope_e.html)

#### Return Value

[Feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

This method attempts to create the mirror feature without displaying a dialog box to get information from the user. It relies on preselected and marked entities and arguments.

 Structure systems 134217728

|  |  |
| --- | --- |
| **Any of these entities to be mirrored...** | **Must be preselected and marked with a value of...** |
| Features | 1 |
| Faces | 128 |
| Bodies | 256 |
| Structure systems | 134217728 |
| Planes or planar faces | 2 |

For information on selecting and marking entities, see [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md).

Example

See the [IMirrorSolidFeatureData::StructureSystemToPatternArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~StructureSystemToPatternArray.md) examples.

Example

[Get Mirror Pattern Feature Data (C#)](Get_Mirror_Pattern_Feature_Data_Example_CSharp.htm)  
[Get Mirror Pattern Feature Data (VB.NET)](Get_Mirror_Pattern_Feature_Data_Example_VBNET.htm)  
[Get Mirror Pattern Feature Data (VBA)](Get_Mirror_Feature_Data_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMirrorPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPatternFeatureData.md)
