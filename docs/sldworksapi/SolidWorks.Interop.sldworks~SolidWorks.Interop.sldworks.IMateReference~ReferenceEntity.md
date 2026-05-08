# ReferenceEntity Property (IMateReference)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity`

Obsolete. Superseded by IMateReference::ReferenceEntity2.
Obsolete. Superseded by [IMateReference::ReferenceEntity2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntity2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ReferenceEntity( _
   ByVal Index As System.Integer _
) As Entity
```

```

Dim instance As IMateReference
Dim Index As System.Integer
Dim value As Entity
 
value = instance.ReferenceEntity(Index)
```

```

Entity ReferenceEntity( 
   System.int Index
) {get;}
```

```

property Entity^ ReferenceEntity {
   Entity^ get(System.int Index);
}
```

#### Parameters

*Index*
:   Mate reference entity as define by [swMateReferenceIndex\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMateReferenceIndex_e.html)

#### Property Value

[Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

Remarks

Before calling this property, call [IMateReference::ReferenceEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference~ReferenceEntityCount.md) to determine the number of mate reference entities for the mate reference.

Example

[Get Mate Reference Properties (VBA)](Get_Mate_Reference_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference.md)  
[IMateReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateReference_members.md)
