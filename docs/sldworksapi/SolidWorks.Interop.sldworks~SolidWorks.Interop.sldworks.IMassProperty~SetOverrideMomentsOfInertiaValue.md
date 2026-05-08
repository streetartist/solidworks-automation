# SetOverrideMomentsOfInertiaValue Method (IMassProperty)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverrideMomentsOfInertiaValue`

Overrides the moments of inertia of the model currently being edited in this part or assembly document.
Overrides the moments of inertia of the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverrideMomentsOfInertiaValue( _
   ByVal ReferenceFrame As System.Integer, _
   ByVal CoordinateSystemName As System.String, _
   ByVal Value As System.Object, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim ReferenceFrame As System.Integer
Dim CoordinateSystemName As System.String
Dim Value As System.Object
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetOverrideMomentsOfInertiaValue(ReferenceFrame, CoordinateSystemName, Value, Config_option, Config_names)
```

```

System.bool SetOverrideMomentsOfInertiaValue( 
   System.int ReferenceFrame,
   System.string CoordinateSystemName,
   System.object Value,
   System.int Config_option,
   System.object Config_names
)
```

```

System.bool SetOverrideMomentsOfInertiaValue( 
   System.int ReferenceFrame,
   System.String^ CoordinateSystemName,
   System.Object^ Value,
   System.int Config_option,
   System.Object^ Config_names
) 
```

#### Parameters

*ReferenceFrame*
:   Frame of reference as defined in [swMomentsOfInertiaReferenceFrame\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMomentsOfInertiaReferenceFrame_e.html)

*CoordinateSystemName*
:   Name of coordinate system; valid only if ReferenceFrame = swMomentsOfInertiaReferenceFrame\_e.swMomentsOfInertiaReferenceFrame\_UserCoordinateSystem

*Value*
:   Array of nine doubles: [ Lxx, Lxy, Lxz, Lyx, Lyy, Lyz, Lzx, Lzy, Lzz ]

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names; valid only if Config\_option = swInConfigurationOpts\_e.swSpecifyConfiguration

#### Return Value

True if the moments of inertia are overridden, false if not

Example

[Get and Override Mass Properties (VBA)](Get_Mass_Properties_using_MassProperty_Object_Example_VB.htm)  
[Get and Override Mass Properties (VB.NET)](Get_Mass_Properties_Using_IMassProperty_Example_VBNET.htm)  
[Get and Override Mass Properties (C#)](Get_Mass_Properties_Using_IMassProperty_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::ISetOverrideMomentsOfInertiaValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverrideMomentsOfInertiaValue.md)  
[IMassProperty::OverrideMomentsOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~OverrideMomentsOfInertia.md)
