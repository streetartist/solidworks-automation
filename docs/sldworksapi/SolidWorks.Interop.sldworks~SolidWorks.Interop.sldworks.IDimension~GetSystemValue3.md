# GetSystemValue3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetSystemValue3`

Gets the value of the current dimension in system units in the named configuration.
Gets the value of the current dimension in system units in the named configuration.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSystemValue3( _
   ByVal WhichConfigurations As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Object
```

```

Dim instance As IDimension
Dim WhichConfigurations As System.Integer
Dim Config_names As System.Object
Dim value As System.Object
 
value = instance.GetSystemValue3(WhichConfigurations, Config_names)
```

```

System.object GetSystemValue3( 
   System.int WhichConfigurations,
   System.object Config_names
)
```

```

System.Object^ GetSystemValue3( 
   System.int WhichConfigurations,
   System.Object^ Config_names
) 
```

#### Parameters

*WhichConfigurations*
:   Configurations to get this value from as defined by [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html) (see **Remarks**)

*Config\_names*
:   Names of the configuration (see **Remarks**)

#### Return Value

Value in system units

Remarks

The Config\_names argument is only used if whichConfigurations is set to swSpecifyConfiguration.

In OLE, Config\_names can be either a BSTR array or a single BSTR.

Example

[Change Dimensions of Gear Mate (VBA)](Change_Dimensions_of_Gear_Mate_Example_VB.htm)  
[Edit Mate (VBA)](Edit_Mate_Example_VB.htm)  
[Get Dimension of Distance Mate (VBA)](Get_Dimension_of_Distance_Mate_Example_VB.htm)  
[Get Dimension Values in All Configurations (VBA)](Get_Dimension_Values_in_All_Configurations_Example_VB.htm)  
[Get Mate Definition (VBA)](Get_Mate_Definition_Example_VB.htm)  
[Modify Plane By Changing System Value (VBA)](Modify_Plane_by_Changing_System_Value_Example_VB.htm)  
[Get Depth of Extrusion (VBA)](Get_Depth_of_Extrusion_Example_VB.htm)  
[Get Depth of Extrusion (VB.NET)](Get_Depth_of_Extrusion_Example_VBNET.htm)  
[Get Depth of Extrusion (C#)](Get_Depth_of_Extrusion_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDimension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension.md)  
[IDimension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension_members.md)  
[IDimension::IGetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetSystemValue3.md)  
[IDimension::ISetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetSystemValue3.md)  
[IDimension::SetSystemValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetSystemValue3.md)  
[IDimension::SetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetUserValueIn2.md)  
[IDimension::ISetUserValueIn3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetUserValueIn3.md)  
[IDimension::GetUserValueIn Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetUserValueIn.md)  
[IDimension::IGetUserValueIn2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetUserValueIn2.md)  
[IDimension::GetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~GetValue3.md)  
[IDimension::IGetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~IGetValue3.md)  
[IDimension::ISetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~ISetValue3.md)  
[IDimension::SetValue3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDimension~SetValue3.md)
