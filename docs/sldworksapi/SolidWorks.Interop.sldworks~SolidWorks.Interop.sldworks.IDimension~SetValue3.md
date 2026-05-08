# SetValue3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3`

Sets the values of the dimensions in the specified configurations.
Sets the values of the dimensions in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetValue3( _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Integer
```

```

Dim instance As IDimension
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim Config_names As System.Object
Dim value As System.Integer
 
value = instance.SetValue3(NewValue, WhichConfigurations, Config_names)
```

```

System.int SetValue3( 
   System.double NewValue,
   System.int WhichConfigurations,
   System.object Config_names
)
```

```

System.int SetValue3( 
   System.double NewValue,
   System.int WhichConfigurations,
   System.Object^ Config_names
) 
```

#### Parameters

*NewValue*
:   Value for this dimension in the units of owning document

*WhichConfigurations*
:   Configurations in which to set this value as defined in [swSetValueInConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html) (see **Remarks**)

*Config\_names*
:   Names of the configurations for which to set dimension values (see **Remarks**)

#### Return Value

Error code as defined in [swSetValueReturnStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

Remarks

The Config\_names argument is only used if WhichConfigurations is set to swSetValue\_InSpecificConfigurations and can contain either a BSTR array or a single BSTR.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::GetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3.md)  
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.md)  
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md)  
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md)  
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md)  
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md)  
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md)  
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md)  
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md)  
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md)  
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md)
