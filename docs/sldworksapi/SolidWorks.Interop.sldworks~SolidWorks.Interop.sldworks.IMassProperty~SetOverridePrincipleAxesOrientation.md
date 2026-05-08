# SetOverridePrincipleAxesOrientation Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~SetOverridePrincipleAxesOrientation`

Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document.
Overrides the orientation of the specified principal axis of inertia for the model currently being edited in this part or assembly document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetOverridePrincipleAxesOrientation( _
   ByVal Axis As System.Integer, _
   ByVal Value As System.Object, _
   ByVal Config_option As System.Integer, _
   ByVal Config_names As System.Object _
) As System.Boolean
```

```

Dim instance As IMassProperty
Dim Axis As System.Integer
Dim Value As System.Object
Dim Config_option As System.Integer
Dim Config_names As System.Object
Dim value As System.Boolean
 
value = instance.SetOverridePrincipleAxesOrientation(Axis, Value, Config_option, Config_names)
```

```

System.bool SetOverridePrincipleAxesOrientation( 
   System.int Axis,
   System.object Value,
   System.int Config_option,
   System.object Config_names
)
```

```

System.bool SetOverridePrincipleAxesOrientation( 
   System.int Axis,
   System.Object^ Value,
   System.int Config_option,
   System.Object^ Config_names
) 
```

#### Parameters

*Axis*
:   One of the following principal axes:

    - 0 = X axis
    - 1 = Y axis
    - 2 = Z axis

*Value*
:   An array of three doubles of the x, y, and z coordinates of Axis

*Config\_option*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*Config\_names*
:   Array of configuration names; valid only if Config\_option = swInConfigurationOpts\_e.swSpecifyConfiguration

#### Return Value

True if orientation of principal axis is overridden, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMassProperty Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty.md)  
[IMassProperty Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty_members.md)  
[IMassProperty::ISetOverridePrincipleAxesOrientation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~ISetOverridePrincipleAxesOrientation.md)  
[IMassProperty::PrincipleAxesOfInertia Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMassProperty~PrincipleAxesOfInertia.md)
