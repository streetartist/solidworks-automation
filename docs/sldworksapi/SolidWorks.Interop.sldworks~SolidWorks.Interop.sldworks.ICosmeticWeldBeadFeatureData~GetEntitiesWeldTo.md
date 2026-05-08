# GetEntitiesWeldTo Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldTo`

Gets the weld-to entity type and weld-to entities for this cosmetic weld bead, which was created using weld geometry.
Gets the weld-to entity type and weld-to entities for this cosmetic weld bead, which was created using weld geometry.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesWeldTo( _
   ByRef EntType As System.Integer _
) As System.Object
```

```

Dim instance As ICosmeticWeldBeadFeatureData
Dim EntType As System.Integer
Dim value As System.Object
 
value = instance.GetEntitiesWeldTo(EntType)
```

```

System.object GetEntitiesWeldTo( 
   out System.int EntType
)
```

```

System.Object^ GetEntitiesWeldTo( 
   [Out] System.int EntType
) 
```

#### Parameters

*EntType*
:   Weld-to entity type as defined in [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html); i.e., either swSelFACES or swSelEDGES

#### Return Value

Array of weld-to entities of [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) or [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Example

[Insert Cosmetic Weld Bead Using Geometric Entities (C#)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_CSharp.htm)  
[Insert Cosmetic Weld Bead Using Geometric Entities (VB.NET)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VBNET.htm)  
[Insert Cosmetic Weld Bead Using Geometric Entities (VBA)](Insert_Cosmetic_Weld_Bead_Using_Geometric_Entities_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICosmeticWeldBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData.md)  
[ICosmeticWeldBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData_members.md)  
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldTo](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldTo.md)  
[ICosmeticWeldBeadFeatureData::GetEntitiesWeldFrom](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~GetEntitiesWeldFrom.md)  
[ICosmeticWeldBeadFeatureData::SetEntitiesWeldFrom Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICosmeticWeldBeadFeatureData~SetEntitiesWeldFrom.md)
