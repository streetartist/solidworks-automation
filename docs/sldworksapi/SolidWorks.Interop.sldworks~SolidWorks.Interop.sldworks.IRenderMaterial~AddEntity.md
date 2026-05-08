# AddEntity Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity`

Adds the appearance to the specified entity.
Adds the appearance to the specified entity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddEntity( _
   ByVal Entity As System.Object _
) As System.Boolean
```

```

Dim instance As IRenderMaterial
Dim Entity As System.Object
Dim value As System.Boolean
 
value = instance.AddEntity(Entity)
```

```

System.bool AddEntity( 
   System.object Entity
)
```

```

System.bool AddEntity( 
   System.Object^ Entity
) 
```

#### Parameters

*Entity*
:   Entity to which to add the appearance

#### Return Value

True if the appearance is added to Entity, false if not

Example

See [IRenderMaterial](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.md)  
[IRenderMaterial::GetEntitiesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntitiesCount.md)  
[IRenderMaterial::IGetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IGetEntities.md)  
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.md)
