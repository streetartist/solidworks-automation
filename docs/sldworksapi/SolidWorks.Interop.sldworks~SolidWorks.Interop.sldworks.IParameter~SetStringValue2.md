# SetStringValue2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetStringValue2`

Sets the double or integer value of a named configuration option parameter.
Sets the double or integer value of a named configuration option parameter.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStringValue2( _
   ByVal StringValue As System.String, _
   ByVal ConfigurationOption As System.Integer, _
   ByVal ConfigurationName As System.String _
) As System.Boolean
```

```

Dim instance As IParameter
Dim StringValue As System.String
Dim ConfigurationOption As System.Integer
Dim ConfigurationName As System.String
Dim value As System.Boolean
 
value = instance.SetStringValue2(StringValue, ConfigurationOption, ConfigurationName)
```

```

System.bool SetStringValue2( 
   System.string StringValue,
   System.int ConfigurationOption,
   System.string ConfigurationName
)
```

```

System.bool SetStringValue2( 
   System.String^ StringValue,
   System.int ConfigurationOption,
   System.String^ ConfigurationName
) 
```

#### Parameters

*StringValue*
:   Value to store for the named configuration option

*ConfigurationOption*
:   Configuration option as defined in [swInConfigurationOpts\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swInConfigurationOpts_e.html)

*ConfigurationName*
:   Name of the configuration

#### Return Value

True if successful, false if not

Remarks

The ConfigurationName argument is:

- Not required if ConfigurationOption is set to swThisConfiguration = 1 or swAllConfiguration = 2.
- Required if ConfigurationOption is set to swSpecifyConfiguration =3 .

Set ConfigurationOption to swAllConfiguration = 2 for drawing documents because they do not have configurations.

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
[IParameter::GetStringValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetStringValue.md)
