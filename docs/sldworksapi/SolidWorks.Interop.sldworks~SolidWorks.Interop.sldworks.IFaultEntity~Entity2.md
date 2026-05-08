# Entity2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Entity2`

Gets the specified entity.
Gets the specified entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property Entity2( _
   ByVal Index As System.Integer _
) As System.Object
```

```

Dim instance As IFaultEntity
Dim Index As System.Integer
Dim value As System.Object
 
value = instance.Entity2(Index)
```

```

System.object Entity2( 
   System.int Index
) {get;}
```

```

property System.Object^ Entity2 {
   System.Object^ get(System.int Index);
}
```

#### Parameters

*Index*
:   0-based index number indicating the entity to get

#### Property Value

Entity at Index or NULL if the object at Index is not an entity

Remarks

To determine the value for Index, call [IFaultEntity::Count](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~Count.md) before calling this property. Call [IFaultEntity::ErrorCode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity~ErrorCode.md) to determine the error code.

This method might return NULL if the entity is absorbed by the fault.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFaultEntity Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity.md)  
[IFaultEntity Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFaultEntity_members.md)
