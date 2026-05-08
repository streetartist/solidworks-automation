# ISetOverridePrincipleAxesOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleAxesOrientation`

Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document.
Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetOverridePrincipleAxesOrientation( _
   ByVal Axis As System.Integer, _
   ByRef Value As System.Double, _
   ByVal Config_option As System.Integer, _
   ByVal Config_numbers As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Axis As System.Integer
Dim Value As System.Double
Dim Config_option As System.Integer
Dim Config_numbers As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean
 
value = instance.ISetOverridePrincipleAxesOrientation(Axis, Value, Config_option, Config_numbers, Config_names)
```

```

System.bool ISetOverridePrincipleAxesOrientation( 
   System.int Axis,
   ref System.double Value,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

```

System.bool ISetOverridePrincipleAxesOrientation( 
   System.int Axis,
   System.double% Value,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
) 
```

#### Parameters

*Axis*
:   One of the following principal axes:

    - 0 = X axis
    - 1 = Y axis
    - 2 = Z axis

*Value*
:   - in-process, unmanaged C++: Pointer to an array of three doubles of the x, y, and z coordinates of the specified principal Axis
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_numbers*
:   Number of configurations

*Config\_names*
:   - in-process, unmanaged C++: Pointer to an array of configuration names of size Config\_numbers; valid only if Config\_option = swInConfigurationOpts\_e.swSpecifyConfiguration
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if orientation of principal axis is overridden, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::SetOverridePrincipleAxesOrientation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleAxesOrientation.md)  
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.md)
