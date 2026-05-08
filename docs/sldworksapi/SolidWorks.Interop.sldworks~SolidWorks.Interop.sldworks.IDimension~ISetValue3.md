# ISetValue3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3`

Sets the values of the dimensions in the specified configurations.
Sets the values of the dimensions in the specified configurations.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetValue3( _
   ByVal NewValue As System.Double, _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_count As System.Integer, _
   ByRef Config_names As System.String _
) As System.Integer
```

```

Dim instance As IDimension
Dim NewValue As System.Double
Dim WhichConfigurations As System.Integer
Dim Config_count As System.Integer
Dim Config_names As System.String
Dim value As System.Integer
 
value = instance.ISetValue3(NewValue, WhichConfigurations, Config_count, Config_names)
```

```

System.int ISetValue3( 
   System.double NewValue,
   System.int WhichConfigurations,
   System.int Config_count,
   ref System.string Config_names
)
```

```

System.int ISetValue3( 
   System.double NewValue,
   System.int WhichConfigurations,
   System.int Config_count,
   System.String^% Config_names
) 
```

#### Parameters

*NewValue*
:   Value for this dimension in the units of the owning document

*WhichConfigurations*
:   - in-process, unmanaged C++: Pointer to an array of configurations in which to set this value as defined in [swSetValueInConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html) (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Config\_count*
:   Number of configurations for which to set dimension values (see **Remarks**)

*Config\_names*
:   - in-process, unmanaged C++: Pointer to an array of strings of the names of the configurations for which to set dimension values (see **Remarks**)

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Error code as defined in [swSetValueReturnStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueReturnStatus_e.html)

Remarks

The Config\_count and Config\_names arguments are only used if whichConfigurations is set to swSetValue\_InSpecificConfigurations. Config\_names can contain either a BSTR array or a single BSTR.

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
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md)  
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md)  
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md)  
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md)  
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md)  
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md)
