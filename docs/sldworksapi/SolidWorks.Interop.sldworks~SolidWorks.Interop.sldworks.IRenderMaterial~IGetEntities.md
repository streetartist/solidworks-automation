# IGetEntities Method (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IGetEntities`

Gets the entities on which this appearance is applied.
Gets the entities on which this appearance is applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntities( _
   ByVal Count As System.Integer _
) As System.Object
```

```

Dim instance As IRenderMaterial
Dim Count As System.Integer
Dim value As System.Object
 
value = instance.IGetEntities(Count)
```

```

System.object IGetEntities( 
   System.int Count
)
```

```

System.Object^ IGetEntities( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array of entities on which this appearance is applied

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IRenderMaterial::GetEntitiesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntitiesCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.md)  
[IRenderMaterial::AddEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity.md)  
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.md)
