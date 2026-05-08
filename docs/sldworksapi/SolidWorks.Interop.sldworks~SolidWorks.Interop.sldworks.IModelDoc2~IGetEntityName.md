# IGetEntityName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetEntityName`

Gets the name of the specified face, edge, or vertex.
Gets the name of the specified face, edge, or vertex.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntityName( _
   ByVal Entity As Entity _
) As System.String
```

```

Dim instance As IModelDoc2
Dim Entity As Entity
Dim value As System.String
 
value = instance.IGetEntityName(Entity)
```

```

System.string IGetEntityName( 
   Entity Entity
)
```

```

System.String^ IGetEntityName( 
   Entity^ Entity
) 
```

#### Parameters

*Entity*
:   [Entity](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEntity.md)

#### Return Value

Name of the entity

Example

[Get Entity Name (C++)](Get_Entity_Name_Example_CPlusPlus_COM.htm)  
[Get Named Entities (C++)](Get_Named_Entities_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetEntityName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetEntityName.md)
