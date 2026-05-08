# LockLightToModel Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~LockLightToModel`

Locks or unlocks the specified light.
Locks or unlocks the specified light.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function LockLightToModel( _
   ByVal LightId As System.Integer, _
   ByVal Fix As System.Boolean _
) As System.Boolean
```

```

Dim instance As IModelDoc2
Dim LightId As System.Integer
Dim Fix As System.Boolean
Dim value As System.Boolean
 
value = instance.LockLightToModel(LightId, Fix)
```

```

System.bool LockLightToModel( 
   System.int LightId,
   System.bool Fix
)
```

```

System.bool LockLightToModel( 
   System.int LightId,
   System.bool Fix
) 
```

#### Parameters

*LightId*
:   Light ID

*Fix*
:   True if the light is locked, false if not

#### Return Value

True if change is successful, false if not

Example

[Add Spotlight and Get Light Feature (C#)](Add_Spotlight_and_Get_Light_Feature_Example_CSharp.htm)  
[Add Spotlight and Get Light Feature (VB.NET)](Add_Spotlight_and_Get_Light_Feature_Example_VBNET.htm)  
[Add Spotlight and Get Light Feature (VBA)](Add_Spotlight_and_Get_Light_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IsLightLockedToModel Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsLightLockedToModel.md)  
[IModelDoc2::GetLightSourceIdFromName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetLightSourceIdFromName.md)
