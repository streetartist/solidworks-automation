# GetUserUnit Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUserUnit`

Gets this document's units settings.
Gets this document's units settings.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUserUnit( _
   ByVal UnitType As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim UnitType As System.Integer
Dim value As System.Object
 
value = instance.GetUserUnit(UnitType)
```

```

System.object GetUserUnit( 
   System.int UnitType
)
```

```

System.Object^ GetUserUnit( 
   System.int UnitType
) 
```

#### Parameters

*UnitType*
:   Document unit type as defined in [swUserUnitsType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserUnitsType_e.html)

#### Return Value

[IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)

Remarks

The properties of IUserUnit are read only. Set them using the IModelDocExtension::SetUserPreference\* methods.

Example

[Get and Set Document Units (VBA)](Get_and_Set_User_Units_Example_VB.htm)  
[Get and Set Document Units (VB.NET)](Get_and_Set_User_Units_Example_VBNET.htm)  
[Get and Set Document Units (C#)](Get_and_Set_User_Units_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::GetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetAngularUnits.md)  
[IModelDoc2::GetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetUnits.md)  
[IModelDoc2::IGetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetAngularUnits.md)  
[IModelDoc2::IGetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUnits.md)  
[IModelDoc2::IGetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetUserUnit.md)  
[IModelDoc2::ISetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ISetAngularUnits.md)  
[IModelDoc2::SetUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetUnits.md)  
[IModelDoc2::SetAngularUnits Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetAngularUnits.md)  
[ISldWorks::GetUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetUserUnit.md)
