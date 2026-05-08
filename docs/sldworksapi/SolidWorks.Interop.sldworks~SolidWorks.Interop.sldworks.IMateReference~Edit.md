# Edit Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~Edit`

Lets you edit the selected mate reference.
Lets you edit the selected mate reference.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Edit( _
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
) As System.Boolean
```

```

Dim instance As IMateReference
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
Dim value As System.Boolean
 
value = instance.Edit(BstrMateReferenceName, PrimaryReferenceEntity, PrimaryReferenceType, PrimaryReferenceAlignment, SecondaryReferenceEntity, SecondaryReferenceType, SecondaryReferenceAlignment, TertiaryReferenceEntity, TertiaryReferenceType, TertiaryReferenceAlignment)
```

```

System.bool Edit( 
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

System.bool Edit( 
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
:   Name of the new mate reference, which replaces the selected mate reference

*PrimaryReferenceEntity*
:   Primary mate reference entity, a pointer to an [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*PrimaryReferenceType*
:   Type of mate as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html) for PrimaryReferenceEntity

*PrimaryReferenceAlignment*
:   Type of alignment as defined by [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html) for PrimaryReferenceEntity

*SecondaryReferenceEntity*
:   Secondary mate reference entity, a pointer to an [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*SecondaryReferenceType*
:   Type of mate as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html) for SecondaryReferenceEntity

*SecondaryReferenceAlignment*
:   Type of alignment as defined by [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html) for SecondaryReferenceEntity

*TertiaryReferenceEntity*
:   Tertiary mate reference entity, a pointer to an [IEntity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md) object

*TertiaryReferenceType*
:   Type of mate as defined by [swMateReferenceType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceType_e.html) for TertiaryReferenceEntity

*TertiaryReferenceAlignment*
:   Type of alignment as defined by [swMateReferenceAlignment\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceAlignment_e.html) for TertiaryReferenceEntity

#### Return Value

Always True

Remarks

To clear the previous references, you can pass Nothing or null for the primary, secondary, or tertiary reference entities.

This method applies the parameters to the actual features. After calling this method, call [IModelDoc2::EditRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~EditRebuild3.md) to rebuild the model, and then call [IModelDocExtension::NeedsRebuild](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~NeedsRebuild.md) to determine if the rebuild was successful.

Example

[Edit Mate Reference (C#)](Edit_Mate_Reference_Example_CSharp.htm)  
[Edit Mate Reference (VB.NET)](Edit_Mate_Reference_Example_VBNET.htm)  
[Edit Mate Reference (VBA)](Edit_Mate_Reference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)  
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.md)
