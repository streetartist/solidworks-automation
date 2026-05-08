# IGetEntities Method (IDisplayStateSetting)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~IGetEntities`

Gets the entities for this display state setting.
Gets the entities for this display state setting.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetEntities( _
   ByVal EntityCount As System.Integer _
) As System.Object
```

```

Dim instance As IDisplayStateSetting
Dim EntityCount As System.Integer
Dim value As System.Object
 
value = instance.IGetEntities(EntityCount)
```

```

System.object IGetEntities( 
   System.int EntityCount
)
```

```

System.Object^ IGetEntities( 
   System.int EntityCount
) 
```

#### Parameters

*EntityCount*
:   Number of entities

#### Return Value

- in-process, unmanaged C++: Pointer to an array entities
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IDisplayStateSetting::GetEntityCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~GetEntityCount.md) to populate EntityCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDisplayStateSetting Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting.md)  
[IDisplayStateSetting Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting_members.md)  
[IDisplayStateSetting::Entities Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~Entities.md)  
[IDisplayStateSetting::ISetEntities Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDisplayStateSetting~ISetEntities.md)
