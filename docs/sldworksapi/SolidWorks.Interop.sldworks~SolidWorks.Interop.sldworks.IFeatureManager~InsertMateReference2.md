# InsertMateReference2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMateReference2`

Inserts a mate reference for a part or assembly document.
Inserts a mate reference for a part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMateReference2( _
   ByVal BstrMateReferenceName As System.String, _
   ByVal PrimaryReferenceEntity As Entity, _
   ByVal PrimaryReferenceType As System.Integer, _
   ByVal PrimaryReferenceAlignment As System.Integer, _
   ByVal PrimaryReferenceAlignAxes As System.Boolean, _
   ByVal SecondaryReferenceEntity As Entity, _
   ByVal SecondaryReferenceType As System.Integer, _
   ByVal SecondaryReferenceAlignment As System.Integer, _
   ByVal SecondaryReferenceAlignAxes As System.Boolean, _
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
Dim PrimaryReferenceAlignAxes As System.Boolean
Dim SecondaryReferenceEntity As Entity
Dim SecondaryReferenceType As System.Integer
Dim SecondaryReferenceAlignment As System.Integer
Dim SecondaryReferenceAlignAxes As System.Boolean
Dim TertiaryReferenceEntity As Entity
Dim TertiaryReferenceType As System.Integer
Dim TertiaryReferenceAlignment As System.Integer
Dim value As Feature
 
value = instance.InsertMateReference2(BstrMateReferenceName, PrimaryReferenceEntity, PrimaryReferenceType, PrimaryReferenceAlignment, PrimaryReferenceAlignAxes, SecondaryReferenceEntity, SecondaryReferenceType, SecondaryReferenceAlignment, SecondaryReferenceAlignAxes, TertiaryReferenceEntity, TertiaryReferenceType, TertiaryReferenceAlignment)
```

```

Feature InsertMateReference2( 
   System.string BstrMateReferenceName,
   Entity PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   System.bool PrimaryReferenceAlignAxes,
   Entity SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   System.bool SecondaryReferenceAlignAxes,
   Entity TertiaryReferenceEntity,
   System.int TertiaryReferenceType,
   System.int TertiaryReferenceAlignment
)
```

```

Feature^ InsertMateReference2( 
   System.String^ BstrMateReferenceName,
   Entity^ PrimaryReferenceEntity,
   System.int PrimaryReferenceType,
   System.int PrimaryReferenceAlignment,
   System.bool PrimaryReferenceAlignAxes,
   Entity^ SecondaryReferenceEntity,
   System.int SecondaryReferenceType,
   System.int SecondaryReferenceAlignment,
   System.bool SecondaryReferenceAlignAxes,
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

*PrimaryReferenceAlignAxes*
:   True to align with the axes of the coordinate system or origin when forming a mate, false to not

*SecondaryReferenceEntity*
:   Pointer to the secondary mate, the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*SecondaryReferenceType*
:   Secondary mate's reference type as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)

*SecondaryReferenceAlignment*
:   Secondary mate's alignment type as defined [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

*SecondaryReferenceAlignAxes*
:   True to align with the axes of the coordinate system or origin when forming a mate, false to not

*TertiaryReferenceEntity*
:   Pointer to the tertiary mate, the [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*TertiaryReferenceType*
:   Tertiary mate's reference type as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html)

*TertiaryReferenceAlignment*
:   Tertiary mate's reference alignment as defined by [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html)

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Example

[Edit Mate Reference (C#)](Edit_Mate_Reference_Example_CSharp.htm)  
[Edit Mate Reference (VB.NET)](Edit_Mate_Reference_Example_VBNET.htm)  
[Edit Mate Reference (VBA)](Edit_Mate_Reference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)
