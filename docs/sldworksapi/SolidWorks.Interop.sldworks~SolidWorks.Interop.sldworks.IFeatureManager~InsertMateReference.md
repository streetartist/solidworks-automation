# InsertMateReference Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMateReference`

Obsolete. Superseded by IFeatureManager::InsertMateReference2.
Obsolete. Superseded by [IFeatureManager::InsertMateReference2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMateReference2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMateReference( _
   ByVal BstrMateReferenceName As System.String, _
   ByVal PrimaryReferenceEntity As Entity, _
   ByVal PrimaryReferenceType As System.Integer, _
   ByVal PrimaryReferenceAlignment As System.Integer, _
   ByVal SecondaryReferenceEntity As Entity, _
   ByVal SecondaryReferenceType As System.Integer, _
   ByVal SecondaryReferenceAlignment As System.Integer, _
   ByVal TertiaryReferenceEntity As Entity, _
   ByVal TertiaryReferenceType As System.Integer, _
   ByVal TertiaryReferenceAlignment As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BstrMateReferenceName As System.String
Dim PrimaryReferenceEntity As Entity
Dim PrimaryReferenceType As System.Integer
Dim PrimaryReferenceAlignment As System.Integer
Dim SecondaryReferenceEntity As Entity
Dim SecondaryReferenceType As System.Integer
Dim SecondaryReferenceAlignment As System.Integer
Dim TertiaryReferenceEntity As Entity
Dim TertiaryReferenceType As System.Integer
Dim TertiaryReferenceAlignment As System.Integer
Dim value As Feature
 
value = instance.InsertMateReference(BstrMateReferenceName, PrimaryReferenceEntity, PrimaryReferenceType, PrimaryReferenceAlignment, SecondaryReferenceEntity, SecondaryReferenceType, SecondaryReferenceAlignment, TertiaryReferenceEntity, TertiaryReferenceType, TertiaryReferenceAlignment)
```

```

Feature InsertMateReference( 
   System.string BstrMateReferenceName,
   Entity PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   Entity SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   Entity TertiaryReferenceEntity,
   System.int TertiaryReferenceType,
   System.int TertiaryReferenceAlignment
)
```

```

Feature^ InsertMateReference( 
   System.String^ BstrMateReferenceName,
   Entity^ PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   Entity^ SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   Entity^ TertiaryReferenceEntity,
   System.int TertiaryReferenceType,
   System.int TertiaryReferenceAlignment
) 
```

#### Parameters

*BstrMateReferenceName*
:   Name of mate reference

*PrimaryReferenceEntity*
:   Pointer to the primary mate, the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*PrimaryReferenceType*
:   Primary mate's reference type as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)

*PrimaryReferenceAlignment*
:   Primary mate's reference alignment type as defined [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

*SecondaryReferenceEntity*
:   Pointer to the secondary mate, the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*SecondaryReferenceType*
:   Secondary mate's reference type as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)

*SecondaryReferenceAlignment*
:   Secondary mate's alignment type as defined [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

*TertiaryReferenceEntity*
:   Pointer to the tertiary mate, the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*TertiaryReferenceType*
:   Tertiary mate's reference type as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)

*TertiaryReferenceAlignment*
:   Tertiary mate's reference alignment as defined by [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Either select the mate references interactively or select them programmatically using [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with marks of 1, 2, and 4. If the mate references are interactively selected, then specify NOTHING for PrimaryReferenceEntity, SecondaryReferenceEntity, and TertiaryReferenceEntity.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)
