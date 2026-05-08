# Delete2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Delete2`

Deletes the specified custom property.
Deletes the specified custom property.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Delete2( _
   ByVal FieldName As System.String _
) As System.Integer
```

```

Dim instance As ICustomPropertyManager
Dim FieldName As System.String
Dim value As System.Integer
 
value = instance.Delete2(FieldName)
```

```

System.int Delete2( 
   System.string FieldName
)
```

```

System.int Delete2( 
   System.String^ FieldName
) 
```

#### Parameters

*FieldName*
:   Name of the custom property to delete

#### Return Value

Result code as defined in [swCustomInfoDeleteResult\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCustomInfoDeleteResult_e.html)

Example

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)  
[Get Custom Properties for Configuration (VB.NET)](Get_Custom_Properties_for_Configuration_Example_VBNET.htm)  
[Get Custom Properties for Configuration (C#)](Get_Custom_Properties_for_Configuration_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICustomPropertyManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager.md)  
[ICustomPropertyManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager_members.md)  
[ICustomPropertyManager::Add3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICustomPropertyManager~Add3.md)
