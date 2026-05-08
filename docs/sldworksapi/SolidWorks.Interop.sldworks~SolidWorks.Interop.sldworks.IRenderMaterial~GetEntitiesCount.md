# GetEntitiesCount Method (IRenderMaterial)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntitiesCount`

Gets the number of entities on which this appearance was applied.
Gets the number of entities on which this appearance was applied.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetEntitiesCount() As System.Integer
```

```

Dim instance As IRenderMaterial
Dim value As System.Integer
 
value = instance.GetEntitiesCount()
```

```

System.int GetEntitiesCount()
```

```

System.int GetEntitiesCount(); 
```

#### Return Value

Number of entities on which this appearance was applied

Remarks

Call this method before calling [IRenderMaterial::IGetEntities](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~IGetEntities.md) to get the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRenderMaterial Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial.md)  
[IRenderMaterial Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial_members.md)  
[IRenderMaterial::AddEntity Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~AddEntity.md)  
[IRenderMaterial::GetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~GetEntities.md)  
[IRenderMaterial::RemoveAllEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenderMaterial~RemoveAllEntities.md)
