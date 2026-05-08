# AddParameter Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~AddParameter`

Adds a parameter to the attribute definition using the specified name and default value.
Adds a parameter to the attribute definition using the specified name and default value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddParameter( _
   ByVal NameIn As System.String, _
   ByVal Type As System.Integer, _
   ByVal DefaultValue As System.Double, _
   ByVal Options As System.Integer _
) As System.Boolean
```

```

Dim instance As IAttributeDef
Dim NameIn As System.String
Dim Type As System.Integer
Dim DefaultValue As System.Double
Dim Options As System.Integer
Dim value As System.Boolean
 
value = instance.AddParameter(NameIn, Type, DefaultValue, Options)
```

```

System.bool AddParameter( 
   System.string NameIn,
   System.int Type,
   System.double DefaultValue,
   System.int Options
)
```

```

System.bool AddParameter( 
   System.String^ NameIn,
   System.int Type,
   System.double DefaultValue,
   System.int Options
) 
```

#### Parameters

*NameIn*
:   Name to be given to the parameter (see **Remarks**)

*Type*
:   Parameter type as defined in [swParamType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swParamType_e.html)

*DefaultValue*
:   Default value (see **Remarks**)

*Options*
:   Not used

#### Return Value

True if the parameter is added successfully, false if not

Remarks

Parameters cannot be added after the attribute definition is registered.

The name of the parameter given by NameIn must be unique in the attribute definition.

For parameters of type swParamTypeDouble, the DefaultValue argument allows a default value to be placed in the attribute definition parameter. This value is assigned to the parameters of newly created attribute instances.

**NOTE:** There is no way to get or set integer parameters in attributes. Instead, use [IParameter::GetDoubleValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~GetDoubleValue.md) and [IParameter::SetDoubleValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetDoubleValue2.md) to get and set values for integer parameters. If you need to store a negative value, define your attribute parameter as type double. SOLIDWORKS does not allow negative integer values.

Example

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)  
[Add Attribute to Feature and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)  
[Find Attribute (C#)](Find_Attribute_Example_CSharp.htm)  
[Find Attribute (VB.NET)](Find_Attribute_Example_VBNET.htm)  
[Find Attribute (VBA)](Find_Attribute_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttributeDef Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef.md)  
[IAttributeDef Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef_members.md)  
[IAttribute::Register Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttributeDef~Register.md)  
[ISldWorks::DefineAttribute Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~DefineAttribute.md)
