# SetVector2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetVector2`

Sets the vector values of a named configuration option parameter.
Sets the vector values of a named configuration option parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetVector2( _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double, _
   ByVal ConfigurationOption As System.Integer, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

```

Dim instance As IParameter
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim ConfigurationOption As System.Integer
Dim ConfigurationName As System.String
Dim value As System.Boolean
 
value = instance.SetVector2(X, Y, Z, ConfigurationOption, ConfigurationName)
```

```

System.bool SetVector2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int ConfigurationOption,
   System.string ConfigurationName
)
```

```

System.bool SetVector2( 
   System.double X,
   System.double Y,
   System.double Z,
   System.int ConfigurationOption,
   System.String^ ConfigurationName
) 
```

#### Parameters

*X*
:   x value to store for the named configuration option

*Y*
:   y value to store for the named configuration option

*Z*
:   z value to store for the named configuration option

*ConfigurationOption*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigurationName*
:   Name of the configuration

#### Return Value

True if successful, false if not

Remarks

The ConfigurationName argument is:

- Not required if ConfigurationOption is set to swThisConfiguration = 1 or swAllConfiguration = 2.
- Required if ConfigurationOption is set to swSpecifyConfiguration = 3.

Set the ConfigurationOption argument to swAllConfiguration = 2 for Drawing Docs as they do not have configurations.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)  
[IParameter::GetVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVector.md)  
[IParameter::GetVectorVB Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetVectorVB.md)
