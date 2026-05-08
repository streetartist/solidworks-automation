# Get2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get2`

Obsolete. Superseded by ICustomPropertyManager::Get3.
Obsolete. Superseded by [ICustomPropertyManager::Get3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Get3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub Get2( _
   ByVal FieldName As System.String, _
   ByRef ValOut As System.String, _
   ByRef ReesolvedValOut As System.String _
) 
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim ValOut As System.String
Dim ReesolvedValOut As System.String
 
instance.Get2(FieldName, ValOut, ReesolvedValOut)
```

```

void Get2( 
   System.string FieldName,
   out System.string ValOut,
   out System.string ReesolvedValOut
)
```

```

void Get2( 
   System.String^ FieldName,
   [Out] System.String^ ValOut,
   [Out] System.String^ ReesolvedValOut
) 
```

#### Parameters

*FieldName*
:   Name of the custom property

*ValOut*
:   Value of the custom property

*ReesolvedValOut*
:   Evaluated value of the custom property

Example

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)  
[Get Custom Properties for Cut-list Item (VBA)](Get_Custom_Properties_for_Cut-list_Item_Example_VB.htm)  
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (C#)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_CSharp.htm)  
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VB.NET)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VBNET.htm)  
[Get Solid Bodies from Cut-list Folders and Get Custom Properties (VBA)](Get_Solid_Bodies_from_Cut-list_Folders_and_Get_Custom_Properties_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::GetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~GetAll.md)  
[ICustomPropertyManager::IGetAll Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~IGetAll.md)  
[ICustomPropertyManager::Set Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Set.md)
