# IsLightLockedToModel Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsLightLockedToModel`

Gets whether the specified light is fixed.
Gets whether the specified light is fixed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsLightLockedToModel( _
   ByVal LightId As System.Integer _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim LightId As System.Integer
Dim value As System.Boolean
 
value = instance.IsLightLockedToModel(LightId)
```

```

System.bool IsLightLockedToModel( 
   System.int LightId
)
```

```

System.bool IsLightLockedToModel( 
   System.int LightId
) 
```

#### Parameters

*LightId*
:   Light ID

#### Return Value

True if the light is fixed, false otherwise

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.md)  
[IModelDoc2::LockLightToModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockLightToModel.md)
