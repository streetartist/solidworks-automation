# ReplaceEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation~ReplaceEntity`

Replaces an entity in this sketch relation.
Replaces an entity in this sketch relation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ReplaceEntity( _
   ByVal OldEntity As System.Object, _
   ByVal NewEntity As System.Object _
) As System.Boolean
```

```

Dim instance As ISketchRelation
Dim OldEntity As System.Object
Dim NewEntity As System.Object
Dim value As System.Boolean
 
value = instance.ReplaceEntity(OldEntity, NewEntity)
```

```

System.bool ReplaceEntity( 
   System.object OldEntity,
   System.object NewEntity
)
```

```

System.bool ReplaceEntity( 
   System.Object^ OldEntity,
   System.Object^ NewEntity
) 
```

#### Parameters

*OldEntity*
:   Entity to replace

*NewEntity*
:   Replacement entity

#### Return Value

True if OldEntity is replaced by NewEntity, false if not

Remarks

This method requires that the sketch be in edit mode.

Example

[Replace Sketch Relation (VBA)](Replace_Sketch_Relation_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchRelation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation.md)  
[ISketchRelation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchRelation_members.md)
