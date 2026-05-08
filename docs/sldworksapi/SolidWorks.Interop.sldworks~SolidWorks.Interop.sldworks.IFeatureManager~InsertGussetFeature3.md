# InsertGussetFeature3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGussetFeature3`

Inserts a gusset feature for pre-selected faces of a weldment.
Inserts a gusset feature for pre-selected faces of a weldment.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGussetFeature3( _
   ByVal Depth As System.Double, _
   ByVal DirType As System.Short, _
   ByVal LocType As System.Short, _
   ByVal BIsProfile As System.Boolean, _
   ByVal ProfileD1 As System.Double, _
   ByVal ProfileD2 As System.Double, _
   ByVal ProfileD3 As System.Double, _
   ByVal ProfileAngle As System.Double, _
   ByVal ProfileD4 As System.Double, _
   ByVal BOffset As System.Boolean, _
   ByVal DProfileOffset As System.Double, _
   ByVal CrvIndex As System.Integer, _
   ByVal BReverseDir As System.Boolean, _
   ByVal BReverseFace As System.Boolean, _
   ByVal BUseLenDim As System.Boolean, _
   ByVal ProfileD5 As System.Double, _
   ByVal ProfileD6 As System.Double, _
   ByVal ProfileChamferAngle As System.Double, _
   ByVal BUseLenDimForChamfer As System.Boolean, _
   ByVal BNeedChamferInGusset As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim Depth As System.Double
Dim DirType As System.Short
Dim LocType As System.Short
Dim BIsProfile As System.Boolean
Dim ProfileD1 As System.Double
Dim ProfileD2 As System.Double
Dim ProfileD3 As System.Double
Dim ProfileAngle As System.Double
Dim ProfileD4 As System.Double
Dim BOffset As System.Boolean
Dim DProfileOffset As System.Double
Dim CrvIndex As System.Integer
Dim BReverseDir As System.Boolean
Dim BReverseFace As System.Boolean
Dim BUseLenDim As System.Boolean
Dim ProfileD5 As System.Double
Dim ProfileD6 As System.Double
Dim ProfileChamferAngle As System.Double
Dim BUseLenDimForChamfer As System.Boolean
Dim BNeedChamferInGusset As System.Boolean
Dim value As Feature
 
value = instance.InsertGussetFeature3(Depth, DirType, LocType, BIsProfile, ProfileD1, ProfileD2, ProfileD3, ProfileAngle, ProfileD4, BOffset, DProfileOffset, CrvIndex, BReverseDir, BReverseFace, BUseLenDim, ProfileD5, ProfileD6, ProfileChamferAngle, BUseLenDimForChamfer, BNeedChamferInGusset)
```

```

Feature InsertGussetFeature3( 
   System.double Depth,
   System.short DirType,
   System.short LocType,
   System.bool BIsProfile,
   System.double ProfileD1,
   System.double ProfileD2,
   System.double ProfileD3,
   System.double ProfileAngle,
   System.double ProfileD4,
   System.bool BOffset,
   System.double DProfileOffset,
   System.int CrvIndex,
   System.bool BReverseDir,
   System.bool BReverseFace,
   System.bool BUseLenDim,
   System.double ProfileD5,
   System.double ProfileD6,
   System.double ProfileChamferAngle,
   System.bool BUseLenDimForChamfer,
   System.bool BNeedChamferInGusset
)
```

```

Feature^ InsertGussetFeature3( 
   System.double Depth,
   System.short DirType,
   System.short LocType,
   System.bool BIsProfile,
   System.double ProfileD1,
   System.double ProfileD2,
   System.double ProfileD3,
   System.double ProfileAngle,
   System.double ProfileD4,
   System.bool BOffset,
   System.double DProfileOffset,
   System.int CrvIndex,
   System.bool BReverseDir,
   System.bool BReverseFace,
   System.bool BUseLenDim,
   System.double ProfileD5,
   System.double ProfileD6,
   System.double ProfileChamferAngle,
   System.bool BUseLenDimForChamfer,
   System.bool BNeedChamferInGusset
) 
```

#### Parameters

*Depth*
:   Thickness of the gusset

*DirType*
:   Thickness direction of the gusset as defined in [swGussetThicknessType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGussetThicknessType_e.html)

*LocType*
:   Location of the reference plane for the sketch of the gusset as defined in [swGussetProfileLocationType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGussetProfileLocationType_e.html)

*BIsProfile*
:   True to use a polygon profile, false to use a triangle profile

*ProfileD1*
:   Profile Distance1 (see **Remarks**)

*ProfileD2*
:   Profile Distance2 (see **Remarks**)

*ProfileD3*
:   Profile Distance3 (see **Remarks**)

*ProfileAngle*
:   Profile Angle (see **Remarks**); valid only if BUseLenDim is false

*ProfileD4*
:   Profile Distance4 (see **Remarks**); valid only if BUseLenDim is true

*BOffset*
:   True to offset the reference plane for the sketch, false to not

*DProfileOffset*
:   Value by which to offset the reference plane for the sketch

*CrvIndex*
:   Index of the edge to use if multiple intersecting edges exist

*BReverseDir*
:   If BOffset set to true, then true to reverse direction, false to not

*BReverseFace*
:   Reverse ProfileD1 and ProfileD2 if triangle profile

    - or -

    Reverse ProfileD1 and ProfileD2 and reverse ProfileD3 and ProfileD4 if polygon profile

*BUseLenDim*
:   True to use ProfileD4, false to use ProfileAngle

*ProfileD5*
:   Chamfer Distance5 (see **Remarks**); valid only if BNeedChamferInGusset is true

*ProfileD6*
:   Chamfer Distance6 (see **Remarks**); valid only if BNeedChamferInGusset and BUseLenDimForChamber are both true

*ProfileChamferAngle*
:   Chamfer Angle (see **Remarks**); valid only if BUseLenDimForChamfer is false and BNeedChamferInGusset is true

*BUseLenDimForChamfer*
:   True to use ProfileD6, false to use ProfileChamferAngle; valid only if BNeedChamferInGusset is true

*BNeedChamferInGusset*
:   True to create a chamfer to allow room for a weld bead under the gusset, false to not

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

See the SOLIDWORKS Help for more information about profile and chamfer distances and angles in weldment gussets.

Before calling this method, you must call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) to select two faces that are the supporting legs of this gusset with a Mark of 1.

Instead of using this method, you can pass an array of faces to [IFeatureManager::InsertGussetFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertGussetFeature2.md).

Example

[Insert Gusset Feature (VBA)](Insert_Gusset_Feature_Example_VB.htm)  
[Insert Gusset Feature (VB.NET)](Insert_Gusset_Feature_Example_VBNET.htm)  
[Insert Gusset Feature (C#)](Insert_Gusset_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IGussetFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGussetFeatureData.md)
