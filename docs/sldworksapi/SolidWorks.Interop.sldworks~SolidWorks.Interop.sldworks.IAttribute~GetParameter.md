# GetParameter Method (IAttribute)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter`

Gets the specified parameter on this attribute.
Gets the specified parameter on this attribute.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetParameter( _
   ByVal NameIn As System.String _
) As System.Object
```

```

Dim instance As IAttribute
Dim NameIn As System.String
Dim value As System.Object
 
value = instance.GetParameter(NameIn)
```

```

System.object GetParameter( 
   System.string NameIn
)
```

```

System.Object^ GetParameter( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Name of the parameter

#### Return Value

Object for the parameter

Example

[Create Attribute (VBA)](Create_Attribute_Example_VB.htm)  
[Add Attribute to Feature and Include in Library Feature (C#)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_CSharp.htm)  
[Add Attribute to Feautre and Include in Library Feature (VB.NET)](Add_Attribute_to_Feature_and_Include_in_Library_Feature_Example_VBNET.htm)  
[Add Attribute to Feature and Include in Library Feature (VBA)](Add_Attribute_to_Feature_and_Include_In_Library_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[IAttribute::IGetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter.md)
