# SetDoubleValue2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetDoubleValue2`

Sets the double or integer value of a named configuration option parameter.
Sets the double or integer value of a named configuration option parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDoubleValue2( _
   ByVal Value As System.Double, _
   ByVal ConfigurationOption As System.Integer, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

```

Dim instance As IParameter
Dim Value As System.Double
Dim ConfigurationOption As System.Integer
Dim ConfigurationName As System.String
Dim value As System.Boolean
 
value = instance.SetDoubleValue2(Value, ConfigurationOption, ConfigurationName)
```

```

System.bool SetDoubleValue2( 
   System.double Value,
   System.int ConfigurationOption,
   System.string ConfigurationName
)
```

```

System.bool SetDoubleValue2( 
   System.double Value,
   System.int ConfigurationOption,
   System.String^ ConfigurationName
) 
```

#### Parameters

*Value*
:   Value to store for the named configuration option

*ConfigurationOption*
:   Configuration option as defined in [swSetValueInConfiguration\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSetValueInConfiguration_e.html)

*ConfigurationName*
:   Name of the configuration

#### Return Value

True if successful, false if not

Remarks

The ConfigurationName argument is:

- Not required if ConfigurationOption is set to swSetValue\_InThisConfiguration = 1 or swSetValue\_InAllConfigurations = 2.
- Required if ConfigurationOption is set to swSetValue\_InSpecificConfigurations = 3.

Set ConfigurationOption to swSetValue\_InAllConfigurations = 2 for drawing documents because they do not have configurations.

Example

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)  
[Delete Attribute (C#)](Delete_Attribute_Example_CSharp.htm)  
[Delete Attribute (VB.NET)](Delete_Attribute_Example_VBNET.htm)  
[Delete Attribute (VBA)](Delete_Attribute_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)  
[IParameter::GetDoubleValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetDoubleValue.md)
