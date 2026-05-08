# ISetOverrideMomentsOfInertiaValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMomentsOfInertiaValue`

Overrides the moments of inertia of the model currently being edited in this part or assembly document.
Overrides the moments of inertia of the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetOverrideMomentsOfInertiaValue( _
   ByVal ReferenceFrame As System.Integer, _
   ByVal CoordinateSystemName As System.String, _
   ByRef Value As System.Double, _
   ByVal Config_option As System.Integer, _
   ByVal Config_numbers As System.Integer, _
   ByRef Config_names As System.String _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim ReferenceFrame As System.Integer
Dim CoordinateSystemName As System.String
Dim Value As System.Double
Dim Config_option As System.Integer
Dim Config_numbers As System.Integer
Dim Config_names As System.String
Dim value As System.Boolean
 
value = instance.ISetOverrideMomentsOfInertiaValue(ReferenceFrame, CoordinateSystemName, Value, Config_option, Config_numbers, Config_names)
```

```

System.bool ISetOverrideMomentsOfInertiaValue( 
   System.int ReferenceFrame,
   System.string CoordinateSystemName,
   ref System.double Value,
   System.int Config_option,
   System.int Config_numbers,
   ref System.string Config_names
)
```

```

System.bool ISetOverrideMomentsOfInertiaValue( 
   System.int ReferenceFrame,
   System.String^ CoordinateSystemName,
   System.double% Value,
   System.int Config_option,
   System.int Config_numbers,
   System.String^% Config_names
) 
```

#### Parameters

*ReferenceFrame*
:   Frame of reference as defined in [swMomentsOfInertiaReferenceFrame\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMomentsOfInertiaReferenceFrame_e.html)

*CoordinateSystemName*
:   Name of coordinate system; valid only if ReferenceFrame = swMomentsOfInertiaReferenceFrame\_e.swMomentsOfInertiaReferenceFrame\_UserCoordinateSystem

*Value*
:   - in-process, unmanaged C++: Pointer to an array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]
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

True if the moments of inertia are overridden, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::SetOverrideMomentsOfInertiaValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMomentsOfInertiaValue.md)  
[IMassProperty::OverrideMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.md)
